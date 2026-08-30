#!/usr/bin/env python3
"""Validate a portable presentation scenario Skill package."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_EVAL_CATEGORIES = {
    "normal",
    "boundary",
    "negative-trigger",
    "brand-constraint",
    "information-overload",
}


def main() -> int:
    errors: list[str] = []
    scenario = yaml.safe_load((ROOT / "references" / "scenario.yaml").read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "schemas" / "scenario.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    for error in Draft202012Validator(schema).iter_errors(scenario):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"scenario.yaml:{location}: {error.message}")

    evals = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
    if evals.get("skill_name") != ROOT.name:
        errors.append("evals.json skill_name must match the Skill directory")
    cases = evals.get("evals")
    if not isinstance(cases, list):
        errors.append("evals.json evals must be a list")
        cases = []
    categories = {case.get("category") for case in cases if isinstance(case, dict)}
    missing = sorted(REQUIRED_EVAL_CATEGORIES - categories)
    if missing:
        errors.append("evals.json missing categories: " + ", ".join(missing))

    for relative in ("references/expert-patterns.md", "references/slide-grammar.md"):
        if not (ROOT / relative).is_file():
            errors.append(f"missing {relative}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"valid: {ROOT.name} ({len(cases)} evals)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

