# Operating modes and real-project generalization testing

Use this guide to route a request before rendering. The goal is to prevent a
theme-selection step, a design-direction study, and a generalization test from
being treated as the same workflow merely because each can show multiple
previews.

## Three distinct modes

| Mode | Use when | Main output | Stop point |
|---|---|---|---|
| Existing-theme generation | The user selected a bundled theme or only needs a finished workshop | Complete, validated workshop deck | After full render and QA |
| FRAME direction exploration | The user asks for Allen FRAME, three directions, a new theme, or a major visual redesign | Three controlled routes using the same content and assets | After representative frames; wait for selection |
| Real-project generalization test | The user asks whether a route or theme transfers to a real project | Five stress frames and a Keep / Break / Adapt report | Before full-deck production |

The three recommended theme previews compare systems that already exist. The
three FRAME routes create a new system or substantially redesign one. Never run
both rounds automatically. If an existing theme is already selected, proceed
directly unless the user explicitly asks to redesign it.

## What generalization means

A presentation system generalizes when its reasoning and visual grammar survive
new, truthful content without recreating layouts page by page. Test five kinds
of transfer:

1. **Instructional transfer** — performance need, outcomes, practice, feedback,
   transfer, and evaluation still form a coherent learning experience.
2. **Narrative transfer** — the system works for a different topic, audience,
   and level of content complexity.
3. **Visual transfer** — the same tokens, image rules, component families, and
   cadence support both sparse and dense pages.
4. **Evidence integrity** — real artifacts, claims, limitations, and sources fit
   without invention or decorative substitution.
5. **Facilitation transfer** — instructions, timeboxes, outputs, debriefs, and
   room-distance legibility remain usable by a facilitator.

One real project is a pilot, not proof of universal generalization. Choose a
first project that differs materially from the concept used to create the
direction. For Learning Agent, a real manager-feedback, safety, customer-service,
operations, or onboarding workshop is more informative than another AI course.

## Minimum real-project input package

Do not begin the visual test from a topic sentence alone. Ask for or derive a
normalized brief containing:

- organization and project name, which may be anonymized;
- target roles, current behavior, desired workplace behavior, and business
  context;
- duration, venue, audience size, facilitation format, and accessibility needs;
- authoritative source documents and the owner of the subject matter;
- one real task, incident, decision, conversation, or case learners must handle;
- observable learning criteria and any available baseline or transfer evidence;
- brand assets, approved terminology, actual workplace artifacts, and image-use
  permissions;
- facts that are confidential, uncertain, synthetic, or forbidden to invent.

Missing data must be marked as missing. A redacted real artifact is preferable
to a polished fictional claim.

## Baseline protocol

1. **Freeze the candidate.** Record theme or route ID, version, status, tokens,
   components, image rules, and the exact files under test. Do not overwrite the
   official theme.
2. **Normalize the real brief.** Build an evidence ledger and replace every
   concept-project claim, person, metric, image, and artifact. Do not reuse
   sample evidence simply because it fits the layout.
3. **Hold the system constant.** On the first pass, do not add new visual rules
   or one-off layout code. Content-specific substitutions are allowed; design
   exceptions are recorded as failures.
4. **Render five stress frames.** Use the same candidate for:
   - relevance or cover: sparse, emotionally legible, and project-specific;
   - model or structure: dense enough to test hierarchy and explanation;
   - activity brief: objective, time, steps, output, and fallback;
   - evidence or assessment: data, criteria, source, and limitation;
   - transfer or close: owner, workplace action, evidence, and review moment.
5. **Inspect at two scales.** Review each frame full size for craft and at
   contact-sheet scale for hierarchy, variety, and cross-slide rhythm.
6. **Classify every failure.** Do not repair until it is labeled:
   - content substitution — expected project-specific replacement, not a
     generalization failure;
   - parameter or slot gap — the system needs a reusable token, component, image
     slot, or rule;
   - conceptual mismatch — the direction's governing metaphor does not belong
     to the new scenario.
7. **Run one adaptation pass.** Add only reusable changes justified by the
   failures. Re-render the same five frames and record what changed.
8. **Request human review.** The facilitator or project owner confirms content,
   room usability, and brand fit before the candidate becomes approved or is
   expanded into the full deck.

## Pass and return criteria

The candidate passes the pilot only when:

- all Allen FRAME hard gates pass;
- the five required page types render without clipping, broken assets, or
  unreadable room-distance text;
- every activity exposes objective, timebox, steps, output, and debrief or
  fallback;
- no claims, results, testimonials, people, or workplace artifacts are invented;
- the five-lens weighted score is at least 85 and no lens is below 8;
- no more than one of the five frames requires a new structural exception after
  the adaptation pass.

Two structural exceptions mean **adapt and retest**. Three or more mean **return
to the design system or choose another route** rather than polishing individual
slides. A visually attractive result that needs repeated page-specific fixes has
not generalized.

## Required test deliverables

Return:

1. normalized real-project brief and evidence ledger;
2. candidate ID, version, status, and frozen-file manifest;
3. five baseline stress frames and one contact sheet;
4. hard-gate results and five-lens review;
5. a **Keep / Break / Adapt** table;
6. the adapted frames, change log, and remaining risks;
7. human decision: approve, adapt again, select another route, or stop.

The Learning Agent exploration under
`assets/explorations/learning-agent/` is an example of a FRAME route study, not
proof of generalization and not an approved theme while its selection remains
`pending`.

## Copy-paste invocation prompts

### Generate directly with an existing theme

```text
使用 $corporate-training-workshop，把我提供的真实项目资料制作成完整 Workshop。
已选主题：[主题 ID]，不要再做三个视觉方向。
请先核实绩效需求、学习目标、练习、评估与迁移设计，再生成并检查完整网页演示。
```

### Trigger three FRAME directions

```text
使用 $corporate-training-workshop，按 Allen FRAME 为这个项目探索新的视觉方向。
请固定同一组内容、证据、图片和画布，分别渲染：清晰基线、场景转译、原创跃迁。
每个方向只先做封面、推理/结构页、练习/人物页；暂不完成整套模板。
等我选择或混合方向后，再形成设计系统和完整演示。
```

### Test a candidate with a real project

```text
使用 $corporate-training-workshop，对 [候选主题或方向 ID + 版本] 做真实项目泛化测试。
项目资料见：[文件或目录]。
请冻结候选系统，不覆盖正式主题；第一轮不新增页面专属样式。
先核实真实项目输入包，并渲染封面、结构、活动、证据/评估、迁移/结尾五类压力页。
请区分内容替换、参数/槽位缺口和概念不匹配，输出 Keep / Break / Adapt 报告。
未通过前不要制作完整演示，也不要虚构缺失资料。
```

For a publishable test record, replace bracketed values with exact file paths,
route IDs, versions, and named reviewers. Preserve the user's approval language
verbatim in the design-direction record.
