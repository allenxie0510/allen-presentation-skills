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

## 0.3.0 主题画廊

六套草稿主题已经接入同一套 Presentation IR 与 HTML 渲染器：Signal Grid
信号网格、Executive Night 董事会夜幕、Evidence Ledger 证据账本、Stage
Contrast 舞台对比、Artifact Editorial 作品集画册、Learning Canvas 学习画布。

[打开真实渲染主题画廊](skills/presentation-core/gallery/README.md)。画廊包含
5 个场景、15 组公平对比和 45 张 1920×1080 截图；每组都用同一份场景 IR
渲染封面、核心组件与收尾页，并非手工效果图。

可以把任一 Skill 目录链接直接发给支持 GitHub 读取的 AI，也可以克隆整个
仓库后从本地目录使用。每个场景 Skill 都自带网页渲染器、设计系统、Schema
和运行资源，不依赖私有仓库。

## 输出能力

- 根据行业、场景、听众与决策任务建立叙事结构；
- 生成经过 Schema 校验的 Presentation IR；
- 渲染固定 1920×1080、自包含的 HTML 网页幻灯片；
- 支持翻页、触控、演讲者备注、文字微调、保存和打印/PDF；
- 检查越界和可预估的文字溢出。
- 按场景推荐三套主题，并把场景组件映射为可执行 archetype 与 layout variant；
- 通过 `--theme <theme.yaml> --allow-draft-theme` 生成所选主题的网页幻灯片。

当前不生成原生 `.pptx`，浏览器编辑也不会自动同步回 Presentation IR。
内置 Allen Signal Grid 设计系统与六套 0.3.0 主题仍为 `draft`，不应被描述为
已批准品牌系统。

## 发布说明

本仓库由私有管理仓库通过白名单自动发布。公开仓库中的直接修改可能在下次
同步时被覆盖；建议通过 Issue 提交问题或建议。

## License

[MIT](LICENSE)
