#!/usr/bin/env python3
"""Check the public-resource registry for schema, staleness, and optional URL reachability."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


DEFAULT_REGISTRY = Path(__file__).resolve().parents[1] / "references" / "public-resource-registry.json"
ACCESS_STATES = {
    "open-full-text",
    "open-data",
    "open-code",
    "metadata-only",
    "registration",
    "restricted",
    "unverified",
}
REQUIRED_FIELDS = {
    "id",
    "title",
    "stable_url",
    "persistent_id",
    "source_type",
    "access_state",
    "domain",
    "exact_use",
    "evidence_limit",
    "license_or_reuse",
    "last_checked",
}


def check_online(url: str, timeout: float) -> str | None:
    request = Request(url, headers={"User-Agent": "analytical-skill-resource-check/1.0"}, method="HEAD")
    try:
        with urlopen(request, timeout=timeout) as response:
            if response.status >= 400:
                return f"HTTP {response.status}"
    except HTTPError as exc:
        if exc.code not in {403, 405}:
            return f"HTTP {exc.code}"
        fallback = Request(url, headers={"User-Agent": "analytical-skill-resource-check/1.0"})
        try:
            with urlopen(fallback, timeout=timeout) as response:
                if response.status >= 400:
                    return f"HTTP {response.status}"
        except (HTTPError, URLError, TimeoutError) as fallback_exc:
            return str(fallback_exc)
    except (URLError, TimeoutError) as exc:
        return str(exc)
    return None


def validate_registry(
    registry: dict[str, Any], *, max_age_days: int, online: bool, timeout: float
) -> list[str]:
    errors: list[str] = []
    if registry.get("schema_version") != "1.0":
        errors.append("registry schema_version must be '1.0'")
    resources = registry.get("resources")
    if not isinstance(resources, list) or not resources:
        return errors + ["registry resources must be a non-empty list"]

    ids: set[str] = set()
    today = date.today()
    for index, resource in enumerate(resources):
        label = f"resources[{index}]"
        if not isinstance(resource, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = REQUIRED_FIELDS - resource.keys()
        extra = resource.keys() - REQUIRED_FIELDS
        if missing:
            errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{label} has unsupported fields: {', '.join(sorted(extra))}")
        for field in REQUIRED_FIELDS & resource.keys():
            if not isinstance(resource[field], str) or not resource[field].strip():
                errors.append(f"{label}.{field} must be a non-empty string")

        resource_id = resource.get("id")
        if isinstance(resource_id, str):
            if resource_id in ids:
                errors.append(f"duplicate resource id: {resource_id}")
            ids.add(resource_id)

        access_state = resource.get("access_state")
        if access_state not in ACCESS_STATES:
            errors.append(f"{label}.access_state is invalid: {access_state!r}")

        url = resource.get("stable_url")
        if isinstance(url, str):
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{label}.stable_url must be an absolute HTTPS URL")
            elif online:
                online_error = check_online(url, timeout)
                if online_error:
                    errors.append(f"{label}.stable_url is not reachable: {online_error}")

        checked = resource.get("last_checked")
        if isinstance(checked, str):
            try:
                checked_date = date.fromisoformat(checked)
            except ValueError:
                errors.append(f"{label}.last_checked must use YYYY-MM-DD")
            else:
                age = (today - checked_date).days
                if age < 0:
                    errors.append(f"{label}.last_checked is in the future")
                elif age > max_age_days:
                    errors.append(f"{label} is stale: last checked {age} days ago")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--max-age-days", type=int, default=365)
    parser.add_argument("--online", action="store_true", help="also request every URL")
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args()

    try:
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read registry: {exc}")
        return 2
    if not isinstance(registry, dict):
        print("FAIL: registry root must be an object")
        return 2

    errors = validate_registry(
        registry,
        max_age_days=args.max_age_days,
        online=args.online,
        timeout=args.timeout,
    )
    if errors:
        print(f"FAIL: {len(errors)} resource issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(registry['resources'])} resource records checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
