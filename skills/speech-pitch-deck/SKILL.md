---
name: speech-pitch-deck
description: Plan and render keynote, conference talk, investor pitch, and business roadshow web presentations around a memorable idea, audience belief shift, credible proof, spoken delivery, and explicit next action. Use when a presenter must persuade, inspire, secure a follow-up, or make an idea memorable. Do not use for a read-only report, routine status update, or document-style information archive.
license: MIT
metadata:
  owner: "allenxie"
  category: "presentation"
  maturity: "stable"
  risk: "local-write"
  version: "0.5.0"
  origin: "personal"
  visibility: "public"
  public_url: "https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/speech-pitch-deck"
  compatibility: "Planning is tool-neutral; the bundled PyYAML/jsonschema renderer produces a fixed-stage, self-contained HTML deck with navigation, inline text editing, speaker notes, download, and print/PDF support."
---

# Speech Pitch Deck

Design for a live speaker and a specific audience response. Slides support the
spoken argument; they are not the transcript.

## Current release

Version 0.5.0 retains the two
approved, designer-reviewed themes. Slope Trace is the default: it uses a
content-born progression rail, quiet/working/peak cadence, orthogonal data axes,
and documentary learning scenes. Night Relay is the alternative for stronger
live-stage contrast: dark mechanism peaks alternate with light evidence pages,
and blue-to-mint nodes show responsibility moving from Agent back to learner.
It also adds Silent Spectrum 0.3.0 as a complete ten-slide alternative, pairing
sparse stage peaks with a high-density proof ledger, objection handling, future
state, explicit ask, and closing callback.

The bundled AhaSlope example is a disclosed synthetic concept project. Its
international teenagers and young adults are AI-generated concept scenes, not
real users, a longitudinal cohort, or evidence of product or learning outcomes.

## Choose the mode

Identify audience, venue, duration, speaker, desired belief or action, available
proof, and rehearsal constraints. Select one primary mode:

- **Keynote / conference talk:** one defensible idea that changes perception.
- **Investor / business pitch:** a clear proposition and strongest facts that
  earn a next meeting, approval, adoption, or investment decision.

Read [references/scenario.yaml](references/scenario.yaml) before planning. Read
[references/expert-patterns.md](references/expert-patterns.md) for mode-specific
story structure, proof, spoken delivery, and fact-checking. Read
[references/slide-grammar.md](references/slide-grammar.md) for visual choices.

## Shape the talk

1. Write the audience shift as `from → to → so they will`.
2. Reduce the talk to one core idea and three to seven remembered points.
3. Establish tension, stakes, or a surprising observation quickly.
4. Alternate claims, concrete examples, demonstrations, and proof; identify
   unsupported claims before drafting slides.
5. Build spoken transitions and pacing. Give each slide one audience job.
6. Make the ask or action explicit and proportionate to the evidence.
7. Produce speaker notes, timing, and rehearsal checkpoints separately from
   audience-facing copy.

## Generate the web deck

When the user asks for an actual presentation, read
[references/allen-design-system.md](references/allen-design-system.md) and
[references/web-deck-generation.md](references/web-deck-generation.md). Create
schema-valid Presentation IR with larger type, fewer objects, tension-to-proof
pacing, a clear future state, speaker notes, and an explicit ask. Keep the spoken
script out of the audience-facing slides.

Read `references/theme-selection.md` and `references/themes/index.yaml`, compare
the two real-render previews in `assets/theme-previews/`, then default to Slope
Trace; offer Silent Spectrum when the talk needs stronger editorial contrast and
a room-readable proof ledger, or Night Relay when a live venue benefits from dark mechanism peaks
and a memorable human–Agent responsibility handoff. After selection, read the
theme's `preview.md`, `art-direction.md`, `theme.yaml`, and `theme.css`. Render with
`python scripts/render-html.py <deck>.ir.yaml --design
references/allen-signal-grid.yaml --output <deck>.html
--allow-draft-design --theme references/themes/slope-trace/theme.yaml`, then open
and inspect every slide. Repair the IR and
render again if anything is clipped, crowded, under-supported, or visually flat.

To start from the complete Silent Spectrum talk, copy
`fixtures/silent-spectrum.ir.yaml`, replace all proof-status placeholders, then
render with `--theme references/themes/silent-spectrum/theme.yaml`. Keep the
speaker notes separate from audience-facing copy.

The HTML supports navigation, inline text refinement, speaker notes, download,
and print/PDF. It does not produce native PPTX or automatically write browser
edits back into the IR.

## Output contract

Return the normalized speaking brief, mode and rationale, audience shift, core
idea, remembered points, evidence ledger, narrative beats, slide plan, speaker
notes plan, timing, explicit ask, fact-check gaps, rehearsal checklist,
schema-valid Presentation IR, and an actual self-contained HTML deck when a
rendered presentation is requested.

Before release, use an environment with the dependencies declared in
`scripts/requirements.txt`, then run `python scripts/validate.py`. If dependency
installation is not authorized, report validation as not run rather than imply
that the Skill itself failed. Use
[evals/evals.json](evals/evals.json) when changing behavior and convert real
failure patterns into regression cases.

## Guardrails

- On light canvases and light modules, use black/dark primary text or the
  dark-gray secondary token. White text requires a stable dark surface and at
  least 4.5:1 contrast; never use a crossing band or image crop as its only
  contrast support.
- Do not fabricate traction, customer quotes, market facts, credentials, or
  scientific claims.
- Do not use personal stories as proof for a general factual claim.
- Do not bury the proposition or ask behind a long biography or agenda.
- Do not put the spoken script on slides.
- Preserve brand constraints without reducing legibility, contrast, or proof.
