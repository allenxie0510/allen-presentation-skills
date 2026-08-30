#!/usr/bin/env python3
"""Validate presentation-core schemas, fixtures, and cross-file invariants."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
    from referencing import Registry, Resource
except ModuleNotFoundError as exc:
    print(
        "Missing validation dependency. Install scripts/requirements.txt "
        f"before running this validator ({exc.name}).",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


SKILL_DIR = Path(__file__).resolve().parents[1]
SCHEMA_DIR = SKILL_DIR / "schemas"
FIXTURE_DIR = SKILL_DIR / "fixtures"

SCHEMA_FILES = {
    "presentation-ir": SCHEMA_DIR / "presentation-ir.schema.json",
    "design-system": SCHEMA_DIR / "design-system.schema.json",
    "editor-permissions": SCHEMA_DIR / "editor-permissions.schema.json",
    "scenario": SCHEMA_DIR / "scenario.schema.json",
    "theme": SCHEMA_DIR / "theme.schema.json",
}


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def relative(path: Path) -> str:
    return str(path.relative_to(SKILL_DIR))


def format_json_path(parts: Iterable[Any]) -> str:
    rendered = "$"
    for part in parts:
        rendered += f"[{part}]" if isinstance(part, int) else f".{part}"
    return rendered


def schema_registry(schemas: dict[str, dict[str, Any]]) -> Registry:
    resources = []
    for name, schema in schemas.items():
        schema_id = schema.get("$id")
        if not isinstance(schema_id, str) or not schema_id:
            raise ValueError(f"schema {name} must define a non-empty $id")
        resources.append((schema_id, Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def validate_instance(
    path: Path,
    instance: dict[str, Any],
    schema: dict[str, Any],
    registry: Registry,
) -> list[ValidationIssue]:
    validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
    issues = []
    for error in sorted(
        validator.iter_errors(instance),
        key=lambda item: tuple(str(part) for part in item.absolute_path),
    ):
        issues.append(
            ValidationIssue(
                f"{relative(path)}:{format_json_path(error.absolute_path)}",
                error.message,
            )
        )
    return issues


def duplicate_values(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def validate_ir_semantics(
    path: Path,
    ir: dict[str, Any],
    scenarios: dict[str, dict[str, Any]],
    design_systems: dict[str, dict[str, Any]],
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    slides = ir.get("slides", [])
    slide_ids = [slide.get("id") for slide in slides if isinstance(slide.get("id"), str)]
    for duplicate in sorted(duplicate_values(slide_ids)):
        issues.append(ValidationIssue(relative(path), f"duplicate slide id: {duplicate}"))

    scenario_id = ir.get("deck", {}).get("scenario", {}).get("id")
    if scenario_id not in scenarios:
        issues.append(ValidationIssue(relative(path), f"unknown scenario id: {scenario_id}"))

    design_ref = ir.get("deck", {}).get("design_system", {})
    design_id = design_ref.get("id")
    design = design_systems.get(design_id)
    if design is None:
        issues.append(ValidationIssue(relative(path), f"unknown design-system id: {design_id}"))

    object_ids: list[str] = []
    for slide_index, slide in enumerate(slides):
        slide_objects = slide.get("objects", [])
        local_ids = {
            obj.get("id") for obj in slide_objects if isinstance(obj.get("id"), str)
        }
        if design is not None:
            archetype_name = slide.get("archetype")
            archetype = design.get("archetypes", {}).get(archetype_name)
            if archetype is None:
                issues.append(
                    ValidationIssue(
                        f"{relative(path)}:$.slides[{slide_index}].archetype",
                        f"design system {design_id} does not define archetype {archetype_name}",
                    )
                )
            elif slide.get("layout_variant") not in archetype.get("variants", []):
                issues.append(
                    ValidationIssue(
                        f"{relative(path)}:$.slides[{slide_index}].layout_variant",
                        f"variant {slide.get('layout_variant')} is not allowed by archetype {archetype_name}",
                    )
                )

        for object_index, obj in enumerate(slide_objects):
            object_id = obj.get("id")
            if isinstance(object_id, str):
                object_ids.append(object_id)
            frame = obj.get("frame", {})
            x, y, width, height = (
                frame.get("x"),
                frame.get("y"),
                frame.get("w"),
                frame.get("h"),
            )
            if all(isinstance(value, (int, float)) for value in (x, y, width, height)):
                if x + width > 1920 or y + height > 1080:
                    issues.append(
                        ValidationIssue(
                            f"{relative(path)}:$.slides[{slide_index}].objects[{object_index}].frame",
                            "object frame exceeds the 1920×1080 authoring stage",
                        )
                    )
            for child in obj.get("children", []):
                if child not in local_ids:
                    issues.append(
                        ValidationIssue(
                            f"{relative(path)}:$.slides[{slide_index}].objects[{object_index}].children",
                            f"unknown child object id: {child}",
                        )
                    )

    for duplicate in sorted(duplicate_values(object_ids)):
        issues.append(ValidationIssue(relative(path), f"duplicate object id: {duplicate}"))
    return issues


def validate_design_semantics(path: Path, design: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    ratio = design.get("visual_dna", {}).get("color_behavior", {}).get("approximate_ratio", {})
    values = [ratio.get(key) for key in ("background", "neutral", "accent")]
    if all(isinstance(value, (int, float)) for value in values) and abs(sum(values) - 1) > 0.02:
        issues.append(ValidationIssue(relative(path), "color approximate_ratio must sum to approximately 1"))

    meta = design.get("meta", {})
    if meta.get("status") == "approved" and (not meta.get("reviewed_by") or not meta.get("reviewed_at")):
        issues.append(
            ValidationIssue(relative(path), "approved design systems require reviewed_by and reviewed_at")
        )
    return issues


def validate_permission_semantics(path: Path, model: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    profiles = model.get("profiles", {})
    locked = profiles.get("locked", {})
    if any(locked.get(key) for key in ("content", "image_replace", "data", "position", "resize", "delete")):
        issues.append(ValidationIssue(relative(path), "locked profile must not allow mutations"))
    content_only = profiles.get("content-only", {})
    if any(content_only.get(key) for key in ("position", "resize", "delete")):
        issues.append(ValidationIssue(relative(path), "content-only profile must preserve layout"))
    freeform = profiles.get("freeform", {})
    if not all(freeform.get(key) for key in ("content", "position", "resize", "delete")):
        issues.append(ValidationIssue(relative(path), "freeform profile must allow core object edits"))
    if freeform.get("unlock_required"):
        issues.append(ValidationIssue(relative(path), "freeform profile represents an already unlocked object"))
    return issues


def validate_theme_semantics(path: Path, theme: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    theme_id = theme.get("meta", {}).get("id")
    if theme_id != path.parent.name:
        issues.append(ValidationIssue(relative(path), "theme id must match its directory name"))
    stylesheet = theme.get("stylesheet")
    if isinstance(stylesheet, str) and not (path.parent / stylesheet).is_file():
        issues.append(ValidationIssue(relative(path), f"missing theme stylesheet: {stylesheet}"))
    return issues


def run_validation() -> tuple[list[ValidationIssue], dict[str, int]]:
    schemas = {name: load_json(path) for name, path in SCHEMA_FILES.items()}
    issues: list[ValidationIssue] = []
    for name, schema in schemas.items():
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # jsonschema exposes several schema-error subclasses.
            issues.append(ValidationIssue(relative(SCHEMA_FILES[name]), f"invalid schema: {exc}"))

    registry = schema_registry(schemas)
    scenarios: dict[str, dict[str, Any]] = {}
    scenario_files = sorted((FIXTURE_DIR / "scenarios").glob("*.yaml"))
    for path in scenario_files:
        fixture = load_yaml(path)
        issues.extend(validate_instance(path, fixture, schemas["scenario"], registry))
        scenario_id = fixture.get("scenario", {}).get("id")
        if isinstance(scenario_id, str):
            scenarios[scenario_id] = fixture
        if scenario_id != path.stem:
            issues.append(ValidationIssue(relative(path), "scenario id must match the fixture filename"))

    design_systems: dict[str, dict[str, Any]] = {}
    design_files = sorted((FIXTURE_DIR / "design-systems").glob("*.yaml"))
    for path in design_files:
        fixture = load_yaml(path)
        issues.extend(validate_instance(path, fixture, schemas["design-system"], registry))
        issues.extend(validate_design_semantics(path, fixture))
        design_id = fixture.get("meta", {}).get("id")
        if isinstance(design_id, str):
            design_systems[design_id] = fixture
        if design_id != path.stem:
            issues.append(ValidationIssue(relative(path), "design-system id must match the fixture filename"))

    permission_files = sorted((FIXTURE_DIR / "editor-permissions").glob("*.yaml"))
    for path in permission_files:
        fixture = load_yaml(path)
        issues.extend(validate_instance(path, fixture, schemas["editor-permissions"], registry))
        issues.extend(validate_permission_semantics(path, fixture))

    theme_files = sorted((SKILL_DIR / "themes").glob("*/theme.yaml"))
    for path in theme_files:
        fixture = load_yaml(path)
        issues.extend(validate_instance(path, fixture, schemas["theme"], registry))
        issues.extend(validate_theme_semantics(path, fixture))

    ir_files = sorted((FIXTURE_DIR / "ir").glob("*.yaml"))
    for path in ir_files:
        fixture = load_yaml(path)
        issues.extend(validate_instance(path, fixture, schemas["presentation-ir"], registry))
        issues.extend(validate_ir_semantics(path, fixture, scenarios, design_systems))
        if fixture.get("deck", {}).get("scenario", {}).get("id") != path.stem:
            issues.append(ValidationIssue(relative(path), "IR scenario id must match the fixture filename"))

    counts = {
        "schemas": len(schemas),
        "scenario_fixtures": len(scenario_files),
        "design_system_fixtures": len(design_files),
        "permission_fixtures": len(permission_files),
        "theme_fixtures": len(theme_files),
        "ir_fixtures": len(ir_files),
    }
    return issues, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit machine-readable results")
    args = parser.parse_args()

    try:
        issues, counts = run_validation()
    except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError) as exc:
        issues = [ValidationIssue("validation", str(exc))]
        counts = {}

    if args.json:
        print(
            json.dumps(
                {
                    "valid": not issues,
                    "counts": counts,
                    "issues": [issue.__dict__ for issue in issues],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif issues:
        for issue in issues:
            print(f"ERROR {issue.path}: {issue.message}", file=sys.stderr)
        print(f"Validation failed with {len(issues)} issue(s).", file=sys.stderr)
    else:
        print(
            "Validated "
            f"{counts['schemas']} schemas, "
            f"{counts['scenario_fixtures']} scenarios, "
            f"{counts['design_system_fixtures']} design systems, "
            f"{counts['permission_fixtures']} permission models, and "
            f"{counts['theme_fixtures']} themes, and "
            f"{counts['ir_fixtures']} Presentation IR fixtures."
        )
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
