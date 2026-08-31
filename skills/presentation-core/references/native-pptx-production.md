# Native PPTX production contract

Use this contract when the requested deliverable is an editable `.pptx`. It is
renderer-neutral: the canonical Presentation IR still owns narrative and
semantics, while a compatible PPTX renderer owns native shapes, images, notes,
and file export.

## Route the format before layout

1. Confirm whether the deliverable is HTML, PDF, or editable PPTX before choosing
   layouts. A supplied corporate template takes precedence over bundled profiles.
2. For native PPTX, select a schema-valid profile from
   `fixtures/native-pptx-profiles/` and record a layout ID, energy, silhouette,
   density, and image slots for every slide.
3. If no compatible editable-PPTX renderer is available, do not approximate the
   deliverable or claim success. Return the validated IR or HTML projection and
   disclose the missing renderer.

## Preflight assets before composition

- Inventory every image, logo, chart, table, diagram, and source before laying
  out slides. Mark each item `verified`, `synthetic`, `placeholder`, or `missing`.
- Fill evidence-bearing image slots with authorized real assets first. Generated
  images may illustrate a disclosed concept, but must not masquerade as a client,
  user, interface, quote, or measured result.
- Every image requires alt text, fit mode, crop or focal position, provenance, and
  disclosure status. Keep recurring people, rooms, daylight, materials, and
  photographic language continuous when a concept series is generated.
- Write a cast-and-place bible before generating a recurring team. Preserve
  recognizable identities while varying role, pose, camera distance, and
  low-saturation clothing. When the brief calls for an international team,
  express it through credible cultural diversity, workplace details, and equal
  professional agency rather than tokenistic casting or matching dark suits.
- Generate for the destination slot aspect ratio and safe zone. A landscape
  source is not acceptable for a tall slot when `cover` would cut a face,
  diagram, label, or evidence object. Render the final slot crop, not only the
  uncropped source image, before approval.
- Apply semantic artifact density: every visible sticky note, card, board label,
  worksheet, sketch, and screen must support the slide claim or work activity.
  Remove blank or decorative notes, unrelated symbols, gibberish, invented UI,
  and labels that become incomplete after crop.
- Define the crop at the slot, not by manually dragging an image after layout.
  Never stretch, distort, or use an arbitrary decorative crop.

## Compose for room-scale reading

- Use a 12-column grid. On a 1280 × 720 renderer canvas, keep at least 64 px from
  the edge, at least 24 px between major regions, and align repeated anchors to a
  4 px tolerance.
- Recommended minimums on that canvas are 66 px deck title, 46 px slide title,
  32 px mid-level heading, 21 px body, and 14 px caption. Title line height is
  1.04–1.12; body line height is 1.30–1.50.
- Do not shrink text to solve overflow. Shorten copy, change the archetype, split
  the slide, or move facilitation detail into speaker notes.
- Avoid orphan punctuation, unexpected one-word wraps, and visually equal title,
  body, and caption levels. Verify Chinese font substitution in the exported file.

## Author cross-slide rhythm

Assign each slide one energy level and one silhouette:

- `quiet`: orientation, reflection, or a single idea with generous negative space;
- `working`: comparison, model, process, evidence, or structured practice;
- `peak`: a decisive image, activity launch, reveal, or commitment.

Do not repeat the same energy or silhouette more than twice without a documented
narrative reason. Alternate image-led, type-led, diagram-led, and activity-led
frames according to the storyline rather than rotating arbitrary templates.

## Keep the deck natively editable

- Use native text, vector shapes, tables, and charts when practical. Do not flatten
  a full slide into one image.
- Encode recurring layouts, type styles, colors, spacing, and image slots as named
  profile/layout rules instead of page-specific coordinates.
- Put sources, disclosures, and facilitator detail in speaker notes. Every slide
  with external or generated assets must contain a `[Sources]` block.

## Release gates

Release only after all of the following pass:

1. render every slide to an image;
2. inspect a contact sheet for narrative rhythm and repeated silhouettes;
3. inspect every slide full size for internal collisions, edge overflow, font
   substitution, wrap errors, crop integrity, complete in-image labels, and
   meaningless or empty work artifacts;
4. run programmatic outside-bounds and overflow checks;
5. verify notes, source disclosures, and editable object structure;
6. re-render after the final change and repeat the affected checks.

An absence of outside-bound warnings is not proof of visual quality. Internal
overlap, poor hierarchy, bad cropping, repetition, and unreadable room-scale text
must be checked visually.
