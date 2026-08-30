---
name: ux-brand-case-study
description: Plan and render UX and brand case-study web presentations that show the challenge, role, evidence, reasoning, iterations, system decisions, applications, outcomes, and honest attribution. Use for portfolio reviews, client case studies, design awards, internal impact reviews, or design leadership presentations. Do not use for a visual moodboard, image gallery, or confidential work that cannot be disclosed safely.
license: MIT
metadata:
  owner: "allenxie"
  category: "presentation"
  maturity: "draft"
  risk: "local-write"
  version: "0.3.0"
  origin: "personal"
  visibility: "public"
  public_url: "https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/ux-brand-case-study"
  compatibility: "Visual examples require permitted image access; the bundled PyYAML/jsonschema renderer produces a fixed-stage, self-contained HTML deck with navigation, inline text editing, notes, download, and print/PDF support."
---

# Ux Brand Case Study

Show why a design decision was made, how it was tested or applied, and what
changed. A case study is evidence of judgment and impact, not a gallery of final
screens or identity assets.

## Establish the case-study job

Identify audience, desired decision, project type, business and user context,
the presenter’s role, collaborators, constraints, available artifacts, evidence,
outcomes, and disclosure limits. Choose UX, brand, or combined mode.

Read [references/scenario.yaml](references/scenario.yaml) before planning. Read
[references/expert-patterns.md](references/expert-patterns.md) for case logic,
attribution, impact, UX and brand patterns, and disclosure. Read
[references/slide-grammar.md](references/slide-grammar.md) for reasoning-to-visual
mapping.

## Construct the case

1. State the challenge, stakes, audience, constraints, role, and success criteria.
2. Show only the research and diagnosis that changed a decision.
3. Connect insight to strategy, design principles, alternatives, and trade-offs.
4. Use iterations to show learning—not a linear process-theater timeline.
5. Present the resulting experience or brand as a coherent system across
   relevant touchpoints.
6. Compare before/after behavior or expression using fair evidence.
7. Report outcomes with attribution limits, then reflect on what changed or
   remains unresolved.

## Generate the web deck

When the user asks for an actual presentation, read
[references/allen-design-system.md](references/allen-design-system.md) and
[references/web-deck-generation.md](references/web-deck-generation.md). Create
schema-valid Presentation IR that moves through challenge, role, evidence,
consequential iterations, system decisions, annotated artifacts, fair comparison,
outcomes, attribution, and reflection. Use only permitted images; embed local
assets so the result remains self-contained.

Read `references/theme-selection.md` and `references/themes/index.yaml`, compare
the three real-render previews in `assets/theme-previews/`, then default to
Artifact Editorial; offer Signal Grid and Stage Contrast when their fit is stronger. Render with
`python scripts/render-html.py <deck>.ir.yaml --design
references/allen-signal-grid.yaml --output <deck>.html
--allow-draft-design --theme references/themes/artifact-editorial/theme.yaml
--allow-draft-theme`, then open and inspect every slide. Repair the IR and
render again if anything is clipped, crowded, weakly annotated, or visually
repetitive.

The HTML supports navigation, inline text refinement, notes, download, and
print/PDF. It does not produce native PPTX or automatically write browser edits
back into the IR.

## Output contract

Return the normalized case brief, audience decision, disclosure plan, role and
collaboration statement, evidence ledger, storyline, slide plan, artifact list,
outcome and attribution table, redaction notes, reflection, schema-valid
Presentation IR, and an actual self-contained HTML deck when a rendered
presentation is requested and permitted assets exist.

Before release, use an environment with the dependencies declared in
`scripts/requirements.txt`, then run `python scripts/validate.py`. If dependency
installation is not authorized, report validation as not run rather than imply
that the Skill itself failed. Use
[evals/evals.json](evals/evals.json) when revising and convert repeated real-world
failures into versioned regression cases.

## Guardrails

- Never claim team work, research, or business impact as the presenter’s sole work.
- Never invent research findings, quotes, metrics, awards, or client approval.
- Redact personal data, confidential strategy, unreleased work, and NDA material.
- Do not reveal proprietary research artifacts merely to make the case look rich.
- Brand restrictions govern presentation expression; the case must still expose
  process, evidence, and limitations.
