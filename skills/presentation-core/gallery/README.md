# Presentation Theme Gallery

These previews are generated from real Presentation IR through the bundled HTML
renderer and Chromium. They are not mockups. Every scenario uses one three-slide
IR across its three recommended themes so visual selection does not accidentally
change the story or evidence.

Material Ledger, Signal Pitch, and Open Frame are approved `0.4.0` UX Brand
Case Study themes; Material Ledger is the default. Learning Agent is the
approved Corporate Training Workshop theme. The six legacy themes remain draft.
Signal Grid's Product Roadmap preview uses the synthetic NOVA Flow concept project and a
theme-specific `1 / 0 / 2` documentary-image rhythm. See
`gallery/assets/nova-flow/SOURCES.md` for provenance.

| Scenario | Default | Alternative 1 | Alternative 2 |
|---|---|---|---|
| Product Roadmap Review | [Signal Grid](previews/product-roadmap-review/signal-grid.webp) | [Executive Night](previews/product-roadmap-review/executive-night.webp) | [Evidence Ledger](previews/product-roadmap-review/evidence-ledger.webp) |
| Industry Research Deck | [Evidence Ledger](previews/industry-research-deck/evidence-ledger.webp) | [Executive Night](previews/industry-research-deck/executive-night.webp) | [Signal Grid](previews/industry-research-deck/signal-grid.webp) |
| Speech Pitch Deck | [Stage Contrast](previews/speech-pitch-deck/stage-contrast.webp) | [Executive Night](previews/speech-pitch-deck/executive-night.webp) | [Artifact Editorial](previews/speech-pitch-deck/artifact-editorial.webp) |
| UX Brand Case Study | [Material Ledger](previews/ux-brand-case-study/material-ledger.webp) | [Signal Pitch](previews/ux-brand-case-study/signal-pitch.webp) | [Open Frame](previews/ux-brand-case-study/open-frame.webp) |
| Corporate Training Workshop | [Learning Canvas](previews/corporate-training-workshop/learning-canvas.webp) | [Signal Grid](previews/corporate-training-workshop/signal-grid.webp) | [Artifact Editorial](previews/corporate-training-workshop/artifact-editorial.webp) |

Run `scripts/build-presentation-theme-gallery.mjs` from the repository root to
rebuild all 15 contact sheets and 45 individual screenshots after changing IR,
theme CSS, the base runtime, or the renderer.
