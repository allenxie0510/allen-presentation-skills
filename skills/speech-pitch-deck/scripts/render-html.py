#!/usr/bin/env python3
"""Render a validated Presentation IR and design system to one offline HTML deck."""

from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
from pathlib import Path
import re
import sys
import math
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
    from referencing import Registry, Resource
except ModuleNotFoundError as exc:
    print(
        "Missing renderer dependency. Install scripts/requirements.txt "
        f"before rendering ({exc.name}).",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


SKILL_DIR = Path(__file__).resolve().parents[1]
SCHEMA_DIR = SKILL_DIR / "schemas"
ASSET_DIR = SKILL_DIR / "assets" / "web-deck"
SAFE_STYLE_OVERRIDES = {
    "background",
    "background-color",
    "border",
    "border-color",
    "border-radius",
    "color",
    "font-size",
    "font-weight",
    "line-height",
    "letter-spacing",
    "opacity",
    "padding",
    "text-align",
    "z-index",
}


def load_structured(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        if path.suffix.lower() == ".json":
            value = json.load(handle)
        else:
            value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


def schema_registry(schemas: list[dict[str, Any]]) -> Registry:
    resources = []
    for schema in schemas:
        schema_id = schema.get("$id")
        if isinstance(schema_id, str):
            resources.append((schema_id, Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def validate(ir: dict[str, Any], design: dict[str, Any], theme: dict[str, Any] | None = None) -> list[str]:
    ir_schema = load_schema("presentation-ir.schema.json")
    design_schema = load_schema("design-system.schema.json")
    editor_schema = load_schema("editor-permissions.schema.json")
    theme_schema = load_schema("theme.schema.json")
    registry = schema_registry([ir_schema, design_schema, editor_schema, theme_schema])
    issues = []
    checks = (("IR", ir, ir_schema), ("design", design, design_schema))
    if theme is not None:
        checks += (("theme", theme, theme_schema),)
    for label, instance, schema in checks:
        validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path)):
            location = ".".join(str(part) for part in error.absolute_path) or "$"
            issues.append(f"{label}:{location}: {error.message}")

    design_ref = ir.get("deck", {}).get("design_system", {})
    design_meta = design.get("meta", {})
    if design_ref.get("id") != design_meta.get("id"):
        issues.append("IR design_system.id does not match the supplied design system")
    if design_ref.get("version") != design_meta.get("version"):
        issues.append("IR design_system.version does not match the supplied design system")
    if theme is not None and theme.get("design_system", {}).get("id") != design_meta.get("id"):
        issues.append("theme design_system.id does not match the supplied design system")

    object_ids: set[str] = set()
    for slide_index, slide in enumerate(ir.get("slides", [])):
        archetype = slide.get("archetype")
        design_archetype = design.get("archetypes", {}).get(archetype)
        if not design_archetype:
            issues.append(f"IR:slides.{slide_index}.archetype: design system does not define {archetype}")
        elif slide.get("layout_variant") not in design_archetype.get("variants", []):
            issues.append(
                f"IR:slides.{slide_index}.layout_variant: {slide.get('layout_variant')} "
                f"is not allowed for {archetype}"
            )
        for obj in slide.get("objects", []):
            object_id = obj.get("id")
            if object_id in object_ids:
                issues.append(f"IR: duplicate object id {object_id}")
            if isinstance(object_id, str):
                object_ids.add(object_id)
            frame = obj.get("frame", {})
            if frame.get("x", 0) + frame.get("w", 0) > 1920 or frame.get("y", 0) + frame.get("h", 0) > 1080:
                issues.append(f"IR:{object_id}: frame exceeds 1920×1080")
            fit_issue = text_fit_issue(obj, design)
            if fit_issue:
                issues.append(f"IR:{object_id}: {fit_issue}")
    return issues


def text_fit_issue(obj: dict[str, Any], design: dict[str, Any]) -> str | None:
    if obj.get("type") != "text":
        return None
    text = str(obj.get("content", {}).get("text", ""))
    if not text:
        return None
    token = obj.get("style", {}).get("token", "typography.body")
    role_name = token.split(".", 1)[1] if token.startswith("typography.") else "body"
    role = design.get("typography", {}).get(role_name, design["typography"]["body"])
    overrides = obj.get("style", {}).get("overrides", {})
    font_size = float(overrides.get("font_size", overrides.get("font-size", role["size"])))
    line_height = float(overrides.get("line_height", overrides.get("line-height", role["line_height"])))
    frame = obj.get("frame", {})
    width = float(frame.get("w", 1))
    height = float(frame.get("h", 1))
    width_em = max(1.0, width / font_size)
    explicit_lines = text.splitlines() or [text]
    estimated_lines = 0
    for line in explicit_lines:
        weighted = sum(
            1.0 if ord(character) > 0x2FF else 0.28 if character.isspace() else 0.56
            for character in line
        )
        estimated_lines += max(1, math.ceil(weighted / width_em))
    required_height = estimated_lines * font_size * line_height * 1.06
    if required_height > height:
        return (
            f"estimated text height {required_height:.0f}px exceeds frame height {height:.0f}px; "
            "split the slide, shorten the text, enlarge the frame, or lower the approved type token"
        )
    return None


def css_family(role: dict[str, Any]) -> str:
    families = []
    preferred = role.get("preferred_family")
    if preferred:
        families.append(preferred)
    families.extend(role.get("fallback", []))
    rendered = []
    for family in families:
        if family.lower() in {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui"}:
            rendered.append(family)
        else:
            rendered.append(f'"{family}"')
    return ", ".join(rendered)


def typography_style(role: dict[str, Any]) -> dict[str, str]:
    return {
        "font-family": css_family(role),
        "font-size": f"{role['size']}px",
        "font-weight": str(role["weight"]),
        "line-height": str(role["line_height"]),
        "letter-spacing": f"{role['tracking']}em",
    }


def style_overrides(value: dict[str, Any]) -> dict[str, str]:
    rendered: dict[str, str] = {}
    for raw_key, raw_value in value.items():
        key = raw_key.replace("_", "-")
        if key not in SAFE_STYLE_OVERRIDES:
            continue
        if isinstance(raw_value, bool):
            rendered[key] = "true" if raw_value else "false"
        elif isinstance(raw_value, (int, float)) and key not in {"font-weight", "line-height", "opacity", "z-index"}:
            rendered[key] = f"{raw_value}px"
        else:
            rendered[key] = str(raw_value)
    return rendered


def object_style(obj: dict[str, Any], design: dict[str, Any]) -> str:
    frame = obj["frame"]
    styles = {
        "left": f"{frame['x']}px",
        "top": f"{frame['y']}px",
        "width": f"{frame['w']}px",
        "height": f"{frame['h']}px",
    }
    if frame.get("rotation"):
        styles["transform"] = f"rotate({frame['rotation']}deg)"

    token = obj.get("style", {}).get("token", "")
    if token.startswith("typography."):
        role_name = token.split(".", 1)[1]
        role = design.get("typography", {}).get(role_name)
        if role:
            styles.update(typography_style(role))
    elif obj.get("type") == "metric":
        styles.update({"font-family": css_family(design["typography"]["metric"])})
    elif obj.get("type") in {"text", "table", "group"}:
        styles.update(typography_style(design["typography"]["body"]))

    styles.update(style_overrides(obj.get("style", {}).get("overrides", {})))
    return ";".join(f"{key}:{value}" for key, value in styles.items())


def editable_attribute(obj: dict[str, Any]) -> str:
    return "true" if obj.get("editable", {}).get("content") else "false"


def text_target(value: Any) -> str:
    return f'<span data-edit-target="true">{html.escape(str(value))}</span>'


def embed_image(src: str, base_dir: Path, allow_remote: bool) -> str:
    if re.match(r"^https?://", src):
        if not allow_remote:
            raise ValueError(f"remote image requires --allow-remote-assets: {src}")
        return src
    if src.startswith("data:"):
        return src
    path = (base_dir / src).resolve() if not Path(src).is_absolute() else Path(src)
    if not path.is_file():
        raise ValueError(f"image not found: {src}")
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def render_chart(content: dict[str, Any], design: dict[str, Any]) -> str:
    categories = content.get("categories", [])
    series = content.get("series", [])
    values = [abs(float(value)) for item in series for value in item.get("values", []) if isinstance(value, (int, float))]
    maximum = max(values, default=1)
    colors = [design["colors"].get("accent_secondary", design["colors"]["accent_primary"]), design["colors"]["accent_primary"], design["colors"]["positive"]]
    groups = []
    for category_index, category in enumerate(categories):
        bars = []
        for series_index, item in enumerate(series):
            item_values = item.get("values", [])
            if category_index >= len(item_values) or not isinstance(item_values[category_index], (int, float)):
                continue
            value = item_values[category_index]
            height = max(2, abs(float(value)) / maximum * 82)
            color = item.get("color") or colors[series_index % len(colors)]
            bars.append(
                f'<div class="chart__bar" style="height:{height}%;--series-color:{html.escape(str(color), quote=True)}" '
                f'title="{html.escape(str(item.get("name", "Series")), quote=True)}: {value}">'
                f'<span class="chart__value">{html.escape(str(value))}</span></div>'
            )
        groups.append(
            '<div class="chart__group">'
            + "".join(bars)
            + f'<span class="chart__category">{html.escape(str(category))}</span></div>'
        )
    return "".join(groups) or text_target("Chart data unavailable")


def render_object(obj: dict[str, Any], design: dict[str, Any], base_dir: Path, allow_remote: bool) -> str:
    object_type = obj["type"]
    content = obj.get("content", {})
    role = obj.get("role", "content")
    attributes = (
        f'id="{html.escape(obj["id"], quote=True)}" '
        f'class="object object--{html.escape(object_type, quote=True)}" '
        f'data-role="{html.escape(role, quote=True)}" '
        f'data-editable="{editable_attribute(obj)}" '
        f'style="{html.escape(object_style(obj, design), quote=True)}"'
    )

    if object_type == "text":
        inner = text_target(content.get("text", ""))
    elif object_type == "metric":
        inner = (
            f'<div class="metric__label" data-edit-target="true">{html.escape(str(content.get("label", "")))}</div>'
            f'<div class="metric__value" data-edit-target="true">{html.escape(str(content.get("value", "")))}</div>'
            '<div class="metric__meta">'
            f'<span data-edit-target="true">{html.escape(str(content.get("period", "")))}</span>'
            f'<span data-edit-target="true">{html.escape(str(content.get("delta", "")))}</span>'
            '</div>'
        )
    elif object_type == "image":
        src = embed_image(str(content.get("src", "")), base_dir, allow_remote)
        alt = html.escape(str(content.get("alt", "")), quote=True)
        fit = html.escape(str(content.get("fit", "cover")), quote=True)
        inner = f'<img src="{html.escape(src, quote=True)}" alt="{alt}" style="object-fit:{fit}">'
    elif object_type == "table":
        columns = content.get("columns", [])
        rows = content.get("rows", [])
        head = '<div class="table__row table__row--head">' + "".join(
            f'<div class="table__cell" data-edit-target="true">{html.escape(str(cell))}</div>' for cell in columns
        ) + "</div>"
        body = "".join(
            '<div class="table__row">' + "".join(
                f'<div class="table__cell" data-edit-target="true">{html.escape(str(cell))}</div>' for cell in row
            ) + "</div>" for row in rows
        )
        inner = f'<div style="--columns:{max(1, len(columns))}">{head}{body}</div>'
    elif object_type == "group":
        stages = content.get("stages", [])
        inner = "".join(f'<div class="group__stage">{text_target(stage)}</div>' for stage in stages)
    elif object_type == "chart":
        inner = render_chart(content, design)
    elif object_type == "shape":
        inner = text_target(content.get("text", "")) if content.get("text") else ""
    elif object_type == "divider":
        inner = ""
    elif object_type == "icon":
        inner = text_target(content.get("glyph", content.get("label", "")))
    else:
        inner = text_target(json.dumps(content, ensure_ascii=False))
    return f"<div {attributes}>{inner}</div>"


def css_variables(design: dict[str, Any], theme: dict[str, Any] | None = None) -> str:
    colors = theme["colors"] if theme is not None else design["colors"]
    values = {
        "--deck-canvas": colors["canvas"],
        "--deck-surface": colors["surface"],
        "--deck-text": colors["text_primary"],
        "--deck-muted": colors["text_secondary"],
        "--deck-accent": colors["accent_primary"],
        "--deck-accent-2": colors.get("accent_secondary", colors["accent_primary"]),
        "--deck-positive": colors["positive"],
        "--deck-negative": colors["negative"],
        "--deck-rule": colors["rule"],
    }
    return ":root{" + ";".join(f"{key}:{value}" for key, value in values.items()) + "}"


def load_theme_styles(theme: dict[str, Any] | None, theme_path: Path | None) -> str:
    if theme is None or theme_path is None:
        return ""
    stylesheet = theme.get("stylesheet")
    if not isinstance(stylesheet, str):
        raise ValueError("theme stylesheet must be a relative CSS path")
    root = theme_path.resolve().parent
    path = (root / stylesheet).resolve()
    if root != path.parent and root not in path.parents:
        raise ValueError("theme stylesheet escapes the theme directory")
    if not path.is_file():
        raise ValueError(f"theme stylesheet not found: {stylesheet}")
    css = path.read_text(encoding="utf-8")

    def inline_local_asset(match: re.Match[str]) -> str:
        source = match.group("source").strip()
        if source.startswith(("data:", "#")):
            return match.group(0)
        if re.match(r"^[a-z][a-z0-9+.-]*:", source, re.IGNORECASE):
            raise ValueError(f"remote or protocol theme asset is not offline-safe: {source}")
        asset = (path.parent / source).resolve()
        if root != asset and root not in asset.parents:
            raise ValueError(f"theme asset escapes the theme directory: {source}")
        if not asset.is_file():
            raise ValueError(f"theme asset not found: {source}")
        mime = mimetypes.guess_type(asset.name)[0] or "application/octet-stream"
        encoded = base64.b64encode(asset.read_bytes()).decode("ascii")
        return f'url("data:{mime};base64,{encoded}")'

    return re.sub(
        r"url\(\s*(?P<quote>['\"]?)(?P<source>[^'\")]+)(?P=quote)\s*\)",
        inline_local_asset,
        css,
    )


def render_document(
    ir: dict[str, Any],
    design: dict[str, Any],
    ir_path: Path,
    allow_remote: bool,
    theme: dict[str, Any] | None = None,
    theme_path: Path | None = None,
) -> str:
    base_css = (ASSET_DIR / "base.css").read_text(encoding="utf-8")
    runtime_js = (ASSET_DIR / "runtime.js").read_text(encoding="utf-8")
    slide_html = []
    for index, slide in enumerate(ir["slides"]):
        child_ids = {child for obj in slide["objects"] for child in obj.get("children", [])}
        objects = [
            render_object(obj, design, ir_path.parent, allow_remote)
            for obj in slide["objects"]
            if obj["id"] not in child_ids
        ]
        sources = []
        for evidence in slide.get("evidence", []):
            source = evidence.get("source") or evidence.get("source_type")
            if source:
                sources.append(str(source))
        source_html = f'<div class="slide__source">Source: {html.escape(" · ".join(sources))}</div>' if sources else ""
        notes = html.escape(str(slide.get("speaker_notes") or ""), quote=True)
        section = slide.get("narrative_role", {}).get("section", "")
        grammar = slide.get("grammar", "")
        variant = slide.get("layout_variant", "")
        slide_html.append(
            f'<section id="{html.escape(slide["id"], quote=True)}" '
            f'class="slide slide--{html.escape(slide["archetype"], quote=True)}{" active" if index == 0 else ""}" '
            f'data-sequence="{index + 1:02d}" data-notes="{notes}" '
            f'data-grammar="{html.escape(grammar, quote=True)}" '
            f'data-layout="{html.escape(variant, quote=True)}" '
            f'aria-label="Slide {index + 1}: {html.escape(slide["assertion"]["text"], quote=True)}">'
            f'<div class="slide__eyebrow">{html.escape(str(section).replace("-", " "))}</div>'
            + "".join(objects)
            + source_html
            + "</section>"
        )

    deck = ir["deck"]
    theme_id = theme.get("meta", {}).get("id", "base") if theme else "base"
    theme_styles = load_theme_styles(theme, theme_path)
    return f'''<!doctype html>
<html lang="{html.escape(deck["language"], quote=True)}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="generator" content="Allen Presentation Core">
  <title>{html.escape(deck["title"])}</title>
  <style>
{base_css}
{css_variables(design, theme)}
{theme_styles}
  </style>
</head>
<body data-theme="{html.escape(str(theme_id), quote=True)}" data-scenario="{html.escape(deck['scenario']['id'], quote=True)}">
  <main class="deck-viewport" aria-label="{html.escape(deck["title"], quote=True)}">
    <div class="deck-stage" data-deck-id="{html.escape(deck["id"], quote=True)}">
      {''.join(slide_html)}
    </div>
  </main>
  <nav class="deck-ui" aria-label="Presentation controls">
    <button type="button" data-action="prev" aria-label="Previous slide">←</button>
    <span data-deck-counter>1 / {len(ir["slides"])}</span>
    <div class="deck-ui__progress" aria-hidden="true"><span data-deck-progress></span></div>
    <button type="button" data-action="next" aria-label="Next slide">→</button>
    <button type="button" data-action="notes" title="Speaker notes (N)">N</button>
    <button type="button" data-action="edit" title="Edit text (E)">E</button>
    <button type="button" data-action="save" title="Download edited HTML (Ctrl/Cmd+S)">Save</button>
  </nav>
  <aside class="notes-panel" aria-live="polite"></aside>
  <script>
{runtime_js}
  </script>
</body>
</html>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ir", type=Path, help="Presentation IR YAML or JSON")
    parser.add_argument("--design", required=True, type=Path, help="design-system YAML or JSON")
    parser.add_argument("--output", required=True, type=Path, help="output HTML path")
    parser.add_argument("--allow-draft-design", action="store_true")
    parser.add_argument("--theme", type=Path, help="optional theme-pack YAML")
    parser.add_argument("--allow-draft-theme", action="store_true")
    parser.add_argument("--allow-remote-assets", action="store_true")
    args = parser.parse_args()

    try:
        ir = load_structured(args.ir)
        design = load_structured(args.design)
        theme = load_structured(args.theme) if args.theme else None
        issues = validate(ir, design, theme)
        if issues:
            for issue in issues:
                print(f"ERROR {issue}", file=sys.stderr)
            return 1
        status = design["meta"]["status"]
        if status != "approved" and not args.allow_draft_design:
            print(
                f"ERROR design system is {status}; pass --allow-draft-design for a labeled prototype",
                file=sys.stderr,
            )
            return 1
        if theme is not None and theme["meta"]["status"] != "approved" and not args.allow_draft_theme:
            print(
                f"ERROR theme is {theme['meta']['status']}; pass --allow-draft-theme for a labeled prototype",
                file=sys.stderr,
            )
            return 1
        rendered = render_document(
            ir,
            design,
            args.ir.resolve(),
            args.allow_remote_assets,
            theme,
            args.theme.resolve() if args.theme else None,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1

    print(
        f"Rendered {len(ir['slides'])} slides to {args.output} "
        f"with {design['meta']['id']} {design['meta']['version']} ({design['meta']['status']})"
        + (f" and theme {theme['meta']['id']} {theme['meta']['version']} ({theme['meta']['status']})." if theme else ".")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
