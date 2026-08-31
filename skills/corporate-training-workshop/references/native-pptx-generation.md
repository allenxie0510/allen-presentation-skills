# Native PPTX generation for workshops

Use this path when the requested deliverable is an editable `.pptx`, not only an
HTML deck. Keep the workshop diagnosis, observable outcomes, practice, feedback,
assessment, and transfer logic unchanged; change only the rendering contract.

## Required route

1. Confirm the delivery room, aspect ratio, template or brand file, editable
   requirements, and whether facilitator notes must travel with the deck.
2. Validate `fixtures/native-pptx-profiles/learning-agent.yaml` against
   `schemas/native-pptx-profile.schema.json`. A supplied corporate template wins
   over this profile, but not over readability, truth, or accessibility.
3. Build a content-and-asset manifest before layout. A photo, screenshot, chart,
   diagram, or deliberate negative-space treatment must fill every evidence slot.
4. Use authorized real project photos first. If concept images are generated,
   keep people, rooms, clothing palette, materials, light, and camera language
   continuous and disclose them in notes and the source list.
   For an international team, define recurring identities, role agency, varied
   low-saturation clothing, and credible workplace context before generating.
   Diversity must be structurally visible in participation, not added as a
   token cast checklist.
5. Use native text, shapes, tables, and charts so the output remains editable.
   Never flatten an entire slide to a screenshot.
6. Generate each image for its actual slide-slot ratio and focal safe zone. Check
   the rendered `cover` crop; regenerate or change the crop if a person, board,
   label, or evidence object is clipped.
7. Every visible note, card, whiteboard label, worksheet, diagram, or screen must
   support the workshop task. Remove blank notes, decorative paper, gibberish,
   unrelated symbols, invented UI, and labels that become incomplete after crop.

## Workshop cadence

Map the learning arc to three energy levels:

- `quiet`: relevance, reflection, orientation, or a single assertion;
- `working`: model, worked example, comparison, practice instructions, or review;
- `peak`: activity launch, decisive documentary image, reveal, or commitment.

Do not repeat an energy or page silhouette more than twice without a learning
reason. A useful sequence alternates human context, model, application, feedback,
and transfer rather than repeating left-copy/right-image pages.

Each activity slide must expose the task, timebox, output, success standard, and
debrief cue at room scale. Put facilitator fallback and detailed instructions in
speaker notes.

## Fidelity reference

`assets/examples/opc-system-thinking-0.5.1/` is a disclosed concept adaptation
that demonstrates Learning Agent in native PPTX: documentary image slots, varied
silhouettes, restrained cobalt/lime coding, Chinese open-source typography,
speaker-note sources, and a quiet–working–peak rhythm. Use it to learn constraints,
not to reuse its claims, people, project name, or page-specific content.

## Hard release gates

- Render every slide after the final edit.
- Inspect a contact sheet for pacing and repeated silhouettes.
- Inspect every slide full size for internal overlap, edge overflow, unexpected
  wrapping, orphan punctuation, font substitution, crop continuity, and room
  readability.
- Inspect every visible in-image label and work artifact after the final crop;
  fail the image when text is clipped, unrelated, blank, or decorative.
- Run programmatic overflow and outside-bounds checks.
- Verify every slide has a `[Sources]` speaker-note block and every synthetic
  asset is explicitly disclosed.
- Do not claim native PPTX completion if a compatible editable-PPTX renderer is
  unavailable; return the validated IR or HTML output and state the limitation.
