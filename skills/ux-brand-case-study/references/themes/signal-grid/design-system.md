# Signal Grid 0.5.0 design system

Signal Grid is an editorial operating-review system for product decisions. It
translates evidence, trade-offs, commitment, and uncertainty into a small number
of unmistakable signals. It is not a generic card dashboard and it must not be
used to make weak evidence look decisive.

Status: `draft`. The supplied visual reference informed composition, spacing,
contrast, and typographic attitude only. Do not copy its content, imagery, exact
palette, or layout mechanically.

## 1. Intent and boundary

- Primary job: help product and executive teams approve, change, stop, or
  sequence work.
- Voice: authored, direct, progressive, evidence-led, never futuristic for its
  own sake.
- Energy: one forceful assertion followed by calm evidence.
- Density: medium-high overall, but every slide keeps one dominant reading path.
- Avoid: ceremonial decks, decorative portfolios, generic startup gradients,
  glassmorphism, soft 3D icons, fake dashboards, and symmetrical card walls.

## 2. Foundation

### Canvas and grid

- Author at 1920 × 1080. Use a 12-column grid with 24 px gutters.
- Normal safe area: 64 px top and bottom, 64 px left and right. Text starts at
  104 px inside a large panel.
- The dominant panel may occupy 5–7 columns; supporting evidence occupies the
  remaining columns. Do not split a slide into equal thirds unless the evidence
  is genuinely equal.
- Use an 8 px base rhythm. Preferred steps: 8, 16, 24, 32, 48, 64, 96, 128.
- Panel radius: 28–36 px. Small chips: fully rounded. Do not mix more than two
  radius families on one slide.
- Shadows are normally absent. Separation comes from surface, spacing, and a
  one-pixel rule; a soft shadow is allowed only for a floating interaction layer.

### Color roles

| Role | Value | Use |
|---|---|---|
| Canvas | `#F4F4F6` | cool neutral breathing space |
| Surface | `#FFFFFF` | evidence and metric modules |
| Ink | `#0D0E10` | assertions, numbers, decisive labels |
| Muted ink | `#666871` | methods, periods, owners, sources |
| Signal Lime | `#B9F227` | recommendation, gate, next action; max 12% of a slide |
| Structure Violet | `#5C63E8` | committed structure, benchmark, selected series |
| Risk Orange | `#D84A2F` | decline, unresolved risk, or stop signal |
| Positive | `#12805C` | verified improvement, never aspiration |

Never communicate status by color alone. Pair every signal with a word, value,
direction, or pattern. A slide normally uses only one saturated signal color;
the others remain small semantic annotations.

### Typography

- Display: embed the unmodified Smiley Sans 2.0.1 (`得意黑`) WOFF2 supplied in
  `assets/fonts/`. It is licensed under SIL OFL 1.1; keep
  `assets/fonts/OFL-1.1.txt` with every redistributed theme pack. Use it only for
  short display titles, never body copy. The renderer must inline it as a data
  URL so exported HTML remains self-contained and offline-safe.
- Hero: 88–104 px, regular Smiley Sans, line height 1.04–1.10, tracking between
  -0.01 and -0.025 em, two to four short lines.
- Slide assertion: 48–60 px, line height 1.08–1.14. A minimum 12 px optical gap
  must remain between Chinese line boxes after visual inspection.
- Body: 24–30 px, line height 1.35–1.5, maximum 55 Latin characters or 30 CJK
  characters per line.
- Metric: 84–132 px with tabular numerals when available.
- Caption/source: 16–18 px. Never shrink evidence text to make an overloaded
  slide fit.
- Use sentence case for prose. Uppercase is reserved for short navigation,
  status, and evidence labels.
- Align title, context, interpretation, owner, and source to one of the authored
  panel baselines; near-alignment within 2–12 px is a defect, not visual nuance.

### Image behavior

- Use imagery only when it is evidence, context, or an intentional emotional
  reset. Do not add decorative AI imagery to operating reviews.
- Prefer documentary workplace/product imagery, interface crops, customer
  environments, or authored abstract fields. Avoid handshakes, glowing brains,
  generic robots, floating UI, and over-smoothed people.
- Crop decisively to 4:3, 3:2, or a tall evidence rail. Use a 28–36 px radius
  when the image is a panel; use square corners for annotated artifacts.
- Captions state what the image proves, not what it depicts.
- Every image object sets `fit` and an explicit, visually inspected `position`;
  renderer-default centering is not an authored crop.
- Use an image rhythm across a short sequence rather than filling every page:
  the NOVA Flow preview uses `1 / 0 / 2` image slots for context, analytical
  pause, and decision evidence.
- A cover image slot may occupy 35–42% of the canvas width. Repeated evidence
  slots share an exact left edge and width, with a 24 px gap on the 8 px rhythm.
- Generated concept imagery must be labeled as synthetic, keep provenance beside
  the assets, and never be presented as a real customer or research session.

For asset qualification, crop inspection, disclosure, and delivery checks, read
[image-realism-qa.md](image-realism-qa.md). The bundled NOVA Flow asset manifest
lives at `gallery/assets/nova-flow/SOURCES.md` in `presentation-core` and at
`assets/nova-flow/SOURCES.md` in the standalone Product Roadmap Review Skill.

## 3. Product-roadmap components

### Outcome scorecard

- One dominant metric carries the decision signal; one or two supporting
  metrics provide context.
- Each card includes definition, period/cohort, direction, and source. Label an
  output metric explicitly so it cannot be mistaken for an outcome.
- Do not use three equal KPI cards when one metric is decision-critical.

### Now / Next / Later

- Use one horizontal evidence rule with three unequal commitment zones.
- `Now` requires owner, capacity, and dependency confidence. `Next` names the
  opportunity and next evidence. `Later` describes an outcome direction, not a
  promised feature or date.
- Mark decision gates with Signal Lime and uncertainty with text or a dashed
  rule, never by fading content until it becomes unreadable.

### Opportunity and trade-off views

- Opportunity nodes must cite recurring evidence; solution nodes remain
  visually subordinate until assumptions are tested.
- A trade-off matrix shows criteria before rank. Highlight only the recommended
  option and state the displaced work directly beside it.

### Dependency and risk views

- Dependencies show owner, dependency type, earliest decision point, and
  consequence of delay. Arrows are semantic, not decorative.
- Risks show likelihood, impact, leading signal, owner, and mitigation. Do not
  use red/amber/green dots without labels.

### Decision close

- Use a large statement panel and no more than two decision modules.
- State allocation or action, stopped/displaced work, owner, next evidence, and
  review date. Signal Lime means a decision to make or execute, never generic
  emphasis.

## 4. Archetype grammar

| Grammar | Preferred composition |
|---|---|
| Cover | 7-column assertion + 5-column authored signal field |
| Evidence/data | 5-column interpretation panel + asymmetric metric field |
| Timeline | full-width rule with three commitment zones and visible gates |
| Comparison | explicit criteria rail + two or three unequal option surfaces |
| Process/causality | left-to-right evidence chain with one highlighted gate |
| Image-led | 5-column interpretation + 7-column evidence image or artifact |
| Closing | large decision panel + one or two execution modules |

## 5. Industry adaptations

- SaaS and growth products: activation, cohort retention, expansion, and quality
  metrics include definition, cohort, period, and instrumentation caveat.
- Enterprise/platform products: emphasize dependency ownership, migration or
  adoption gates, enablement, and cross-team sequencing.
- AI products: pair adoption with task success, quality, latency, cost, safety,
  and evaluation coverage; never present model usage alone as value.
- Hardware or regulated products: replace vague Now/Next/Later confidence with
  evidence gates for supply, certification, clinical/compliance, or reliability.
- Consumer products: show behavior and retention by cohort; do not substitute
  downloads, impressions, or feature count for durable value.

## 6. Motion, accessibility, and quality bar

- Motion reveals assertion, evidence, then implication in 180–260 ms steps.
  Reduced-motion mode shows the complete final state.
- Minimum body 24 px; minimum source 16 px; target WCAG AA contrast.
- Reading order follows the visual order. Every chart uses direct labels and
  every signal has a non-color cue.
- Reject a render if it contains clipped text, equal-weight card repetition,
  more than two competing focal points, unexplained decorative gradients,
  an action signal unsupported by evidence, an unqualified stock image, a
  generated scene without disclosure, or a default-centered crop that weakens
  the subject.
