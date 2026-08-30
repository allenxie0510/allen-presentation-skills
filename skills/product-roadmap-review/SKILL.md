---
name: product-roadmap-review
description: Plan and render product review and roadmap web presentations around outcomes, customer opportunities, evidence, trade-offs, sequencing, dependencies, and explicit leadership decisions. Use for quarterly product reviews, roadmap reviews, portfolio prioritization, or roadmap reset discussions. Do not use for a feature release announcement or a delivery status list that requires no prioritization decision.
license: MIT
metadata:
  owner: "allenxie"
  category: "presentation"
  maturity: "draft"
  risk: "local-write"
  version: "0.2.0"
  origin: "personal"
  visibility: "public"
  public_url: "https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/product-roadmap-review"
  compatibility: "Planning is tool-neutral; the bundled PyYAML/jsonschema renderer produces a fixed-stage, self-contained HTML deck with navigation, inline text editing, notes, download, and print/PDF support."
---

# Product Roadmap Review

Make product leadership decisions visible. Treat a roadmap as a set of outcome,
opportunity, evidence, and sequencing choices under uncertainty—not as a feature
calendar.

## Establish the decision job

Identify the review horizon, audience, product or portfolio boundary, desired
business and product outcomes, decisions required in the meeting, and what is
genuinely committed. Ask only for missing inputs that could change a priority,
sequence, or recommendation.

Read [references/scenario.yaml](references/scenario.yaml) before planning the
deck. For roadmap methods, evidence rules, terminology, and storyline patterns,
read [references/expert-patterns.md](references/expert-patterns.md). For each
reasoning-to-visual choice, read
[references/slide-grammar.md](references/slide-grammar.md).

## Build the argument

1. State the outcome and decision frame, including horizon and constraints.
2. Separate shipped outputs from observed outcomes and learning.
3. Connect customer opportunities to evidence; never invent opportunity nodes
   from unverified intuition.
4. Show candidate choices and evaluation criteria before presenting priority.
5. Express uncertainty honestly: use Now / Next / Later unless dates are backed
   by capacity, dependency, and confidence evidence.
6. Surface cross-team dependencies, risks, capacity trade-offs, and what will not
   be done.
7. End with named decisions, owners, next evidence, and review dates.

Every substantive slide needs an assertion or audience job. Prefer one coherent
decision path over a backlog tour.

## Generate the web deck

When the user asks for an actual presentation, read
[references/allen-design-system.md](references/allen-design-system.md) and
[references/web-deck-generation.md](references/web-deck-generation.md). Then:

1. Create schema-valid Presentation IR using an outcome scorecard, opportunity
   evidence, trade-off comparison, confidence-aware Now / Next / Later sequence,
   dependency map, and explicit decision close where the evidence supports them.
2. Use [references/allen-signal-grid.yaml](references/allen-signal-grid.yaml) as
   the bundled draft design system unless the user supplies a brand system.
3. Render with `python scripts/render-html.py <deck>.ir.yaml --design
   references/allen-signal-grid.yaml --output <deck>.html
   --allow-draft-design`.
4. Open and inspect every slide. Repair the IR and render again if anything is
   clipped, crowded, ambiguous, or visually repetitive.

The HTML supports navigation, inline text refinement, notes, download, and
print/PDF. It does not produce native PPTX or automatically write browser edits
back into the IR.

## Output contract

Produce:

1. normalized review brief and decision questions;
2. outcome, opportunity, evidence, and constraint inventory;
3. assertion-led storyline;
4. slide plan with grammar, archetype, evidence, and decision role;
5. explicit assumptions, gaps, and confidence labels;
6. schema-valid Presentation IR and an actual self-contained HTML deck when a
   rendered presentation is requested;
7. a post-use failure note suitable for the next version.

Do not claim that an editable HTML deck exists unless it has actually been
rendered and checked. Use [evals/evals.json](evals/evals.json) when changing the
workflow. Before release, use an environment with the dependencies declared in
`scripts/requirements.txt`, then run `python scripts/validate.py`. If dependency
installation is not authorized, report validation as not run rather than imply
that the Skill itself failed.

## Guardrails

- Do not equate roadmap items, velocity, or output volume with customer or
  business outcomes.
- Do not imply date certainty for discovery work.
- Do not hide deprioritized work, assumptions, or conflicting evidence.
- Do not disclose confidential customer data, unreleased strategy, or personal
  information in examples.
- Brand rules affect expression, never the product evidence or priority logic.
