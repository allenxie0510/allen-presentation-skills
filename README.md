# Allen Presentation Skills

面向专业演示场景的一组公开 AI Skills。它们先判断沟通场景与决策任务，
再建立叙事架构、Presentation IR 和可在浏览器播放的网页幻灯片。

## Skills

- [Professional Presentation Core](skills/presentation-core/)
- [Product Roadmap Review](skills/product-roadmap-review/)
- [Industry Research Deck](skills/industry-research-deck/)
- [Speech Pitch Deck](skills/speech-pitch-deck/)
- [UX Brand Case Study](skills/ux-brand-case-study/)
- [Corporate Training Workshop](skills/corporate-training-workshop/)

## 直接交给 AI 使用

把本仓库地址或某个 Skill 目录链接发给能够读取公开 GitHub 仓库的 AI，并明确
要求它先读取对应的 `SKILL.md`。公开仓库地址：

`https://github.com/allenxie0510/allen-presentation-skills`

调用 Corporate Training Workshop 0.4.0 的推荐提示词：

```text
请读取并使用这个公开 GitHub Skill：
https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/corporate-training-workshop

先读取 SKILL.md，并按其中的相对链接继续读取本任务需要的 references、Schema、
主题和脚本。请使用 $corporate-training-workshop 0.4.0，把我提供的真实项目资料
制作成可主持、可练习、可评估和可迁移的网页 Workshop。

默认使用已批准的 Learning Agent 主题；不要自动重新做三个 FRAME 方向。
不要虚构需求、数据、人物、评价或项目成果。生成 Schema-valid Presentation IR，
渲染自包含 HTML，并逐页检查后再交付。

我的项目资料：[粘贴内容或提供文件]
```

调用 UX Brand Case Study 0.4.0 的推荐提示词：

```text
请读取并使用这个公开 GitHub Skill：
https://github.com/allenxie0510/allen-presentation-skills/tree/main/skills/ux-brand-case-study

先读取 SKILL.md，并按相对链接继续读取当前任务需要的 scenario、主题、Schema
和 art-direction。请沿“挑战与角色 → 证据 → 洞察 → 迭代 → 系统与应用 →
成效与反思”建立案例，不得虚构研究、用户引语、团队贡献或项目成果。

如果我没有指定主题，默认使用已批准的 Material Ledger；也可以让我从
Signal Pitch 和 Open Frame 中选择。生成 Schema-valid Presentation IR、
自包含 HTML，并逐页检查对齐、溢出、裁切、文字尺度和跨页疏密节奏。

我的项目资料：[粘贴内容或提供文件]
```

如果 AI 不支持读取 GitHub，它无法仅凭链接自动获得 Skill；此时先克隆仓库，
再把本地 `skills/corporate-training-workshop/` 目录提供给它。仓库根链接用于发现
全部 Skills，具体 Skill 目录链接最适合直接调用。

### 给正在读取本仓库的 AI

1. 根据用户场景选择一个 `skills/<name>/SKILL.md`，先读取该入口文件。
2. 只继续读取入口为当前模式链接的 references、Schema、主题与脚本。
3. 相对路径均以该 Skill 目录为根；不要依赖本仓库之外的私有文件。
4. 保留 Skill 的证据、许可、验证和“不虚构”边界。
5. 用户要求实际网页演示时，必须返回有效 IR、实际 HTML 和逐页检查结果，
   不能只返回大纲或假装执行了无法执行的渲染。

## Presentation Theme Gallery · 演示主题画廊

Learning Agent 已正式发布为已批准的 `0.4.0` 企业培训主题。Material Ledger、
Signal Pitch 和 Open Frame 已正式发布为 UX Brand Case Study `0.4.0` 主题族。
其余六套遗留主题仍为**草稿**。通用画廊按场景展示 15 组真实渲染结果；
每组依次为封面页、核心组件页和收尾页，并使用同一份场景 Presentation IR，
便于比较主题差异，而不是比较内容差异。

### Product Roadmap Review · 产品路线图评审

叙事路径：结果 → 机会证据 → 取舍 → 顺序与依赖 → 明确决策。

#### [Signal Grid · 信号网格](skills/presentation-core/themes/signal-grid/) · 默认主题

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/signal-grid-01-cover.webp" width="32.5%" alt="产品路线图评审，信号网格主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/signal-grid-02-core.webp" width="32.5%" alt="产品路线图评审，信号网格主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/signal-grid-03-closing.webp" width="32.5%" alt="产品路线图评审，信号网格主题，收尾页" />
</p>

> 灰白编辑网格、Signal Lime 行动信号与紫蓝结构，适合产品和经营判断。

#### [Executive Night · 董事会夜幕](skills/presentation-core/themes/executive-night/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/executive-night-01-cover.webp" width="32.5%" alt="产品路线图评审，董事会夜幕主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/executive-night-02-core.webp" width="32.5%" alt="产品路线图评审，董事会夜幕主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/executive-night-03-closing.webp" width="32.5%" alt="产品路线图评审，董事会夜幕主题，收尾页" />
</p>

> 深海军蓝、象牙白与低饱和金色，适合高层审批和正式战略沟通。

#### [Evidence Ledger · 证据账本](skills/presentation-core/themes/evidence-ledger/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/evidence-ledger-01-cover.webp" width="32.5%" alt="产品路线图评审，证据账本主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/evidence-ledger-02-core.webp" width="32.5%" alt="产品路线图评审，证据账本主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/product-roadmap-review/evidence-ledger-03-closing.webp" width="32.5%" alt="产品路线图评审，证据账本主题，收尾页" />
</p>

> 纸张底、墨色文字与钴蓝索引，强调定义、来源、范围和不确定性。

### Industry Research Deck · 行业研究演示

叙事路径：决策问题 → 市场定义 → 来源方法 → 规模与结构 → 情景 → 战略含义。

#### [Evidence Ledger · 证据账本](skills/presentation-core/themes/evidence-ledger/) · 默认主题

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/evidence-ledger-01-cover.webp" width="32.5%" alt="行业研究演示，证据账本主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/evidence-ledger-02-core.webp" width="32.5%" alt="行业研究演示，证据账本主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/evidence-ledger-03-closing.webp" width="32.5%" alt="行业研究演示，证据账本主题，收尾页" />
</p>

> 纸张底、墨色文字与钴蓝索引，强调定义、来源、范围和不确定性。

#### [Executive Night · 董事会夜幕](skills/presentation-core/themes/executive-night/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/executive-night-01-cover.webp" width="32.5%" alt="行业研究演示，董事会夜幕主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/executive-night-02-core.webp" width="32.5%" alt="行业研究演示，董事会夜幕主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/executive-night-03-closing.webp" width="32.5%" alt="行业研究演示，董事会夜幕主题，收尾页" />
</p>

> 深海军蓝、象牙白与低饱和金色，适合高层审批和正式战略沟通。

#### [Signal Grid · 信号网格](skills/presentation-core/themes/signal-grid/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/signal-grid-01-cover.webp" width="32.5%" alt="行业研究演示，信号网格主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/signal-grid-02-core.webp" width="32.5%" alt="行业研究演示，信号网格主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/industry-research-deck/signal-grid-03-closing.webp" width="32.5%" alt="行业研究演示，信号网格主题，收尾页" />
</p>

> 灰白编辑网格、Signal Lime 行动信号与紫蓝结构，适合产品和经营判断。

### Speech Pitch Deck · 演讲与路演

叙事路径：钩子 → 张力 → 主张 → 证明 → 未来状态 → 行动请求 → 回扣。

#### [Stage Contrast · 舞台对比](skills/presentation-core/themes/stage-contrast/) · 默认主题

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/stage-contrast-01-cover.webp" width="32.5%" alt="演讲与路演，舞台对比主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/stage-contrast-02-core.webp" width="32.5%" alt="演讲与路演，舞台对比主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/stage-contrast-03-closing.webp" width="32.5%" alt="演讲与路演，舞台对比主题，收尾页" />
</p>

> 深色舞台、大字号与强烈色块，为现场表达和记忆点服务。

#### [Executive Night · 董事会夜幕](skills/presentation-core/themes/executive-night/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/executive-night-01-cover.webp" width="32.5%" alt="演讲与路演，董事会夜幕主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/executive-night-02-core.webp" width="32.5%" alt="演讲与路演，董事会夜幕主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/executive-night-03-closing.webp" width="32.5%" alt="演讲与路演，董事会夜幕主题，收尾页" />
</p>

> 深海军蓝、象牙白与低饱和金色，适合高层审批和正式战略沟通。

#### [Artifact Editorial · 作品集画册](skills/presentation-core/themes/artifact-editorial/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/artifact-editorial-01-cover.webp" width="32.5%" alt="演讲与路演，作品集画册主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/artifact-editorial-02-core.webp" width="32.5%" alt="演讲与路演，作品集画册主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/speech-pitch-deck/artifact-editorial-03-closing.webp" width="32.5%" alt="演讲与路演，作品集画册主题，收尾页" />
</p>

> 暖纸色与编辑排版，让作品、研究证据和设计判断共同叙事。

### UX Brand Case Study · UX 与品牌案例

叙事路径：挑战与角色 → 证据 → 洞察 → 迭代 → 系统与应用 → 成效与反思。

#### [Material Ledger · 材质档案](skills/presentation-core/themes/material-ledger/) · 已批准默认主题 · 0.4.0

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/material-ledger-01-cover.webp" width="32.5%" alt="UX 与品牌案例，材质档案主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/material-ledger-02-core.webp" width="32.5%" alt="UX 与品牌案例，材质档案主题，系统与应用页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/material-ledger-03-closing.webp" width="32.5%" alt="UX 与品牌案例，材质档案主题，成效与反思页" />
</p>

> 暖纸色、档案编号、应用物证与编辑式尺度，适合可追溯的 UX 与品牌系统案例。

#### [Signal Pitch · 信号提案](skills/presentation-core/themes/signal-pitch/) · 已批准主题 · 0.4.0

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/signal-pitch-01-cover.webp" width="32.5%" alt="UX 与品牌案例，信号提案主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/signal-pitch-02-core.webp" width="32.5%" alt="UX 与品牌案例，信号提案主题，系统与应用页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/signal-pitch-03-closing.webp" width="32.5%" alt="UX 与品牌案例，信号提案主题，成效与反思页" />
</p>

> 无描边大圆角色块、高对比标题与单一酸性色，适合客户和设计领导快速判断。

#### [Open Frame · 开放画幅](skills/presentation-core/themes/open-frame/) · 已批准主题 · 0.4.0

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/open-frame-01-cover.webp" width="32.5%" alt="UX 与品牌案例，开放画幅主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/open-frame-02-core.webp" width="32.5%" alt="UX 与品牌案例，开放画幅主题，系统与应用页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/ux-brand-case-study/open-frame-03-closing.webp" width="32.5%" alt="UX 与品牌案例，开放画幅主题，成效与反思页" />
</p>

> 纪实大图、建筑感留白与尺度变化，适合作品集面试和设计奖项案例。

### Corporate Training Workshop · 企业培训与工作坊

叙事路径：绩效需要 → 可观察目标 → 模型 → 示例 → 练习反馈 → 评估与迁移。

#### [Learning Agent · 学习智能体](skills/corporate-training-workshop/references/themes/learning-agent/) · 已批准默认主题 · 0.4.0

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/corporate-training-workshop/assets/theme-previews/learning-agent-01-cover.webp" width="32.5%" alt="企业培训与工作坊，Learning Agent 主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/corporate-training-workshop/assets/theme-previews/learning-agent-02-core.webp" width="32.5%" alt="企业培训与工作坊，Learning Agent 主题，四步委托模型页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/corporate-training-workshop/assets/theme-previews/learning-agent-03-closing.webp" width="32.5%" alt="企业培训与工作坊，Learning Agent 主题，迁移承诺页" />
</p>

> 真实感办公纪实摄影、可验收的 Agent 委托模型与练习—反馈—迁移路径。包含
> [15页正式参考示例](skills/corporate-training-workshop/assets/examples/learning-agent-0.4.0/)
> 和完整图片来源记录；示例明确标注为概念项目。

<img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/corporate-training-workshop/assets/examples/learning-agent-0.4.0/previews/contact-sheet.webp" width="100%" alt="Learning Agent 0.4.0 十五页正式参考示例联系表" />

#### [Learning Canvas · 学习画布](skills/presentation-core/themes/learning-canvas/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/learning-canvas-01-cover.webp" width="32.5%" alt="企业培训与工作坊，学习画布主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/learning-canvas-02-core.webp" width="32.5%" alt="企业培训与工作坊，学习画布主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/learning-canvas-03-closing.webp" width="32.5%" alt="企业培训与工作坊，学习画布主题，收尾页" />
</p>

> 编号导轨、卡片化步骤与活动区，支持练习、反馈和迁移。

#### [Signal Grid · 信号网格](skills/presentation-core/themes/signal-grid/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/signal-grid-01-cover.webp" width="32.5%" alt="企业培训与工作坊，信号网格主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/signal-grid-02-core.webp" width="32.5%" alt="企业培训与工作坊，信号网格主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/signal-grid-03-closing.webp" width="32.5%" alt="企业培训与工作坊，信号网格主题，收尾页" />
</p>

> 灰白编辑网格、Signal Lime 行动信号与紫蓝结构，适合产品和经营判断。

#### [Artifact Editorial · 作品集画册](skills/presentation-core/themes/artifact-editorial/)

<p>
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/artifact-editorial-01-cover.webp" width="32.5%" alt="企业培训与工作坊，作品集画册主题，封面页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/artifact-editorial-02-core.webp" width="32.5%" alt="企业培训与工作坊，作品集画册主题，核心组件页" />
  <img src="https://raw.githubusercontent.com/allenxie0510/allen-presentation-skills/main/skills/presentation-core/gallery/previews/corporate-training-workshop/artifact-editorial-03-closing.webp" width="32.5%" alt="企业培训与工作坊，作品集画册主题，收尾页" />
</p>

> 暖纸色与编辑排版，让作品、研究证据和设计判断共同叙事。

[打开独立画廊索引](skills/presentation-core/gallery/README.md)，可继续查看主题元数据与
15 张三联对比图。当前画廊共包含 45 张 1920×1080 的真实渲染截图。

每个场景 Skill 都自带网页渲染器、设计系统、Schema 和运行资源，不依赖私有
仓库。能读取 GitHub 的 AI 可按本页顶部提示直接使用；其他环境可克隆后从本地
Skill 目录调用。

## 输出能力

- 根据行业、场景、听众与决策任务建立叙事结构；
- 生成经过 Schema 校验的 Presentation IR；
- 渲染固定 1920×1080、自包含的 HTML 网页幻灯片；
- 支持翻页、触控、演讲者备注、文字微调、保存和打印/PDF；
- 检查越界和可预估的文字溢出。
- 按场景推荐三套主题，并把场景组件映射为可执行 archetype 与 layout variant；
- 通过 `--theme <theme.yaml> --allow-draft-theme` 生成所选主题的网页幻灯片。

当前不生成原生 `.pptx`，浏览器编辑也不会自动同步回 Presentation IR。
底层 Allen Signal Grid 设计系统仍为 `draft`。Learning Agent 以及 UX Brand
Case Study 的三套 0.4.0 主题已通过真实渲染、硬性门槛和五维评审并获批准；
其余六套遗留主题仍为草稿。主题批准不代表概念示例中的客户、能力或成效为真。

## 发布说明

本仓库由私有管理仓库通过白名单自动发布。公开仓库中的直接修改可能在下次
同步时被覆盖；建议通过 Issue 提交问题或建议。

## License

[MIT](LICENSE)
