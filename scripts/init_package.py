#!/usr/bin/env python3
"""Create an analytical-package scaffold for a declared workflow mode or stage."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ASSET_DIR = SKILL_DIR / "assets"
SPEC_PATH = SCRIPT_DIR / "package_spec.json"


def load_spec() -> dict[str, Any]:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="new package directory")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--stage", choices=["contract", "theory", "verified"])
    group.add_argument("--mode", choices=["explore", "derive", "audit", "validate", "full"])
    args = parser.parse_args()

    spec = load_spec()
    if args.stage:
        profile_kind = "stage"
        profile_name = args.stage
        profile = spec["stages"][profile_name]
    else:
        profile_kind = "mode"
        profile_name = args.mode or "explore"
        profile = spec["modes"][profile_name]

    destination = args.destination.resolve()
    if destination.exists() and not destination.is_dir():
        print(f"FAIL: destination exists and is not a directory: {destination}")
        return 1
    if destination.exists() and any(destination.iterdir()):
        print(f"FAIL: destination exists and is not empty: {destination}")
        return 1
    destination.mkdir(parents=True, exist_ok=True)

    missing_assets: list[str] = []
    for relative in profile["files"]:
        source = ASSET_DIR / relative
        if not source.is_file():
            missing_assets.append(relative)
            continue
        shutil.copy2(source, destination / relative)

    for relative in profile["directories"]:
        target = destination / relative
        target.mkdir(parents=True, exist_ok=True)
        if relative == "derivations":
            source = ASSET_DIR / "derivation.md"
            if source.is_file():
                shutil.copy2(source, target / "derivation.md")
            else:
                missing_assets.append("derivation.md")

    if missing_assets:
        print("FAIL: missing scaffold assets: " + ", ".join(sorted(missing_assets)))
        return 2

    print(f"CREATED: {profile_kind} '{profile_name}' package at {destination}")
    print("Fill every placeholder before running validate_package.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
