# Allen presentation design-system contract

This contract defines the stable anatomy of an Allen presentation design system.
It was informed by reviewing fixed-stage HTML slide systems, but its visual
language, tokens, archetypes, evidence behavior, and renderer are independently
authored. Do not copy a reference deck's palette, typography pairing, decorative
motifs, layout recipes, or source code.

## Six layers

### 1. Intent and boundaries

Record tone, formality, energy, density, suitable scenarios, and scenarios to
avoid. Scenario and audience determine the design-system profile; visual taste
does not determine the scenario.

### 2. Foundation tokens

Define a fixed 1920 × 1080 canvas, grid, margins, gutters, spacing scale, colors,
type roles, image treatment, and surface behavior. Brand rules override these
defaults. Every color role must describe meaning, not just a swatch name.

### 3. Information components

Define metrics, evidence quotes, charts, tables, process stages, decision gates,
source notes, image captions, and annotations. Components carry evidence and
reasoning; they are not decorative cards.

### 4. Slide archetypes

Map semantic Slide Grammar to layouts. At minimum cover: cover, section,
statement, two-column, comparison, data, chart, timeline, process, quote, image,
and closing. Scenario packs may add variants such as Now/Next/Later,
opportunity-solution tree, profit-pool map, pitch proof, annotated artifact, or
activity brief without changing the stable layer anatomy.

### 5. Data, motion, and accessibility

Specify direct labeling, axes, uncertainty, source placement, entry motion,
reduced-motion behavior, minimum readable sizes, contrast target, non-color
signals, and DOM reading order. Motion reveals narrative order; it must not hide
evidence or imply causality.

Treat text color as a surface role. On a light canvas or light component, use the
primary dark text token for assertions and a secondary dark-gray token for
supporting copy; white or near-white text is prohibited. Light text is allowed
only when the same text element or a stable ancestor owns a sufficiently dark,
opaque surface. Do not rely on a crossing line, image crop, gradient highlight,
or decorative pseudo-element to provide contrast. Require at least 4.5:1 for all
audience-facing text so layout movement and responsive stage scaling cannot turn
an apparent overlay into low-contrast text.

### 6. Runtime and governance

Specify the fixed-stage scaling model, self-contained output, offline behavior,
editing boundary, approval status, provenance, version, and reviewer. New
systems remain `draft` until a designer reviews actual rendered slides across
several archetypes.

## Scenario expression profiles

All five profiles use the same six layers and the `allen-signal-grid` foundation.
They change emphasis, not the underlying evidence standard.

| Scenario | Narrative rhythm | Density | Dominant archetypes | Expression adjustment |
|---|---|---:|---|---|
| Product Roadmap | outcome → opportunity → choices → commitment | medium-high | scorecard, opportunity tree, trade-off matrix, Now/Next/Later, decision | blue for committed structure; orange for decision gates |
| Industry Research | definition → evidence → structure → scenarios → implication | high | scope map, source ledger, range chart, profit-pool map, scenario matrix | restrained surfaces, denser annotations, visible source rail |
| Speech / Pitch | tension → proposition → proof → future → ask | low | statement, image-led proof, metric, contrast, closing ask | larger type, fewer objects, stronger pacing and dark/light alternation |
| UX / Brand Case | challenge → evidence → reasoning → system → outcome → reflection | medium | annotated artifact, iteration comparison, system map, outcome table | image-led composition with neutral evidence captions |
| Training Workshop | performance need → model → practice → feedback → transfer | medium | learning promise, worked example, activity brief, process, assessment, commitment | numbered activity cues and accessible instructional hierarchy |

## Design review checklist

For a new theme or major redesign, this checklist is only the correctness layer.
Run the full concept gate and five-lens review in
[allen-frame-method.md](allen-frame-method.md) before calling the system an
approval candidate.

- Can the storyline still be understood with decoration removed?
- Does every substantive slide have one assertion or audience job?
- Does the visual mapping match the reasoning grammar?
- Are facts, estimates, assumptions, and recommendations distinguishable?
- Are sources, periods, units, and uncertainty visible where material?
- Is body text at least the design system's minimum size?
- Does the slide fit at 1920 × 1080 without overlap or overflow?
- Does it remain interpretable without color?
- Does every text element retain at least 4.5:1 contrast against its owned surface, with no white text on light surfaces?
- Does reduced-motion mode preserve all information?
- Is the output labeled draft until a designer approves the rendered system?
