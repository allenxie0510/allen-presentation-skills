# Learning Agent 0.4.0 reference workshop

This is the 15-slide release example for the approved `learning-agent` theme.
It is a synthetic concept project used to demonstrate narrative, facilitation,
image, component, and transfer behavior. It does not claim a real client,
deployed Agent, learner score, testimonial, or business impact.

Files:

- `learning-agent.ir.yaml` — canonical 15-slide Presentation IR;
- `photos/` — five continuity-controlled synthetic documentary assets;
- `previews/slide-01.webp` through `slide-15.webp` — inspected full-size frames;
- `previews/contact-sheet.webp` — deck-level rhythm review.

Render from the Skill directory:

```bash
python scripts/render-html.py \
  assets/examples/learning-agent-0.4.0/learning-agent.ir.yaml \
  --design references/allen-signal-grid.yaml \
  --theme references/themes/learning-agent/theme.yaml \
  --output learning-agent.html \
  --allow-draft-design
```

The underlying design-system foundation remains draft; the Learning Agent theme
and scenario Skill release are approved at 0.4.0. Replace concept content and
images with verified project evidence before external use.
