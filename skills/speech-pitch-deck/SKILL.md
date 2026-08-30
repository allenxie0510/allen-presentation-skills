---
name: speech-pitch-deck
description: Plan and render keynote, conference talk, investor pitch, and business roadshow web presentations around a memorable idea, audience belief shift, credible proof, spoken delivery, and explicit next action. Use when a presenter must persuade, inspire, secure a follow-up, or make an idea memorable. Do not use for a read-only report, routine status update, or document-style information archive.
license: MIT
metadata:
  owner: "allenxie"
  category: "presentation"
  maturity: "draft"
  risk: "local-write"
  version: "0.2.0"
  origin: "personal"
  visibility: "public"
  public_url: "https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/speech-pitch-deck"
  compatibility: "Planning is tool-neutral; the bundled PyYAML/jsonschema renderer produces a fixed-stage, self-contained HTML deck with navigation, inline text editing, speaker notes, download, and print/PDF support."
---

# Speech Pitch Deck

Design for a live speaker and a specific audience response. Slides support the
spoken argument; they are not the transcript.

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

Use [references/allen-signal-grid.yaml](references/allen-signal-grid.yaml) as the
bundled draft design system unless the user supplies a brand system. Render with
`python scripts/render-html.py <deck>.ir.yaml --design
references/allen-signal-grid.yaml --output <deck>.html
--allow-draft-design`, then open and inspect every slide. Repair the IR and
render again if anything is clipped, crowded, under-supported, or visually flat.

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

- Do not fabricate traction, customer quotes, market facts, credentials, or
  scientific claims.
- Do not use personal stories as proof for a general factual claim.
- Do not bury the proposition or ask behind a long biography or agenda.
- Do not put the spoken script on slides.
- Preserve brand constraints without reducing legibility, contrast, or proof.
