#!/usr/bin/env python3
"""Run repository-level structural checks for the analytical skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
LEGACY_ASSETS = {
    "problem-contract.json",
    "balance-audit.md",
    "assumption-ledger.md",
    "evidence-map.md",
    "resource-register.md",
    "hypothesis-matrix.md",
    "model-card.md",
    "verification-report.md",
    "benchmark-register.md",
    "validation-summary.md",
    "experiment-plan.md",
}


def main() -> int:
    errors: list[str] = []
    skill_path = ROOT / "SKILL.md"
    skill_text = skill_path.read_text(encoding="utf-8")
    lines = skill_text.splitlines()
    if len(lines) >= 500:
        errors.append(f"SKILL.md has {len(lines)} lines; keep it below 500")
    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill_text, flags=re.DOTALL)
    if not frontmatter:
        errors.append("SKILL.md lacks valid YAML frontmatter delimiters")
    else:
        metadata = frontmatter.group(1)
        if not re.search(r"^name:\s*analytical\s*$", metadata, flags=re.MULTILINE):
            errors.append("SKILL.md frontmatter name must be analytical")
        if not re.search(r"^description:\s*\S", metadata, flags=re.MULTILINE):
            errors.append("SKILL.md frontmatter requires a non-empty description")

    for markdown in [skill_path, *sorted((ROOT / "references").glob("*.md"))]:
        text = markdown.read_text(encoding="utf-8")
        if markdown.parent.name == "references" and len(text.splitlines()) > 100 and "## Contents" not in text:
            errors.append(f"reference longer than 100 lines lacks Contents: {markdown.relative_to(ROOT)}")
        for target in LINK_RE.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative_target = unquote(target.split("#", 1)[0])
            if relative_target and not (markdown.parent / relative_target).resolve().exists():
                errors.append(
                    f"broken internal link in {markdown.relative_to(ROOT)}: {target}"
                )

    spec = json.loads((ROOT / "scripts" / "package_spec.json").read_text(encoding="utf-8"))
    required_assets = {
        relative
        for collection in (spec["stages"], spec["modes"])
        for profile in collection.values()
        for relative in profile["files"]
    }
    for relative in sorted(required_assets):
        if not (ROOT / "assets" / relative).is_file():
            errors.append(f"missing scaffold asset declared by package spec: {relative}")
    for legacy in sorted(LEGACY_ASSETS):
        if (ROOT / "assets" / legacy).exists():
            errors.append(f"legacy hyphenated asset remains: {legacy}")

    evaluation = json.loads((ROOT / "tests" / "evaluation_cases.json").read_text(encoding="utf-8"))
    if evaluation.get("schema_version") != "1.0":
        errors.append("evaluation case schema_version must be 1.0")
    dimensions = evaluation.get("scoring_dimensions")
    if not isinstance(dimensions, list) or len(dimensions) != len(set(dimensions)) or not dimensions:
        errors.append("evaluation scoring_dimensions must be a non-empty unique list")
    cases = evaluation.get("cases")
    if not isinstance(cases, list) or len(cases) < 12:
        errors.append("evaluation manifest must contain at least 12 cases")
    else:
        case_ids: set[str] = set()
        required_case_fields = {
            "id", "domain", "mode", "prompt", "required_invariants", "seeded_risks", "maximum_claim_rung"
        }
        for index, case in enumerate(cases):
            if not isinstance(case, dict):
                errors.append(f"evaluation case {index} must be an object")
                continue
            missing = required_case_fields - case.keys()
            if missing:
                errors.append(f"evaluation case {index} missing fields: {', '.join(sorted(missing))}")
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id:
                errors.append(f"evaluation case {index} requires a non-empty id")
            elif case_id in case_ids:
                errors.append(f"duplicate evaluation case id: {case_id}")
            else:
                case_ids.add(case_id)
            if case.get("mode") not in spec["modes"]:
                errors.append(f"evaluation case {case_id} has invalid mode: {case.get('mode')!r}")
            if not isinstance(case.get("required_invariants"), list) or not case.get("required_invariants"):
                errors.append(f"evaluation case {case_id} requires physical invariants")
            rung = case.get("maximum_claim_rung")
            if not isinstance(rung, int) or isinstance(rung, bool) or not 1 <= rung <= 8:
                errors.append(f"evaluation case {case_id} has invalid maximum_claim_rung")

    agent_text = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "$analytical" not in agent_text:
        errors.append("agents/openai.yaml default_prompt must mention $analytical")
    short_match = re.search(r'^\s*short_description:\s*"([^"]+)"', agent_text, flags=re.MULTILINE)
    if not short_match or not 25 <= len(short_match.group(1)) <= 64:
        errors.append("agents/openai.yaml short_description must contain 25-64 characters")

    for forbidden in ("README.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md", "CHANGELOG.md"):
        if (ROOT / forbidden).exists():
            errors.append(f"skill package contains extraneous root document: {forbidden}")

    if errors:
        print(f"FAIL: {len(errors)} skill issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: analytical skill structure and internal links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
