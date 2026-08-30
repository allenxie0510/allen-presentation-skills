# Presentation Theme Gallery

These previews are generated from real Presentation IR through the bundled HTML
renderer and Chromium. They are not mockups. Every scenario uses one three-slide
IR across its three recommended themes so visual selection does not accidentally
change the story or evidence.

Signal Grid is currently `0.4.1`; the other five draft themes remain `0.3.0`.

| Scenario | Default | Alternative 1 | Alternative 2 |
|---|---|---|---|
| Product Roadmap Review | [Signal Grid](previews/product-roadmap-review/signal-grid.webp) | [Executive Night](previews/product-roadmap-review/executive-night.webp) | [Evidence Ledger](previews/product-roadmap-review/evidence-ledger.webp) |
| Industry Research Deck | [Evidence Ledger](previews/industry-research-deck/evidence-ledger.webp) | [Executive Night](previews/industry-research-deck/executive-night.webp) | [Signal Grid](previews/industry-research-deck/signal-grid.webp) |
| Speech Pitch Deck | [Stage Contrast](previews/speech-pitch-deck/stage-contrast.webp) | [Executive Night](previews/speech-pitch-deck/executive-night.webp) | [Artifact Editorial](previews/speech-pitch-deck/artifact-editorial.webp) |
| UX Brand Case Study | [Artifact Editorial](previews/ux-brand-case-study/artifact-editorial.webp) | [Signal Grid](previews/ux-brand-case-study/signal-grid.webp) | [Stage Contrast](previews/ux-brand-case-study/stage-contrast.webp) |
| Corporate Training Workshop | [Learning Canvas](previews/corporate-training-workshop/learning-canvas.webp) | [Signal Grid](previews/corporate-training-workshop/signal-grid.webp) | [Artifact Editorial](previews/corporate-training-workshop/artifact-editorial.webp) |

Run `scripts/build-presentation-theme-gallery.mjs` from the repository root to
rebuild all 15 contact sheets and 45 individual screenshots after changing IR,
theme CSS, the base runtime, or the renderer.
