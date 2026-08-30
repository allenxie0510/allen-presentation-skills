# Signal Grid image realism QA

Use this checklist whenever Signal Grid contains photography, a product
artifact, or a generated concept scene. It protects evidence quality and visual
credibility; it is not a requirement to add an image to every slide.

## 1. Truth and provenance

- Classify each asset as user-provided, externally sourced, or synthetic.
- Keep a `SOURCES.md` beside the assets. Record the original URL for external
  material and the generation workflow for synthetic material.
- Disclose synthetic projects and illustrative values on the visible preview.
- Never imply that a generated person is a real customer, employee, or research
  participant.

## 2. Narrative role

Each image must perform one job: establish context, show evidence, explain an
artifact, or reset emotion between dense sections. Remove images whose only job
is to fill a rectangle. A caption says what the image supports, not merely what
objects appear in it.

## 3. Source qualification

- Prefer user project evidence, then properly sourced documentary photography,
  then synthetic imagery for clearly labeled concept previews.
- Reject visible anatomy defects, plastic skin, repeated people, impossible
  reflections, malformed devices, illegible fake UI, embedded logos, and
  accidental text.
- Keep one coherent visual world per sequence: people, wardrobe, location,
  light, material palette, contrast, and grain should agree.
- Minimum source size for the gallery preview is 1000 × 800 px.

## 4. Authored crop

- Set `fit: cover` and an explicit `position` on every photographic image object.
- Inspect faces, hands, laptops, and evidence cards after the final 16:9 crop.
- Keep the subject clear of rounded corners, captions, page numbers, and panel
  boundaries. Do not solve a weak crop by darkening the entire photo.
- Use a 28–36 px panel radius and the same radius family within a slide.

## 5. Rhythm and alignment

- Alternate image-led and analytical pages when the storyline benefits from a
  pause. The NOVA Flow three-page preview intentionally uses `1 / 0 / 2` images.
- Repeated horizontal evidence wells share the exact baseline and height. Use a
  24 px inter-slot gap and keep outer panel margins on the 8 px grid.
- A cover photo occupies 50–60% of the slide width in the selected Operational
  Documentary direction; evidence images must remain
  large enough to inspect rather than becoming decorative thumbnails.

## 6. Automated gallery gate

`scripts/build-presentation-theme-gallery.mjs` rejects the NOVA Flow render when:

- the three-slide image rhythm is not `1 / 0 / 2`;
- any image lacks alt text, explicit crop position, or minimum source resolution;
- the closing evidence slots do not share a baseline and height or their gap is
  not 24 px;
- the cover image does not occupy its authored slot; or
- the synthetic concept disclosure is missing.

Automation cannot judge facial realism, hand anatomy, photographic taste, or
whether the crop feels intentional. Inspect the three rendered screenshots at
full size and as a contact sheet before publishing.
