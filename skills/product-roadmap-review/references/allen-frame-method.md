# Allen FRAME aesthetic-direction method

FRAME turns taste from an unexplained preference into a traceable design
decision. Use it when creating a theme, substantially redesigning a theme, or
when the visual direction is still ambiguous. Do not force the full exploration
loop for a typo fix, a mechanical resize, or a change inside an already approved
art direction.

The method was informed by studying how `huashu-design` combines design context,
real rendered alternatives, content-derived form, and failure-driven critique.
Its wording, presentation-specific gates, schemas, weights, and artifacts are
independently authored. Do not copy named studios, signature layouts, palettes,
or showcase code. Learn principles from verified work; do not imitate authorship.

## Standard formation

An aesthetic rule is admissible only when it records all five fields below.
Rules that state only a preferred look are taste claims, not standards.

1. **Source** — user context, verified project evidence, communication theory,
   a documented design precedent, or a demonstrated project failure.
2. **Intent** — the communication problem the rule solves.
3. **Observable signal** — what a reviewer can see in the rendered result.
4. **Failure case** — the predictable way the rule becomes generic, decorative,
   unreadable, dishonest, or over-applied.
5. **Override boundary** — the scenario, brand rule, evidence need, or user choice
   that legitimately supersedes it.

Use this evidence order when sources disagree:

1. user-provided brand system and real project artifacts;
2. truthful content and evidence requirements;
3. audience, venue, and scenario communication needs;
4. verified design precedents and domain literature;
5. curated heuristics and model judgment.

Never turn a single reference image, a popular designer, or a recent failure into
a universal law. Record the principle that transfers and the signature detail
that must not be copied.

## F — Foundation / design philosophy

Collect the design context before high-fidelity work: brand assets, existing
slides or product, real imagery, audience distance, venue, content density,
evidence status, and accessibility requirements. If context is missing, label
the result as a provisional concept rather than inventing brand truth.

Write one **concept thesis** that answers: “What does this design make visible
that belongs to this content?” Then define a content-born visual motif. A motif
may come from a workflow, artifact, physical behavior, data relationship, or
narrative tension. It must not be a generic symbol such as a glowing AI orb.

Apply the replaceability test: if client name, title, and logo can be changed and
the design still says exactly the same thing, the concept is too generic.

## R — Routes / design directions

For a new theme or major redesign, create three routes from the same normalized
brief, content, asset set, canvas, and evidence. Routes have different strategic
jobs:

- **Clarity baseline** — the most legible and disciplined answer; proves the
  content works without spectacle.
- **Context translation** — transfers principles from a verified, relevant
  design context without copying its signature expression.
- **Authored leap** — develops the content-born motif into a distinctive system.

Each route must change at least three of five structural axes: grid/composition,
typographic voice, image behavior, density/rhythm, and color/material behavior.
Changing only colors, fonts, or corner radii is a variation, not a direction.

Use `schemas/design-direction.schema.json`. Keep selection `pending` until real
frames exist. A user-provided reference narrows the exploration but does not
remove the obligation to test whether the reference works for evidence-heavy
and image-led pages.

## A — Artifacts / visual exploration

Do not ask users to choose from text labels or mood boards alone. Render the
same two or three representative frames for every route:

1. identity frame — normally the cover;
2. reasoning frame — the densest evidence, comparison, or data page;
3. human/context frame — image-led evidence, artifact, or closing decision.

Acquire content-required imagery before layout exploration. Every route uses the
same real or clearly disclosed synthetic assets so the comparison tests design,
not content quality. Present the routes together at both full size and contact-
sheet scale. Check slide-level hierarchy and deck-level rhythm separately.

For decks of five or more pages, do not scale a route to the whole deck until at
least one identity frame and one reasoning frame prove that its grammar survives
both low and high density.

## M — Mastering / art direction

After the user chooses a route, or after a design lead records a clearly labeled
provisional choice, write an art-direction contract containing:

- concept thesis and visual motif;
- composition and alignment logic;
- Chinese and Latin typography behavior;
- image slots, crop, focus, caption, and provenance rules;
- quiet, working, and peak slide cadence;
- component family and data behavior;
- scenario-specific expression changes;
- anti-patterns and legitimate overrides;
- the selected route, alternatives considered, and the exact approval language.

Do not call a direction user-approved when it was selected by an agent. Use
`provisional` until the user or named designer approves rendered evidence.
Design-system status remains `draft` until the review gate passes and a human
reviewer is recorded.

## E — Evaluation / self review

Evaluation has two layers. Hard gates run first; scoring cannot compensate for
their failure.

### Hard gates

- no overflow, collision, accidental crop, or broken asset;
- readable at the intended audience distance;
- facts, estimates, synthetic scenes, and sources are disclosed honestly;
- evidence-required imagery is present and images are not decorative filler;
- color is not the only carrier of meaning;
- source, font, and asset licenses remain distributable;
- full-size and contact-sheet screenshots have been inspected.

### Five expert lenses

| Lens | Weight | Reviewer question |
|---|---:|---|
| Philosophy and narrative fit | 20 | Does the visual form grow from this content and storyline? |
| Hierarchy and cross-slide rhythm | 25 | Is the reading path clear, and does the deck breathe, build, and peak deliberately? |
| Craft and system consistency | 20 | Are alignment, spacing, typography, crop, and components exact across pages? |
| Communication and evidence function | 20 | Does every visual choice improve understanding, comparison, judgment, or action? |
| Authorship and originality | 15 | Is there an unexpected but defensible expression that avoids template clichés? |

Score each lens from 0–10 and calculate a weighted score out of 100. A theme may
become an approval candidate only when every hard gate passes, the weighted score
is at least 85, and no lens is below 8. Scores from 75–84 require refinement;
lower scores return to Routes. Use `schemas/design-review.schema.json` and report
Keep, Fix, and three Quick Wins. Review the design, not the designer.

## Required artifacts by task size

| Task | Required FRAME artifacts |
|---|---|
| New theme or major redesign | validated direction record, real route frames, art-direction contract, validated review |
| New deck using an approved theme | context and concept thesis, chosen theme rationale, visual QA |
| New deck using a draft theme | context, provisional direction rationale, visual QA, draft disclosure |
| Minor edit inside an approved direction | affected hard gates and relevant expert lenses only |

The schemas make decisions auditable; they do not automate taste. A passing JSON
file is never evidence that the rendered design is good.
