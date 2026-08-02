from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INIT = ROOT / "scripts" / "init_package.py"
VALIDATE = ROOT / "scripts" / "validate_package.py"
CHECK_RESOURCES = ROOT / "scripts" / "check_resources.py"


def replace_placeholders(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("REPLACE_ME", "documented value")
    if isinstance(value, list):
        return [replace_placeholders(item) for item in value]
    if isinstance(value, dict):
        return {key: replace_placeholders(item) for key, item in value.items()}
    return value


class PackageToolsTests(unittest.TestCase):
    def run_tool(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def scaffold(self, directory: Path, mode: str = "full") -> None:
        result = self.run_tool(str(INIT), str(directory), "--mode", mode)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def fill_full_package(self, directory: Path) -> None:
        contract_path = directory / "problem_contract.json"
        contract = replace_placeholders(json.loads(contract_path.read_text(encoding="utf-8")))
        contract["model_status"] = "internally-verified"
        contract["claim_ladder_rung"] = 6
        contract_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")

        for path in directory.rglob("*.md"):
            path.write_text(
                path.read_text(encoding="utf-8").replace("REPLACE_ME", "documented value"),
                encoding="utf-8",
            )

        report_path = directory / "verification_report.json"
        report = replace_placeholders(json.loads(report_path.read_text(encoding="utf-8")))
        report["model_status"] = "internally-verified"
        report["claim_ladder_rung"] = 6
        report["overall_result"] = "pass"
        report["blocking_findings"] = []
        report["applicability_limitations"] = ["documented limit"]
        report["residual_risk"] = ["documented residual risk"]
        for gate in report["gates"]:
            gate["result"] = "pass"
            gate["severity"] = "none"
            gate["required_action"] = "none"
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    def test_scaffold_uses_validator_filenames(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.assertTrue((package / "problem_contract.json").is_file())
            self.assertTrue((package / "verification_report.json").is_file())
            self.assertFalse((package / "problem-contract.json").exists())
            self.assertTrue((package / "derivations" / "derivation.md").is_file())

    def test_every_declared_profile_has_complete_scaffold_assets(self) -> None:
        for option, names in (
            ("--stage", ("contract", "theory", "verified")),
            ("--mode", ("explore", "derive", "audit", "validate", "full")),
        ):
            for name in names:
                with self.subTest(option=option, name=name), tempfile.TemporaryDirectory() as temporary:
                    package = Path(temporary) / "package"
                    created = self.run_tool(str(INIT), str(package), option, name)
                    self.assertEqual(created.returncode, 0, created.stdout + created.stderr)
                    checked = self.run_tool(str(VALIDATE), str(package), option, name)
                    self.assertEqual(checked.returncode, 1)
                    self.assertNotIn("missing required file", checked.stdout)
                    self.assertNotIn("missing required directory", checked.stdout)

    def test_unfilled_scaffold_fails_truthfully(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "explore")
            result = self.run_tool(str(VALIDATE), str(package), "--mode", "explore")
            self.assertEqual(result.returncode, 1)
            self.assertIn("unfilled placeholder", result.stdout)
            self.assertIn("No claim about scientific validity", result.stdout)

    def test_completed_full_package_satisfies_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.fill_full_package(package)
            result = self.run_tool(str(VALIDATE), str(package), "--mode", "full")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("package contract satisfied", result.stdout)
            self.assertIn("not scientific truth", result.stdout)

    def test_major_gate_blocks_promotion_but_is_valid_audit_record(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.fill_full_package(package)
            report_path = package / "verification_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["overall_result"] = "fail"
            report["gates"][1]["result"] = "fail"
            report["gates"][1]["severity"] = "major"
            report["gates"][1]["required_action"] = "repair the conservation defect"
            report["blocking_findings"] = [
                {
                    "id": "F1",
                    "gate_id": report["gates"][1]["id"],
                    "finding": "conservation defect",
                    "severity": "major",
                    "required_action": "repair the conservation defect",
                }
            ]
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

            promoted = self.run_tool(str(VALIDATE), str(package), "--stage", "verified")
            self.assertEqual(promoted.returncode, 1)
            self.assertIn("blocked by major or fatal", promoted.stdout)

            audited = self.run_tool(str(VALIDATE), str(package), "--mode", "audit")
            self.assertEqual(audited.returncode, 0, audited.stdout + audited.stderr)
            self.assertIn("RECORDED MODEL RESULT: fail", audited.stdout)

    def test_gate_registry_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.fill_full_package(package)
            report_path = package / "verification_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["gates"].pop()
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            result = self.run_tool(str(VALIDATE), str(package), "--stage", "verified")
            self.assertEqual(result.returncode, 1)
            self.assertIn("gate registry mismatch", result.stdout)

    def test_pass_without_evidence_and_status_overclaim_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.fill_full_package(package)
            report_path = package / "verification_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["gates"][0]["evidence"] = []
            report["model_status"] = "independently-validated"
            report["claim_ladder_rung"] = 6
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            result = self.run_tool(str(VALIDATE), str(package), "--stage", "verified")
            self.assertEqual(result.returncode, 1)
            self.assertIn("evidence must be a non-empty list", result.stdout)
            self.assertIn("inconsistent with claim_ladder_rung", result.stdout)

    def test_result_severity_and_unrun_overclaim_are_rejected_in_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.fill_full_package(package)
            report_path = package / "verification_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["gates"][0]["result"] = "not-applicable"
            report["gates"][0]["severity"] = "fatal"
            report["gates"][1]["result"] = "not-run"
            report["gates"][1]["severity"] = "none"
            report["overall_result"] = "pass"
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            result = self.run_tool(str(VALIDATE), str(package), "--mode", "audit")
            self.assertEqual(result.returncode, 1)
            self.assertIn("requires severity 'none'", result.stdout)
            self.assertIn("cannot contain not-run or blocked", result.stdout)

    def test_mode_claim_ceiling_is_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "explore")
            contract_path = package / "problem_contract.json"
            contract = replace_placeholders(json.loads(contract_path.read_text(encoding="utf-8")))
            contract["model_status"] = "derived"
            contract["claim_ladder_rung"] = 4
            contract_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")
            for path in package.glob("*.md"):
                path.write_text(
                    path.read_text(encoding="utf-8").replace("REPLACE_ME", "documented value"),
                    encoding="utf-8",
                )
            result = self.run_tool(str(VALIDATE), str(package), "--mode", "explore")
            self.assertEqual(result.returncode, 1)
            self.assertIn("exceeds this mode's ceiling", result.stdout)

    def test_empty_experiment_table_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.fill_full_package(package)
            experiment = package / "experiment_plan.md"
            lines = [line for line in experiment.read_text(encoding="utf-8").splitlines() if not line.startswith("| 1 |")]
            experiment.write_text("\n".join(lines) + "\n", encoding="utf-8")
            result = self.run_tool(str(VALIDATE), str(package), "--mode", "full")
            self.assertEqual(result.returncode, 1)
            self.assertIn("requires at least 1 substantive row", result.stdout)

    def test_short_markdown_table_row_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.fill_full_package(package)
            ledger = package / "assumption_ledger.md"
            lines = ledger.read_text(encoding="utf-8").splitlines()
            lines = ["| A1 | documented |" if line.startswith("| A1 |") else line for line in lines]
            ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
            result = self.run_tool(str(VALIDATE), str(package), "--mode", "full")
            self.assertEqual(result.returncode, 1)
            self.assertIn("columns; expected", result.stdout)

    def test_blocking_finding_must_match_failed_gate_and_blocks_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "full")
            self.fill_full_package(package)
            report_path = package / "verification_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["blocking_findings"] = [
                {
                    "id": "F1",
                    "gate_id": report["gates"][0]["id"],
                    "finding": "unsupported blocking claim",
                    "severity": "major",
                    "required_action": "resolve it",
                }
            ]
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            result = self.run_tool(str(VALIDATE), str(package), "--mode", "audit")
            self.assertEqual(result.returncode, 1)
            self.assertIn("must link to a failed gate", result.stdout)
            self.assertIn("cannot contain blocking findings", result.stdout)

    def test_schema_version_and_variable_fields_are_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            self.scaffold(package, "explore")
            contract_path = package / "problem_contract.json"
            contract = replace_placeholders(json.loads(contract_path.read_text(encoding="utf-8")))
            contract["schema_version"] = "1.1"
            contract["title"] = 42
            del contract["dependent_variables"][0]["sign_convention"]
            contract_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")
            for path in package.glob("*.md"):
                path.write_text(
                    path.read_text(encoding="utf-8").replace("REPLACE_ME", "documented value"),
                    encoding="utf-8",
                )
            result = self.run_tool(str(VALIDATE), str(package), "--mode", "explore")
            self.assertEqual(result.returncode, 1)
            self.assertIn("schema_version is unsupported", result.stdout)
            self.assertIn("title must be a non-empty string", result.stdout)
            self.assertIn("missing keys: sign_convention", result.stdout)

    def test_public_resource_registry_contract(self) -> None:
        result = self.run_tool(str(CHECK_RESOURCES), "--max-age-days", "365")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("resource records checked", result.stdout)

    def test_invalid_resource_registry_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "resources.json"
            path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "resources": [
                            {
                                "id": "R1",
                                "title": "Example",
                                "stable_url": "http://example.com",
                                "persistent_id": "example",
                                "source_type": "metadata",
                                "access_state": "invalid",
                                "domain": "test",
                                "exact_use": "test",
                                "evidence_limit": "test",
                                "license_or_reuse": "test",
                                "last_checked": "not-a-date",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            result = self.run_tool(str(CHECK_RESOURCES), str(path))
            self.assertEqual(result.returncode, 1)
            self.assertIn("absolute HTTPS URL", result.stdout)
            self.assertIn("access_state is invalid", result.stdout)
            self.assertIn("must use YYYY-MM-DD", result.stdout)


if __name__ == "__main__":
    unittest.main()
