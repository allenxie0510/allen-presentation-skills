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

    pptx_profile_schema = json.loads(
        (ROOT / "schemas" / "native-pptx-profile.schema.json").read_text(encoding="utf-8")
    )
    pptx_profile = yaml.safe_load(
        (ROOT / "fixtures" / "native-pptx-profiles" / "learning-agent.yaml").read_text(encoding="utf-8")
    )
    Draft202012Validator.check_schema(pptx_profile_schema)
    for error in Draft202012Validator(pptx_profile_schema).iter_errors(pptx_profile):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"native-pptx-profile:{location}: {error.message}")
    profile_meta = pptx_profile.get("meta", {})
    if profile_meta.get("status") == "approved" and (
        not profile_meta.get("reviewed_by") or not profile_meta.get("reviewed_at")
    ):
        errors.append(
            "native-pptx-profile: approved profiles require reviewed_by and reviewed_at"
        )

    review_schema = json.loads(
        (ROOT / "schemas" / "design-review.schema.json").read_text(encoding="utf-8")
    )
    Draft202012Validator.check_schema(review_schema)
    for path in sorted((ROOT / "fixtures" / "design-reviews").glob("*.yaml")):
        review = yaml.safe_load(path.read_text(encoding="utf-8"))
        for error in Draft202012Validator(review_schema).iter_errors(review):
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            errors.append(f"{path.name}:{location}: {error.message}")
        dimensions = review.get("dimensions", {}) if isinstance(review, dict) else {}
        weighted = sum(
            item.get("score", 0) * item.get("weight", 0)
            for item in dimensions.values()
            if isinstance(item, dict)
        ) / 10
        if abs(weighted - review.get("weighted_score", -1)) > 0.11:
            errors.append(
                f"{path.name}:weighted_score: expected {weighted:.1f}, "
                f"got {review.get('weighted_score')}"
            )

    example_files = (
        "assets/examples/opc-system-thinking-0.5.1/README.md",
        "assets/examples/opc-system-thinking-0.5.1/SOURCES.md",
        "assets/examples/opc-system-thinking-0.5.1/PROMPTS.md",
        "assets/examples/opc-system-thinking-0.5.1/opc-system-thinking-0.5.1.pptx",
        "assets/examples/opc-system-thinking-0.5.1/previews/contact-sheet.png",
        "references/native-pptx-generation.md",
    )
    for relative in example_files:
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
