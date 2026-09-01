---
name: corporate-training-workshop
description: Plan and render corporate training and workshop presentations as web decks or native editable PPTX around a verified performance need, observable learning outcomes, adult-learning principles, practice, feedback, transfer to work, facilitation, and evaluation. Use for instructor-led training, leadership workshops, capability building, onboarding workshops, or applied internal courses. Do not use when the problem is not trainable or when only a passive announcement deck is needed.
license: MIT
metadata:
  owner: "allenxie"
  category: "presentation"
  maturity: "stable"
  risk: "local-write"
  version: "0.6.0"
  origin: "personal"
  visibility: "public"
  public_url: "https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/corporate-training-workshop"
  compatibility: "Planning is tool-neutral; bundled PyYAML/jsonschema runtime renders self-contained HTML. Native PPTX mode requires a compatible editable-PPTX renderer."
---

# Corporate Training Workshop

Design an experience that helps adults perform differently at work. Slides are
only one part of the workshop; activities, practice, feedback, facilitation, job
aids, and transfer support are first-class outputs.

## Current release

Version 0.6.0 retains native editable-PPTX production, a validated Learning Agent
PPTX profile, asset-first documentary image handling, explicit cross-slide
cadence, render-based quality gates, and a repaired 12-slide OPC system-thinking
reference package. The Learning Agent native PPTX profile is approved by Allen
Xie for final delivery. Its revised international-team photo system preserves cast,
office, clothing, light, role agency, meaningful work artifacts, and slot-safe
crops across six images. The OPC example and its photographs are disclosed synthetic
concept material, not evidence of a real client or measured outcome.
It adds Silent Spectrum 0.3.0 as a complete ten-slide web template with explicit
outcomes, protected practice time, worked example, high-density activity brief,
debrief, evaluation, action plan, and transfer commitment.

## Confirm training is the right intervention

Identify the performance gap, target learners, current capability, work context,
desired behavior, business result, sponsor, constraints, duration, delivery
mode, prerequisites, accessibility needs, and evaluation plan. If the gap is
caused mainly by incentives, process, tools, staffing, or authority, say so and
do not disguise the non-training problem as a course.

Read [references/scenario.yaml](references/scenario.yaml) before planning. Read
[references/expert-patterns.md](references/expert-patterns.md) for needs
analysis, objectives, adult learning, practice, transfer, and evaluation. Read
[references/slide-grammar.md](references/slide-grammar.md) for activity and
instructional visual mapping.

## Choose the operating mode

Identify the mode before making slides. Read
[references/generalization-testing.md](references/generalization-testing.md)
when the user asks how to invoke the Skill, requests three design directions,
or wants to test a direction with a real project.

1. **Generate with an existing theme** — use when the user selects a bundled
   theme or asks for a workshop deck without requesting a new visual language.
   Show the three recommended theme previews only when a theme still needs to
   be selected. Then generate the complete workshop. Do not run a new
   three-route design exploration by default.
2. **Explore three FRAME directions** — use when the user explicitly asks for
   Allen FRAME, three visibly different directions, a new theme, or a major
   redesign; also use it when high-fidelity references are supplied but the
   visual premise is genuinely unresolved. Read
   [references/allen-frame-method.md](references/allen-frame-method.md). Keep
   content, assets, canvas, and evidence constant; render a clarity baseline,
   context translation, and authored leap. Stop after representative frames
   and wait for the user to select or mix directions. Do not silently continue
   to the full deck or describe an agent choice as user-approved.
3. **Test generalization with a real project** — use only when the user asks for
   a real-project test, generalization test, transfer test, or stress test.
   Freeze the candidate direction, replace the concept content with supplied
   real evidence, and render the five stress frames defined in the testing
   guide before completing the deck. Keep the baseline pass isolated from the
   official theme and do not add design rules slide by slide to hide failures.

The three existing theme previews and the three FRAME directions are different
decisions. Theme previews choose among already bundled systems; FRAME directions
create or substantially redesign a system.

## Design backward from performance

1. Define observable workplace behavior and success evidence.
2. Write measurable learning outcomes and prerequisite knowledge.
3. Sequence relevance, model, demonstration, guided practice, feedback,
   independent application, reflection, and commitment.
4. Allocate time explicitly; protect practice and debrief time before adding
   more content.
5. Give every activity an objective, instructions, timebox, materials, output,
   debrief questions, and facilitator fallback.
6. Build assessment into the workshop and plan delayed transfer evidence.
7. Separate participant slides, facilitator notes, job aids, and evaluation
   instruments.

## Generate the web deck

When the user asks for an actual presentation, read
[references/allen-design-system.md](references/allen-design-system.md) and
[references/web-deck-generation.md](references/web-deck-generation.md). Create
schema-valid Presentation IR that moves through performance need, observable
outcomes, model, worked example, activity brief, practice, feedback, assessment,
transfer, and commitment. Put facilitator detail in notes rather than crowding
participant-facing slides.

Read `references/theme-selection.md` and `references/themes/index.yaml`, compare
the three real-render previews in `assets/theme-previews/`, then default to
Learning Agent; offer Silent Spectrum for an editorial workshop with dense
activity and transfer pages, Learning Canvas for simpler facilitation, and
Artifact Editorial for reflective work. Render with
`python scripts/render-html.py <deck>.ir.yaml --design
references/allen-signal-grid.yaml --output <deck>.html
--allow-draft-design --theme references/themes/learning-agent/theme.yaml`, then
open and inspect every slide. Repair the IR and
render again if anything is clipped, crowded, unclear during facilitation, or
visually repetitive.

To use the complete Silent Spectrum workshop, copy
`fixtures/silent-spectrum.ir.yaml`, replace the performance need and evidence,
then render with `--theme references/themes/silent-spectrum/theme.yaml`. Keep
facilitator timing, fallback, and recovery prompts in notes.

The HTML supports navigation, inline text refinement, facilitator notes,
download, and print/PDF. It does not automatically write browser edits back into
the IR.

## Generate a native PPTX

When the user requests an editable PowerPoint, read
[references/native-pptx-generation.md](references/native-pptx-generation.md).
Validate the native profile, preflight all evidence and image slots before layout,
and use a compatible PPTX renderer. Keep participant content, facilitator notes,
sources, and disclosures distinct. Use the bundled OPC reference only to learn
the Learning Agent constraints and cadence; never reuse its project facts or
synthetic people as evidence.

Render every slide after the final edit. Inspect both a contact sheet and every
slide full size, then run programmatic overflow and boundary checks. Repair
internal overlap, weak hierarchy, unexpected wrapping, repeated silhouettes,
font substitution, arbitrary crops, clipped in-image labels, and blank or
decorative work artifacts even when no outside-bound warning exists.

## Output contract

Return the needs diagnosis, learner profile, observable outcomes, agenda with
timing, learning arc, slide plan, activity briefs, facilitator notes, job aids,
assessment plan, transfer plan, evaluation plan, accessibility notes, known
non-training dependencies, schema-valid Presentation IR, and an actual
self-contained HTML deck or native editable PPTX when requested and a compatible
renderer is available.

Before release, use an environment with the dependencies declared in
`scripts/requirements.txt`, then run `python scripts/validate.py`. If dependency
installation is not authorized, report validation as not run rather than imply
that the Skill itself failed. Use
[evals/evals.json](evals/evals.json) when revising and turn real facilitation or
transfer failures into regression cases.

## Guardrails

- Do not promise behavior or business results from attendance alone.
- Do not use learner satisfaction as the only effectiveness measure.
- Do not invent learner needs, assessment results, or workplace transfer.
- Do not overload slides and then remove practice to fit the timebox.
- Provide accessible alternatives for activities, media, and participation.
- Brand constraints cannot make instructions or assessment unreadable.
