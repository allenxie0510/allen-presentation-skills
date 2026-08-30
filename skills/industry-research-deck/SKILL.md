---
name: industry-research-deck
description: Research, plan, and render decision-oriented industry web presentations with explicit market definitions, source quality, sizing ranges, structural analysis, competitive dynamics, uncertainty, and strategic implications. Use for market-entry research, sector scans, competitive landscapes, investment theses, or executive industry briefings. Do not use for a simple company profile or unsourced trend summary.
license: MIT
metadata:
  owner: "allenxie"
  category: "presentation"
  maturity: "draft"
  risk: "local-write"
  version: "0.3.0"
  origin: "personal"
  visibility: "public"
  public_url: "https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/industry-research-deck"
  compatibility: "Research planning is tool-neutral; live research requires source access; the bundled PyYAML/jsonschema renderer produces a fixed-stage, self-contained HTML deck with navigation, inline text editing, notes, download, and print/PDF support."
---

# Industry Research Deck

Produce a defensible view of an industry that supports a real decision. Define
the market and the evidence method before collecting attractive statistics.

## Establish the research decision

Identify the audience, decision, geography, time horizon, market boundary,
customer or value-chain scope, known hypotheses, and acceptable uncertainty.
Do not begin with a visual framework.

Read [references/scenario.yaml](references/scenario.yaml) before planning. Read
[references/expert-patterns.md](references/expert-patterns.md) for market-study
method, source hierarchy, sizing, structure, terminology, and uncertainty. Read
[references/slide-grammar.md](references/slide-grammar.md) when turning analysis
into slides.

## Conduct and structure the analysis

1. State the decision question, scope, definitions, exclusions, and as-of date.
2. Form testable hypotheses and specify evidence that could disconfirm them.
3. Build a source ledger before synthesis; prefer primary and official sources.
4. Triangulate market size, growth, and competition. Reconcile differing
   definitions instead of averaging incompatible numbers.
5. Analyze value creation, participants, customer segments, substitutes,
   barriers, regulation, economics, and change drivers.
6. Separate observed fact, estimate, interpretation, scenario, and recommendation.
7. Convert findings into implications, options, leading indicators, and named
   decisions—not a list of trends.

## Generate the web deck

When the user asks for an actual presentation, read
[references/allen-design-system.md](references/allen-design-system.md) and
[references/web-deck-generation.md](references/web-deck-generation.md). Build a
schema-valid Presentation IR whose sequence moves from scope and definition to
source ledger, sizing ranges, value chain or profit pool, competition, scenarios,
uncertainty, implications, and the decision. Keep sources and as-of dates visible
on the relevant slides.

Read `references/theme-selection.md` and `references/themes/index.yaml`, compare
the three real-render previews in `assets/theme-previews/`, then default to
Evidence Ledger; offer Executive Night and Signal Grid when their fit is stronger. Render with
`python scripts/render-html.py <deck>.ir.yaml --design
references/allen-signal-grid.yaml --output <deck>.html
--allow-draft-design --theme references/themes/evidence-ledger/theme.yaml
--allow-draft-theme`, then open and inspect every slide. Repair the IR and
render again if anything is clipped, crowded, misleading, or visually repetitive.

The HTML supports navigation, inline text refinement, notes, download, and
print/PDF. It does not produce native PPTX or automatically write browser edits
back into the IR.

## Output contract

Return the research brief, scope and definitions, hypothesis/evidence ledger,
source register, assertion-led storyline, slide plan, sizing model with ranges,
structural and competitive analysis, scenarios, implications, uncertainties,
appendix plan, schema-valid Presentation IR, and an actual self-contained HTML
deck when a rendered presentation is requested.

Before release, use an environment with the dependencies declared in
`scripts/requirements.txt`, then run `python scripts/validate.py`. If dependency
installation is not authorized, report validation as not run rather than imply
that the Skill itself failed. Use
[evals/evals.json](evals/evals.json) to capture regressions and add a new eval
whenever a real task exposes a repeatable failure.

## Guardrails

- Never fabricate market size, CAGR, quotes, shares, company data, or sources.
- Label source date, geography, currency, units, methodology, and confidence.
- Do not infer competition from concentration alone or one isolated measure.
- Do not disguise a vendor forecast as an observed fact.
- Do not expose licensed report content beyond permitted summaries.
- Brand and style cannot change the analytical conclusion.
