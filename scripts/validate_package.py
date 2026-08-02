#!/usr/bin/env python3
"""Validate the minimum structure and problem contract of an analytical package."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


EVIDENCE_STATES = {
    "measured",
    "reported",
    "simulated",
    "derived",
    "assumed",
    "inferred",
    "illustrative",
    "screening-level",
    "proposed",
    "independently-validated",
    "unknown",
}

STAGE_FILES = {
    "contract": {"problem_contract.json"},
    "theory": {
        "problem_contract.json",
        "evidence_map.md",
        "hypothesis_matrix.md",
        "model_card.md",
    },
    "verified": {
        "problem_contract.json",
        "evidence_map.md",
        "hypothesis_matrix.md",
        "model_card.md",
        "verification_report.md",
        "validation_summary.md",
        "experiment_plan.md",
    },
}

STAGE_DIRECTORIES = {
    "contract": set(),
    "theory": {"derivations"},
    "verified": {"derivations"},
}

REQUIRED_CONTRACT_KEYS = {
    "schema_version",
    "title",
    "decision_or_claim",
    "evidence_state",
    "event_definition",
    "system_boundary",
    "regime",
    "geometry_and_frame",
    "materials_or_fluids",
    "operating_conditions",
    "initial_conditions",
    "boundary_conditions",
    "dependent_variables",
    "governing_variables",
    "assumptions",
    "exclusions",
    "baselines",
    "calibration_boundary",
    "acceptance_criteria",
    "falsification_cases",
    "uncertainty_plan",
    "provenance",
}


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def contains_placeholder(value: Any) -> bool:
    if isinstance(value, str):
        upper = value.upper()
        return "REPLACE_ME" in upper or "TODO" in upper or "TBD" in upper
    if isinstance(value, list):
        return any(contains_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(contains_placeholder(item) for item in value.values())
    return False


def validate_variable_group(
    contract: dict[str, Any], key: str, required: set[str], errors: list[str]
) -> None:
    variables = contract.get(key)
    if not isinstance(variables, list) or not variables:
        errors.append(f"{key} must be a non-empty list")
        return
    for index, variable in enumerate(variables):
        label = f"{key}[{index}]"
        if not isinstance(variable, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = required - variable.keys()
        if missing:
            errors.append(f"{label} missing keys: {', '.join(sorted(missing))}")
        for field in required & variable.keys():
            if is_empty(variable[field]):
                errors.append(f"{label}.{field} must not be empty")
        state = variable.get("evidence_state")
        if state not in EVIDENCE_STATES:
            errors.append(f"{label}.evidence_state is invalid: {state!r}")


def validate_contract(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        contract = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"problem_contract.json is not valid JSON: {exc}"]
    except OSError as exc:
        return [f"cannot read problem_contract.json: {exc}"]

    if not isinstance(contract, dict):
        return ["problem_contract.json root must be an object"]

    missing = REQUIRED_CONTRACT_KEYS - contract.keys()
    if missing:
        errors.append(f"problem contract missing keys: {', '.join(sorted(missing))}")

    for key in REQUIRED_CONTRACT_KEYS & contract.keys():
        if is_empty(contract[key]):
            errors.append(f"problem contract field {key!r} must not be empty")

    state = contract.get("evidence_state")
    if state not in EVIDENCE_STATES:
        errors.append(f"problem contract evidence_state is invalid: {state!r}")

    validate_variable_group(
        contract,
        "dependent_variables",
        {"name", "symbol", "unit", "definition", "evidence_state"},
        errors,
    )
    validate_variable_group(
        contract,
        "governing_variables",
        {"name", "symbol", "unit", "role", "property_state", "evidence_state"},
        errors,
    )

    if contains_placeholder(contract):
        errors.append("problem contract contains an unfilled placeholder")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="analysis-package directory")
    parser.add_argument(
        "--stage", choices=sorted(STAGE_FILES), default="contract", help="validation stage"
    )
    args = parser.parse_args()

    package = args.package.resolve()
    errors: list[str] = []
    if not package.is_dir():
        errors.append(f"package directory does not exist: {package}")
    else:
        for relative in sorted(STAGE_FILES[args.stage]):
            path = package / relative
            if not path.is_file():
                errors.append(f"missing required file for {args.stage} stage: {relative}")
            elif path.stat().st_size == 0:
                errors.append(f"required file is empty: {relative}")

        for relative in sorted(STAGE_DIRECTORIES[args.stage]):
            path = package / relative
            if not path.is_dir():
                errors.append(f"missing required directory for {args.stage} stage: {relative}")
            elif not any(item.is_file() and item.stat().st_size > 0 for item in path.rglob("*")):
                errors.append(f"required directory has no non-empty files: {relative}")

        if args.stage == "verified":
            report = package / "verification_report.md"
            if report.is_file() and "not-run" in report.read_text(encoding="utf-8").lower():
                errors.append("verification_report.md still contains a not-run gate")

        contract_path = package / "problem_contract.json"
        if contract_path.is_file():
            errors.extend(validate_contract(contract_path))

    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {args.stage} package at {package}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
