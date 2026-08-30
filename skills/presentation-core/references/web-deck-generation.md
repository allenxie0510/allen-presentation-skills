# Web deck generation workflow

Use this workflow only when the user asks for an actual web presentation, HTML
deck, or browser-viewable PPT—not for planning-only work.

## Inputs and outputs

Required inputs:

- a normalized brief and selected scenario;
- an assertion-led storyline;
- evidence and explicit placeholders for missing evidence;
- a schema-valid Presentation IR;
- a design system matching `schemas/design-system.schema.json`.

Required outputs:

- `<deck-id>.ir.yaml`, the canonical editable source;
- `<deck-id>.html`, a self-contained browser presentation;
- validation and visual-check results;
- a short usage note for navigation, editing, saving, and print/PDF.

## Generation sequence

1. Choose the scenario before the design profile.
2. Map each storyline beat to a Slide Grammar term and archetype.
3. Create the IR at a fixed 1920 × 1080 canvas. Keep stable IDs and evidence
   references. Do not put internal instructions on visible slides.
4. Use `allen-signal-grid` as a draft foundation unless the user supplies a
   brand system or later approved Allen design system. Apply the scenario
   expression profile from `allen-design-system.md`.
5. Validate the IR and design system.
6. Render with:

   ```bash
   python scripts/render-html.py <deck.ir.yaml> \
     --design references/allen-signal-grid.yaml \
     --output <deck.html> \
     --allow-draft-design
   ```

7. Open or screenshot the HTML and inspect every slide for overflow, overlap,
   weak contrast, tiny text, misleading charts, hidden sources, and broken image
   paths. Fix the IR or design tokens, not the generated HTML, then rerender.

## Runtime behavior

- Arrow keys, Page Up/Down, Space, Home, and End navigate.
- `E` toggles inline text editing for editable objects.
- `Cmd/Ctrl+S` downloads the edited HTML.
- `N` toggles speaker notes.
- `F` enters fullscreen.
- `P` opens browser print for PDF export.
- Swipe navigates on touch screens.

The HTML is a projection. Inline edits are convenient for refinement, but the IR
remains canonical. Important edits should be written back to IR before the next
render.

## Content and visual guardrails

- Split overloaded slides; never shrink content below the design-system minimum.
- Use charts only when the data and comparison are supplied. Otherwise render a
  labeled placeholder or omit the chart.
- Do not invent images, logos, metrics, quotes, approvals, or sources.
- Use relative local images or data URLs. Remote images require explicit
  `--allow-remote-assets` because they break offline delivery.
- Draft design systems may be used for prototypes only with
  `--allow-draft-design`; do not describe them as approved.
- A rendered file is not verified until it has passed schema validation and
  visual inspection.
