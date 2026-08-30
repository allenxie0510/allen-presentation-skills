---
name: corporate-training-workshop
description: Plan and render corporate training and workshop web presentations around a verified performance need, observable learning outcomes, adult-learning principles, practice, feedback, transfer to work, facilitation, and evaluation. Use for instructor-led training, leadership workshops, capability building, onboarding workshops, or applied internal courses. Do not use when the problem is not trainable or when only a passive announcement deck is needed.
license: MIT
metadata:
  owner: "allenxie"
  category: "presentation"
  maturity: "draft"
  risk: "local-write"
  version: "0.2.0"
  origin: "personal"
  visibility: "public"
  public_url: "https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/corporate-training-workshop"
  compatibility: "Planning is tool-neutral; the bundled PyYAML/jsonschema renderer produces a fixed-stage, self-contained HTML deck with navigation, inline text editing, facilitator notes, download, and print/PDF support."
---

# Corporate Training Workshop

Design an experience that helps adults perform differently at work. Slides are
only one part of the workshop; activities, practice, feedback, facilitation, job
aids, and transfer support are first-class outputs.

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

Use [references/allen-signal-grid.yaml](references/allen-signal-grid.yaml) as the
bundled draft design system unless the user supplies a brand system. Render with
`python scripts/render-html.py <deck>.ir.yaml --design
references/allen-signal-grid.yaml --output <deck>.html
--allow-draft-design`, then open and inspect every slide. Repair the IR and
render again if anything is clipped, crowded, unclear during facilitation, or
visually repetitive.

The HTML supports navigation, inline text refinement, facilitator notes,
download, and print/PDF. It does not produce native PPTX or automatically write
browser edits back into the IR.

## Output contract

Return the needs diagnosis, learner profile, observable outcomes, agenda with
timing, learning arc, slide plan, activity briefs, facilitator notes, job aids,
assessment plan, transfer plan, evaluation plan, accessibility notes, known
non-training dependencies, schema-valid Presentation IR, and an actual
self-contained HTML deck when a rendered presentation is requested.

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
