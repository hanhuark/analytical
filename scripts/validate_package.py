#!/usr/bin/env python3
"""Validate analytical-package structure, schemas, and recorded gate evidence.

This validator checks whether a package satisfies the declared artifact contract. It cannot
establish that equations, citations, measurements, or scientific conclusions are true.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SPEC_PATH = SCRIPT_DIR / "package_spec.json"
CONTRACT_SCHEMA_PATH = SCRIPT_DIR / "problem_contract.schema.json"
PLACEHOLDER_RE = re.compile(r"\b(?:REPLACE_ME|TODO|TBD)\b", re.IGNORECASE)
ID_RE = re.compile(r"^[A-Z][1-9][0-9]*$")


def load_json(path: Path, label: str, errors: list[str]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{label} is not valid JSON: {exc}")
    except OSError as exc:
        errors.append(f"cannot read {label}: {exc}")
    return None


def load_configuration() -> tuple[dict[str, Any], dict[str, Any]]:
    errors: list[str] = []
    spec = load_json(SPEC_PATH, "package_spec.json", errors)
    schema = load_json(CONTRACT_SCHEMA_PATH, "problem_contract.schema.json", errors)
    if errors or not isinstance(spec, dict) or not isinstance(schema, dict):
        raise RuntimeError("; ".join(errors) or "invalid validator configuration")
    return spec, schema


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def contains_placeholder(value: Any) -> bool:
    if isinstance(value, str):
        return bool(PLACEHOLDER_RE.search(value))
    if isinstance(value, list):
        return any(contains_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(contains_placeholder(item) for item in value.values())
    return False


def require_string(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty string")


def require_string_list(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{label} must be a non-empty list")
        return
    for index, item in enumerate(value):
        require_string(item, f"{label}[{index}]", errors)


def validate_object_fields(
    value: Any,
    label: str,
    required: set[str],
    errors: list[str],
    *,
    allow_extra: bool = False,
) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return None
    missing = required - value.keys()
    if missing:
        errors.append(f"{label} missing keys: {', '.join(sorted(missing))}")
    if not allow_extra:
        extra = value.keys() - required
        if extra:
            errors.append(f"{label} has unsupported keys: {', '.join(sorted(extra))}")
    for field in required & value.keys():
        if is_empty(value[field]):
            errors.append(f"{label}.{field} must not be empty")
    return value


def validate_object_list(
    value: Any,
    label: str,
    required: set[str],
    errors: list[str],
) -> list[dict[str, Any]]:
    if not isinstance(value, list) or not value:
        errors.append(f"{label} must be a non-empty list")
        return []
    valid: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        checked = validate_object_fields(item, f"{label}[{index}]", required, errors)
        if checked is not None:
            valid.append(checked)
    return valid


def validate_contract(
    path: Path, spec: dict[str, Any], schema: dict[str, Any]
) -> tuple[list[str], dict[str, Any] | None]:
    errors: list[str] = []
    contract = load_json(path, "problem_contract.json", errors)
    if not isinstance(contract, dict):
        if contract is not None:
            errors.append("problem_contract.json root must be an object")
        return errors, None

    required = set(schema.get("required", []))
    missing = required - contract.keys()
    extra = contract.keys() - set(schema.get("properties", {}))
    if missing:
        errors.append(f"problem contract missing keys: {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"problem contract has unsupported keys: {', '.join(sorted(extra))}")
    for key in required & contract.keys():
        if is_empty(contract[key]):
            errors.append(f"problem contract field {key!r} must not be empty")

    supported_versions = set(spec["supported_contract_schema_versions"])
    if contract.get("schema_version") not in supported_versions:
        errors.append(
            "problem contract schema_version is unsupported: "
            f"{contract.get('schema_version')!r}; expected one of {sorted(supported_versions)}"
        )

    evidence_states = set(spec["evidence_states"])
    if contract.get("evidence_state") not in evidence_states:
        errors.append(f"problem contract evidence_state is invalid: {contract.get('evidence_state')!r}")
    for key in (
        "title",
        "decision_or_claim",
        "event_definition",
        "system_boundary",
        "geometry_and_frame",
        "frame_and_invariance",
        "calibration_boundary",
        "uncertainty_plan",
    ):
        require_string(contract.get(key), key, errors)

    model_status = contract.get("model_status")
    if model_status not in set(spec["model_statuses"]):
        errors.append(f"problem contract model_status is invalid: {model_status!r}")
    claim_rung = contract.get("claim_ladder_rung")
    if not isinstance(claim_rung, int) or isinstance(claim_rung, bool) or not 1 <= claim_rung <= 8:
        errors.append("problem contract claim_ladder_rung must be an integer from 1 through 8")
    else:
        allowed_rungs = set(spec["model_status_rungs"].get(model_status, []))
        if allowed_rungs and claim_rung not in allowed_rungs:
            errors.append(
                f"problem contract model_status {model_status!r} is inconsistent with "
                f"claim_ladder_rung {claim_rung}"
            )

    regime = validate_object_fields(
        contract.get("regime"),
        "regime",
        {"description", "included", "excluded"},
        errors,
    )
    if regime:
        require_string(regime.get("description"), "regime.description", errors)
        require_string_list(regime.get("included"), "regime.included", errors)
        require_string_list(regime.get("excluded"), "regime.excluded", errors)

    condition_fields = {"name", "range", "unit", "property_state", "evidence_state"}
    conditions = validate_object_list(
        contract.get("operating_conditions"), "operating_conditions", condition_fields, errors
    )
    for index, condition in enumerate(conditions):
        for field in condition_fields - {"evidence_state"}:
            require_string(condition.get(field), f"operating_conditions[{index}].{field}", errors)
        if condition.get("evidence_state") not in evidence_states:
            errors.append(
                f"operating_conditions[{index}].evidence_state is invalid: "
                f"{condition.get('evidence_state')!r}"
            )

    variable_fields = {
        "name",
        "symbol",
        "dimension",
        "unit",
        "sign_convention",
        "role",
        "property_state",
        "definition",
        "evidence_state",
    }
    for group in ("dependent_variables", "governing_variables"):
        variables = validate_object_list(contract.get(group), group, variable_fields, errors)
        for index, variable in enumerate(variables):
            for field in variable_fields - {"evidence_state"}:
                require_string(variable.get(field), f"{group}[{index}].{field}", errors)
            if variable.get("evidence_state") not in evidence_states:
                errors.append(
                    f"{group}[{index}].evidence_state is invalid: "
                    f"{variable.get('evidence_state')!r}"
                )

    closure_fields = {
        "id",
        "name",
        "relation",
        "status",
        "provenance",
        "calibration_boundary",
        "evidence_state",
    }
    closures = validate_object_list(
        contract.get("constitutive_closures"), "constitutive_closures", closure_fields, errors
    )
    closure_ids: set[str] = set()
    for index, closure in enumerate(closures):
        closure_id = closure.get("id")
        if not isinstance(closure_id, str) or not re.fullmatch(r"C[1-9][0-9]*", closure_id):
            errors.append(f"constitutive_closures[{index}].id must match C<number>")
        elif closure_id in closure_ids:
            errors.append(f"duplicate constitutive closure id: {closure_id}")
        else:
            closure_ids.add(closure_id)
        for field in closure_fields - {"status", "evidence_state"}:
            require_string(closure.get(field), f"constitutive_closures[{index}].{field}", errors)
        if closure.get("status") not in set(spec["closure_statuses"]):
            errors.append(f"constitutive_closures[{index}].status is invalid: {closure.get('status')!r}")
        if closure.get("evidence_state") not in evidence_states:
            errors.append(
                f"constitutive_closures[{index}].evidence_state is invalid: "
                f"{closure.get('evidence_state')!r}"
            )

    for key in (
        "materials_or_fluids",
        "initial_conditions",
        "boundary_conditions",
        "conservation_laws",
        "source_and_sink_terms",
        "assumptions",
        "exclusions",
        "baselines",
        "acceptance_criteria",
        "falsification_cases",
        "benchmark_plan",
        "provenance",
    ):
        require_string_list(contract.get(key), key, errors)

    scale = validate_object_fields(
        contract.get("scale_analysis"),
        "scale_analysis",
        {"reference_scales", "dimensionless_groups", "ordering_parameters", "expected_reduction_error"},
        errors,
    )
    if scale:
        for key in ("reference_scales", "dimensionless_groups", "ordering_parameters"):
            require_string_list(scale.get(key), f"scale_analysis.{key}", errors)
        require_string(
            scale.get("expected_reduction_error"),
            "scale_analysis.expected_reduction_error",
            errors,
        )

    if contains_placeholder(contract):
        errors.append("problem contract contains an unfilled placeholder")
    return errors, contract


def parse_markdown_tables(lines: list[str]) -> list[tuple[list[str], list[list[str]]]]:
    tables: list[tuple[list[str], list[list[str]]]] = []
    index = 0
    while index + 1 < len(lines):
        header_line = lines[index].strip()
        separator_line = lines[index + 1].strip()
        if not header_line.startswith("|") or not separator_line.startswith("|"):
            index += 1
            continue
        headers = [cell.strip() for cell in header_line.strip("|").split("|")]
        separators = [cell.strip() for cell in separator_line.strip("|").split("|")]
        if len(headers) != len(separators) or not separators or not all(
            re.fullmatch(r":?-{3,}:?", cell) for cell in separators
        ):
            index += 1
            continue
        rows: list[list[str]] = []
        cursor = index + 2
        while cursor < len(lines) and lines[cursor].strip().startswith("|"):
            rows.append([cell.strip() for cell in lines[cursor].strip().strip("|").split("|")])
            cursor += 1
        tables.append((headers, rows))
        index = cursor
    return tables


def validate_markdown(path: Path, requirement: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"cannot read {path.name}: {exc}"]

    if PLACEHOLDER_RE.search(text):
        errors.append(f"{path.name} contains an unfilled placeholder")

    lines = text.splitlines()
    heading_positions: dict[str, int] = {}
    for index, line in enumerate(lines):
        if line.startswith("## "):
            heading_positions[line[3:].strip()] = index

    required_headings = requirement.get("headings", [])
    for heading in required_headings:
        if heading not in heading_positions:
            errors.append(f"{path.name} missing required heading: {heading}")
            continue
        start = heading_positions[heading] + 1
        end = next(
            (index for index in range(start, len(lines)) if lines[index].startswith("## ")),
            len(lines),
        )
        body = [line.strip() for line in lines[start:end] if line.strip()]
        prose = [line for line in body if not line.startswith(("|", "```"))]
        body_tables = parse_markdown_tables(body)
        if not prose and not any(rows for _, rows in body_tables):
            errors.append(f"{path.name} has no content under heading: {heading}")

    parsed_tables = parse_markdown_tables(lines)
    for table_requirement in requirement.get("tables", []):
        expected_headers = table_requirement["headers"]
        matching = [rows for headers, rows in parsed_tables if headers == expected_headers]
        if not matching:
            errors.append(
                f"{path.name} missing required table with headers: "
                + " | ".join(expected_headers)
            )
            continue
        rows = matching[0]
        minimum_rows = table_requirement.get("minimum_rows", 0)
        if len(rows) < minimum_rows:
            errors.append(
                f"{path.name} table '{expected_headers[0]}' requires at least "
                f"{minimum_rows} substantive row(s); found {len(rows)}"
            )
        prefix = table_requirement.get("id_prefix")
        row_ids: list[str] = []
        for row_index, row in enumerate(rows, start=1):
            if len(row) != len(expected_headers):
                errors.append(
                    f"{path.name} table '{expected_headers[0]}' row {row_index} has "
                    f"{len(row)} columns; expected {len(expected_headers)}"
                )
                continue
            if any(not cell for cell in row):
                errors.append(
                    f"{path.name} table '{expected_headers[0]}' row {row_index} contains an empty cell"
                )
            if prefix:
                row_id = row[0]
                if not re.fullmatch(rf"{re.escape(prefix)}[1-9][0-9]*", row_id):
                    errors.append(
                        f"{path.name} table '{expected_headers[0]}' row {row_index} "
                        f"requires an ID matching {prefix}<number>"
                    )
                else:
                    row_ids.append(row_id)
        if prefix and len(row_ids) != len(set(row_ids)):
            errors.append(f"{path.name} contains duplicate {prefix}<number> identifiers")

    return errors


def validate_derivations(path: Path) -> list[str]:
    errors: list[str] = []
    files = [item for item in path.rglob("*") if item.is_file() and item.stat().st_size > 0]
    if not files:
        return ["required directory has no non-empty files: derivations"]
    for item in files:
        try:
            text = item.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"cannot inspect derivation file {item.name}: {exc}")
            continue
        if PLACEHOLDER_RE.search(text):
            errors.append(f"derivation file contains an unfilled placeholder: {item.name}")
    return errors


def validate_verification_report(
    path: Path,
    spec: dict[str, Any],
    policy: str,
    contract: dict[str, Any] | None,
) -> tuple[list[str], str | None]:
    errors: list[str] = []
    report = load_json(path, "verification_report.json", errors)
    if not isinstance(report, dict):
        if report is not None:
            errors.append("verification_report.json root must be an object")
        return errors, None

    required = {
        "schema_version",
        "model_status",
        "claim_ladder_rung",
        "overall_result",
        "gates",
        "blocking_findings",
        "applicability_limitations",
        "residual_risk",
    }
    missing = required - report.keys()
    extra = report.keys() - required
    if missing:
        errors.append(f"verification report missing keys: {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"verification report has unsupported keys: {', '.join(sorted(extra))}")
    if contains_placeholder(report):
        errors.append("verification_report.json contains an unfilled placeholder")

    if report.get("schema_version") not in set(spec["supported_verification_schema_versions"]):
        errors.append(f"verification report schema_version is unsupported: {report.get('schema_version')!r}")
    if report.get("model_status") not in set(spec["model_statuses"]):
        errors.append(f"verification report model_status is invalid: {report.get('model_status')!r}")
    rung = report.get("claim_ladder_rung")
    if not isinstance(rung, int) or isinstance(rung, bool) or not 1 <= rung <= 8:
        errors.append("verification report claim_ladder_rung must be an integer from 1 through 8")
    else:
        allowed_rungs = set(spec["model_status_rungs"].get(report.get("model_status"), []))
        if allowed_rungs and rung not in allowed_rungs:
            errors.append(
                f"model_status {report.get('model_status')!r} is inconsistent with claim_ladder_rung {rung}"
            )
    overall = report.get("overall_result")
    if overall not in set(spec["overall_results"]):
        errors.append(f"verification report overall_result is invalid: {overall!r}")
    if contract is not None:
        if report.get("model_status") != contract.get("model_status"):
            errors.append("verification report model_status does not match problem contract")
        if report.get("claim_ladder_rung") != contract.get("claim_ladder_rung"):
            errors.append("verification report claim_ladder_rung does not match problem contract")

    for key in ("applicability_limitations", "residual_risk"):
        value = report.get(key)
        if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"verification report {key} must be a list of non-empty strings")

    blocking_findings = report.get("blocking_findings")
    finding_fields = {"id", "gate_id", "finding", "severity", "required_action"}
    valid_findings: list[dict[str, Any]] = []
    finding_ids: set[str] = set()
    if not isinstance(blocking_findings, list):
        errors.append("verification report blocking_findings must be a list")
        blocking_findings = []
    for index, finding in enumerate(blocking_findings):
        checked_finding = validate_object_fields(
            finding, f"blocking_findings[{index}]", finding_fields, errors
        )
        if checked_finding is None:
            continue
        finding_id = finding.get("id")
        if not isinstance(finding_id, str) or not re.fullmatch(r"F[1-9][0-9]*", finding_id):
            errors.append(f"blocking_findings[{index}].id must match F<number>")
        elif finding_id in finding_ids:
            errors.append(f"duplicate blocking finding id: {finding_id}")
        else:
            finding_ids.add(finding_id)
        for field in ("gate_id", "finding", "required_action"):
            require_string(finding.get(field), f"blocking_findings[{index}].{field}", errors)
        if finding.get("severity") not in set(spec["blocking_severities"]):
            errors.append(
                f"blocking_findings[{index}].severity must be major or fatal"
            )
        valid_findings.append(finding)

    gates = report.get("gates")
    expected_ids = [gate["id"] for gate in spec["gates"]]
    observed_ids: list[str] = []
    failed_results: list[tuple[str, str]] = []
    unresolved_results: list[str] = []
    gate_outcomes: dict[str, tuple[str, str]] = {}
    if not isinstance(gates, list):
        errors.append("verification report gates must be a list")
        gates = []
    gate_fields = {"id", "check_performed", "evidence", "result", "severity", "required_action"}
    for index, gate in enumerate(gates):
        checked_gate = validate_object_fields(gate, f"gates[{index}]", gate_fields, errors)
        if checked_gate is None:
            continue
        gate_id = gate.get("id")
        observed_ids.append(gate_id if isinstance(gate_id, str) else "")
        require_string(gate.get("check_performed"), f"gates[{index}].check_performed", errors)
        require_string_list(gate.get("evidence"), f"gates[{index}].evidence", errors)
        result = gate.get("result")
        severity = gate.get("severity")
        if result not in set(spec["gate_results"]):
            errors.append(f"gates[{index}].result is invalid: {result!r}")
        if severity not in set(spec["severities"]):
            errors.append(f"gates[{index}].severity is invalid: {severity!r}")
        if isinstance(gate_id, str) and isinstance(result, str) and isinstance(severity, str):
            gate_outcomes[gate_id] = (result, severity)
        if result == "pass" and severity not in {"none", "minor"}:
            errors.append(f"gate {gate_id} cannot pass with severity {severity!r}")
        if result in {"not-applicable", "not-run", "blocked"} and severity != "none":
            errors.append(f"gate {gate_id} result {result!r} requires severity 'none'")
        if result == "fail":
            if severity == "none":
                errors.append(f"failed gate {gate_id} must declare a non-none severity")
            require_string(gate.get("required_action"), f"gates[{index}].required_action", errors)
            failed_results.append((str(gate_id), str(severity)))
        if result in {"not-run", "blocked"}:
            require_string(gate.get("required_action"), f"gates[{index}].required_action", errors)
            unresolved_results.append(str(gate_id))

    if observed_ids != expected_ids:
        errors.append(
            "verification gate registry mismatch; expected IDs in order: " + ", ".join(expected_ids)
        )

    if overall == "pass" and failed_results:
        errors.append("overall_result cannot be pass when any gate failed")
    if overall == "qualified-pass" and not failed_results:
        errors.append("overall_result qualified-pass requires at least one recorded failed gate")
    blocking_failures = [
        gate_id for gate_id, severity in failed_results if severity in set(spec["blocking_severities"])
    ]
    linked_blocking_gates: set[str] = set()
    for index, finding in enumerate(valid_findings):
        gate_id = finding.get("gate_id")
        if gate_id not in expected_ids:
            errors.append(f"blocking_findings[{index}].gate_id is not in the gate registry")
            continue
        linked_blocking_gates.add(str(gate_id))
        outcome = gate_outcomes.get(str(gate_id))
        if outcome is None or outcome[0] != "fail":
            errors.append(
                f"blocking finding {finding.get('id')} must link to a failed gate"
            )
        elif outcome[1] != finding.get("severity"):
            errors.append(
                f"blocking finding {finding.get('id')} severity does not match gate {gate_id}"
            )
    unlinked_blocking = sorted(set(blocking_failures) - linked_blocking_gates)
    if unlinked_blocking:
        errors.append(
            "major or fatal gate failures require linked blocking findings: "
            + ", ".join(unlinked_blocking)
        )
    if overall == "qualified-pass" and blocking_failures:
        errors.append("overall_result qualified-pass cannot contain a major or fatal failure")
    if overall in {"pass", "qualified-pass"} and valid_findings:
        errors.append("overall_result pass or qualified-pass cannot contain blocking findings")
    if overall in {"pass", "qualified-pass"} and unresolved_results:
        errors.append("overall_result pass or qualified-pass cannot contain not-run or blocked gates")
    if overall == "fail" and not failed_results:
        errors.append("overall_result fail requires at least one failed gate")
    if overall == "blocked" and not any(gate.get("result") == "blocked" for gate in gates if isinstance(gate, dict)):
        errors.append("overall_result blocked requires at least one blocked gate")
    if overall == "not-run" and not any(gate.get("result") == "not-run" for gate in gates if isinstance(gate, dict)):
        errors.append("overall_result not-run requires at least one not-run gate")

    if policy == "promotion":
        if unresolved_results:
            errors.append("promotion is blocked by unrun or blocked gates: " + ", ".join(unresolved_results))
        if blocking_failures:
            errors.append(
                "promotion is blocked by major or fatal gate findings: "
                + ", ".join(blocking_failures)
            )
        if valid_findings:
            errors.append("promotion is blocked by recorded blocking findings")
        if overall not in {"pass", "qualified-pass"}:
            errors.append("promotion requires overall_result pass or qualified-pass")
        if isinstance(rung, int) and rung < 6:
            errors.append("promotion requires claim_ladder_rung 6 or higher")
        if report.get("model_status") == "proposed":
            errors.append("promotion cannot retain model_status proposed")

    return errors, overall if isinstance(overall, str) else None


def validate_package(
    package: Path,
    profile: dict[str, Any],
    spec: dict[str, Any],
    schema: dict[str, Any],
) -> tuple[list[str], str | None]:
    errors: list[str] = []
    recorded_result: str | None = None
    contract: dict[str, Any] | None = None
    if not package.is_dir():
        return [f"package directory does not exist: {package}"], None

    for relative in profile["files"]:
        path = package / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"required file is empty: {relative}")

    for relative in profile["directories"]:
        path = package / relative
        if not path.is_dir():
            errors.append(f"missing required directory: {relative}")
        elif relative == "derivations":
            errors.extend(validate_derivations(path))

    contract_path = package / "problem_contract.json"
    if contract_path.is_file():
        contract_errors, contract = validate_contract(contract_path, spec, schema)
        errors.extend(contract_errors)
        ceiling = profile.get("claim_ceiling")
        if isinstance(ceiling, int) and contract is not None:
            rung = contract.get("claim_ladder_rung")
            if isinstance(rung, int) and rung > ceiling:
                errors.append(
                    f"claim_ladder_rung {rung} exceeds this mode's ceiling of {ceiling}"
                )

    requirements = spec.get("markdown_requirements", {})
    for relative in profile["files"]:
        if relative in requirements and (package / relative).is_file():
            errors.extend(validate_markdown(package / relative, requirements[relative]))

    report_path = package / "verification_report.json"
    if report_path.is_file() and "verification_report.json" in profile["files"]:
        report_errors, recorded_result = validate_verification_report(
            report_path,
            spec,
            profile.get("verification_policy", "not-required"),
            contract,
        )
        errors.extend(report_errors)

    return errors, recorded_result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="analysis-package directory")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--stage", choices=["contract", "theory", "verified"])
    group.add_argument("--mode", choices=["explore", "derive", "audit", "validate", "full"])
    args = parser.parse_args()

    try:
        spec, schema = load_configuration()
    except RuntimeError as exc:
        print(f"FAIL: validator configuration error: {exc}")
        return 2

    if args.mode:
        profile_kind = "mode"
        profile_name = args.mode
        profile = spec["modes"][args.mode]
    else:
        profile_kind = "stage"
        profile_name = args.stage or "contract"
        profile = spec["stages"][profile_name]

    package = args.package.resolve()
    errors, recorded_result = validate_package(package, profile, spec, schema)
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        print("No claim about scientific validity is made by this validator.")
        return 1

    print(f"PASS: package contract satisfied for {profile_kind} '{profile_name}' at {package}")
    if recorded_result is not None:
        print(f"RECORDED MODEL RESULT: {recorded_result}")
    print("This validates package structure and recorded evidence fields, not scientific truth.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
