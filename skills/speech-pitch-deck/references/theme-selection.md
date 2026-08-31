# Theme Selection Workflow

Choose the scenario before choosing visual expression. Themes do not change the
evidence, conclusion, or scenario narrative.

1. Read `themes/index.yaml` for compact metadata only.
2. Use the scenario profile's `theme_recommendations` to shortlist three themes.
3. Show each shortlisted contact sheet from `gallery/previews/<scenario>/<theme>.webp`.
   Each sheet contains the same content rendered as cover, core component, and
   closing slide, so the comparison is fair.
4. Read only the shortlisted themes' `preview.md` files.
5. Ask the user to select a theme or accept the scenario default.
6. Load only the selected `theme.yaml`, `theme.css`, and linked art-direction
   contract. Render approved themes directly; add `--allow-draft-theme` only
   when the selected theme is explicitly marked draft or review.

Learning Agent 0.4.0 is the approved Corporate Training Workshop default.
Material Ledger, Signal Pitch, and Open Frame 0.4.0 are the approved UX Brand
Case Study theme family; Material Ledger is the default. The six legacy bundled
themes remain draft and must not be described as approved. All themes share the
Allen Presentation Design System contract while keeping independent visual
expression.

Theme selection compares existing expressions. Theme creation or a major visual
redesign is a different workflow: read `allen-frame-method.md`, render three
controlled routes, and record the resulting direction and review before adding a
new gallery candidate.

## Scenario defaults

| Scenario | Default | Alternatives |
|---|---|---|
| Product Roadmap Review | Signal Grid | Executive Night, Evidence Ledger |
| Industry Research Deck | Evidence Ledger | Executive Night, Signal Grid |
| Speech Pitch Deck | Stage Contrast | Executive Night, Artifact Editorial |
| UX Brand Case Study | Material Ledger | Signal Pitch, Open Frame |
| Corporate Training Workshop | Learning Agent | Learning Canvas, Artifact Editorial |
