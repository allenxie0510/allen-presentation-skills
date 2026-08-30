# Professional Presentation System Architecture

## Purpose

This Skill is the portable foundation for a professional presentation intelligence
system. It separates communication reasoning, content structure, visual grammar,
rendering, and editing so each layer can evolve without turning the HTML DOM or a
single platform prompt into the product architecture.

## Canonical pipeline

```text
Brief
→ Scenario and optional industry context
→ Storyline
→ Slide grammar
→ Presentation IR
→ Brand and approved design-system resolution
→ Renderer
→ Design-safe refinement
→ Export
```

The Presentation IR is the only canonical representation. A renderer may produce
editable HTML, PDF, PPTX, or another format, but edits must be representable in the
IR if they are expected to survive save/load or cross-format export.

## Layer boundaries

### Scenario

Defines the communication job, audience, decision types, evidence standard,
storyline patterns, density, preferred information grammar, required archetypes,
and anti-patterns. It must not contain renderer code or a complete visual theme.

### Industry pack

Supplies terminology, evidence conventions, chart conventions, compliance
constraints, and examples. It is a reference pack by default so scenario × industry
combinations do not create a combinatorial number of Skills.

### Presentation IR

Describes the deck, slides, objects, stable IDs, authoring frames, semantic roles,
style-token references, and editing permissions. It must be valid before rendering.

### Design system

Describes how information is expressed: composition, grid, hierarchy, spacing,
color behavior, typography behavior, motifs, component grammar, and archetypes.
New systems begin as `draft`; normal generation may use only `approved` systems.

### Renderer

Consumes Presentation IR plus a design system and emits a view. It must not own
scenario reasoning or silently mutate the narrative. The HTML renderer should use
a fixed 1920 × 1080 stage with uniform viewport scaling.

### Editor

Refines a generated presentation. Safe mode protects authored slots, grid,
hierarchy, decoration, and token usage. Freeform movement and resize require an
explicit unlock. Editor actions update IR first or round-trip to it deterministically.

## Slide grammar

Use semantic grammar before choosing layouts:

```text
assertion, evidence, trend, comparison, causality, process,
hierarchy, relationship, decision, narrative, quote, image-led
```

Archetypes are visual manifestations of grammar, not templates selected by topic.
For example, trend prefers line, slope, or indexed series; comparison prefers a
split comparison, benchmark table, or before/after; causality prefers a driver tree,
causal chain, or annotated flow.

## Precedence

```text
Explicit brand rules
> approved design system
> industry convention
> generic visual preference
```

Communication goal and audience decisions precede this visual precedence chain.

## Source composition and portable release

Development may share schemas, renderer modules, runtime assets, and quality tools.
A released Skill must be self-contained: no absolute paths, symlinks, or references
outside its own directory. Platform adapters are optional projections and cannot
contain the only copy of the core method.

## Phase plan

### Phase 0 — completed

- Freeze four schemas.
- Validate distinct board-review, investor-pitch, and teaching-deck fixtures.
- Validate one complete design-system fixture and the editor-permission model.

### Phase 1 — current

- Render validated IR to a fixed-stage, self-contained HTML deck.
- Provide navigation, notes, inline text refinement, HTML download, and print.
- Define the six-layer Allen design-system contract and one draft foundation.
- Package the runtime with standalone scenario Skills.

### Later phases

1. Edit-to-IR synchronization.
2. Three designer-approved systems and a design-system creator workflow.
3. Native PPTX export.
4. Broader browser visual regression and cross-format fidelity checks.

Do not migrate large template libraries. Expand the runtime only when a concrete
scenario, archetype, or edit requirement cannot be represented through the IR
and the six-layer design-system contract.

## Phase 0 acceptance

- All JSON Schemas pass Draft 2020-12 meta-validation.
- Every bundled fixture passes its assigned schema.
- Canvas dimensions are fixed to 1920 × 1080.
- Slide and object IDs are unique within each IR fixture.
- The design system defines every required archetype.
- The permission model defines locked, content-only, content-style, and freeform.
- No fixture claims designer approval unless a human has approved it.
