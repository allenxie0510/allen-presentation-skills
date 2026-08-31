---
name: presentation-core
description: Plan, structure, and render professional web or native PPTX presentations using scenario-aware communication logic, a canonical Presentation IR, designer-curated design systems, and design-safe editing constraints. Use for board reviews, investor pitches, teaching decks, consulting or research presentations, and reusable presentation-system work. Do not use for simple file conversion or isolated cosmetic edits that do not need storyline or information-architecture decisions.
license: MIT
metadata:
  owner: "allenxie"
  category: "presentation"
  maturity: "draft"
  risk: "local-write"
  version: "0.5.1"
  origin: "personal"
  importance: "flagship"
  visibility: "public"
  public_url: "https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/presentation-core"
  compatibility: "Requires PyYAML and a JSON Schema Draft 2020-12 validator. Bundled runtime renders fixed-stage HTML; native PPTX mode requires a compatible editable-PPTX renderer."
---

# Professional Presentation Core

Build professional presentations by resolving the communication job before the
visual treatment. Keep the Presentation IR as the source of truth; rendered HTML,
PPTX, or other output is a projection of that model, never the canonical state.

## Current release boundary

Version 0.5.1 adds a renderer-neutral native PPTX production contract, a
schema-valid production profile, asset-first image handling, cross-slide cadence,
room-scale typography, editable-object requirements, and render-based release
gates. It also requires slot-ratio-aware image generation, meaningful work
artifacts, and explicit cast, workplace, clothing, and cultural-continuity QA for
international team photography. The bundled runtime still renders self-contained HTML; native PPTX requires
a compatible editable-PPTX renderer and is a projection of the canonical IR.
Browser edits do not automatically round-trip into IR. Do not imply a standalone
PPTX renderer is bundled when it is not.

Read [references/architecture.md](references/architecture.md) for new presentation
systems, renderer/editor work, or changes that affect more than one schema.

## Route the work

- For a professional deck brief, normalize the communication goal, audience,
  decision or learning outcome, evidence, constraints, and delivery format. Ask
  only for missing information that would materially change the storyline.
- For a scenario, use or extend
  [schemas/scenario.schema.json](schemas/scenario.schema.json). Keep industry
  knowledge as a reference pack unless it needs independent behavior.
- For a deck plan or generation request, create a schema-valid Presentation IR
  using [schemas/presentation-ir.schema.json](schemas/presentation-ir.schema.json).
- For a visual system derived from references, use
  [schemas/design-system.schema.json](schemas/design-system.schema.json). Mark new
  systems `draft`; only a designer may promote one to `approved`.
- For a new theme, a major visual redesign, or an ambiguous high-fidelity
  direction, read [references/allen-frame-method.md](references/allen-frame-method.md).
  Record three structurally distinct routes with
  [schemas/design-direction.schema.json](schemas/design-direction.schema.json),
  render the same representative content for each route, and review the selected
  route with [schemas/design-review.schema.json](schemas/design-review.schema.json).
  Do not describe an agent-selected route as user-approved.
- For theme selection, read `themes/index.yaml` first. Load only shortlisted
  `preview.md` files, then the selected `theme.yaml`, `theme.css`, and its
  `design-system.md` when present. Do not read every full theme before the
  scenario and shortlist are known.
- For Allen design-system anatomy and scenario expression profiles, read
  [references/allen-design-system.md](references/allen-design-system.md).
- For an actual browser deck, read
  [references/web-deck-generation.md](references/web-deck-generation.md), create
  a valid IR, and render with `scripts/render-html.py`. Use the draft
  `fixtures/design-systems/allen-signal-grid.yaml` only with explicit draft
  allowance and never describe it or any bundled theme as approved. Pass the
  selected theme with `--theme themes/<id>/theme.yaml --allow-draft-theme`.
- For an editable native PPTX, read
  [references/native-pptx-production.md](references/native-pptx-production.md),
  validate a profile against
  [schemas/native-pptx-profile.schema.json](schemas/native-pptx-profile.schema.json),
  and use a compatible PPTX renderer. Preflight evidence and images before
  composition, record energy and silhouette for every slide, and render every
  slide for full-size plus contact-sheet inspection before release.
- For a new scenario template, a major template upgrade, or promotion from a
  successful deck to a reusable Skill, read
  [references/scenario-template-production.md](references/scenario-template-production.md).
  Reuse its production and release gates while redesigning narrative, industry
  evidence, cultural context, photography, component grammar, and visual rhythm
  for the new scenario.
- For editing behavior, apply
  [schemas/editor-permissions.schema.json](schemas/editor-permissions.schema.json).
  Default to protected slots and require an explicit unlock before freeform layout.
- Before handing an IR or design system to a renderer, run
  `python scripts/validate-schemas.py` from this Skill directory.

## Decision order

Resolve in this order:

1. Communication goal.
2. Audience and required decision, belief, or learning outcome.
3. Storyline and evidence standard.
4. Slide grammar and archetypes.
5. Brand constraints.
6. FRAME direction exploration when the visual premise is new or unresolved.
7. Approved design system.
8. Delivery-format profile and renderer-specific implementation.

Do not select a visual preset before the communication job is clear. Prefer an
assertion-led slide sequence; every substantive slide should have a purpose and a
claim or audience job that can be evaluated.

## Invariants

- Author at 1920 × 1080 and let the renderer apply uniform scale. Do not model a
  slide as responsive reflow.
- Keep scenario logic, design-system logic, IR, renderer, and editor permissions
  separable.
- Treat a slot as design-authored and protected. Treat a user-added object as
  freeform refinement content.
- Preserve stable deck, slide, and object IDs across edit/save/load cycles.
- Explicit brand rules override the approved design system, which overrides
  industry convention and generic visual preference.
- Never claim an exact font match without evidence. Record its class,
  characteristics, and substitutes when identification is uncertain.
- Do not fabricate claims, numbers, sources, or approval status.
- Do not imitate a named designer or studio. Transfer a documented principle and
  record the signature expression that must not be copied.
- Treat aesthetic rules as standards only when source, intent, observable signal,
  failure case, and override boundary are recorded.
- Keep process notes, prompt scaffolds, and internal commentary out of
  audience-facing slide content.

## Output contract

For planning or generation work, produce:

1. a normalized brief;
2. the selected scenario and rationale;
3. an assertion-led storyline;
4. a valid Presentation IR;
5. a FRAME direction record and review when the task creates or substantially
   changes visual language;
6. the approved design-system selection, or a clearly labeled draft;
7. a validation result;
8. rendered self-contained HTML or native editable PPTX when requested and a
   compatible renderer is available, followed by full visual inspection;
   otherwise stop at the validated IR and disclose the renderer boundary.

Use the fixtures under `fixtures/` as structural examples, not as content or
visual templates to copy mechanically.
