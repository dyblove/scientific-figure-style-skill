# Usage Guide

Use this skill when creating, revising, critiquing, or replicating high-density scientific figures based on the user's preferred Nature/Science-style gallery.

## When To Use

- Multi-panel publication figures.
- SDG, climate, energy, water, equity, scenario, or spatial analysis figures.
- Map-dominant figures with trend, inequality, or socioeconomic diagnostics.
- Figure critique: layout, palette, typography, legends, label collisions, or scientific rigor.
- Reference imitation: copying the visual grammar of a chosen gallery figure without copying its data or unique content.

Do not use this skill for decorative illustrations, posters, slide covers, or figures without a data basis unless the task is explicitly a layout mockup.

## Required User Inputs

For real research plotting, request or identify:

- Raw data files and formats.
- Spatial keys: country ISO, region, grid cell, latitude/longitude, geometry.
- Temporal keys: year, period, baseline, projection horizon.
- Scenario keys: SSP, policy, pathway, model, experiment, or intervention.
- Metrics and units.
- Weighting fields, such as population or GDP, if using weighted indices or inequality metrics.
- Desired claim or narrative: what the figure should prove.

If a requested panel has no supporting data, report the missing data and propose a supported alternative.

## Standard Workflow

1. Start with a figure contract for new plotting tasks. Do not jump into code until the contract is approved.
2. Classify the figure grammar: map-dominant, paired maps, trend-plus-diagnostics, scenario matrix, distribution diagnosis, SDG section matrix, image plate, or bubble-scatter explanation.
3. Select panel-level chart forms from `chart-atlas.md`.
4. Retrieve 3-5 references from `gallery-annotations.md`, `gallery-index.jsonl`, and `gallery-scan-manifest.json` by chart grammar first, then by narrative role.
5. Build a data provenance table mapping each panel to raw fields and derived calculations.
6. Choose a layout template from `layout-templates.md`.
7. Define the figure skeleton: canvas aspect ratio, named panel boxes, row gutters, legend boxes, and colorbar boxes.
8. Define the font hierarchy and label placement before final plotting.
9. Render data-derived marks only.
10. Export SVG/PDF/PNG when feasible and inspect final files for label cropping, row collisions, colorbar collisions, and unreadable text.
11. Report any synthetic, placeholder, or unsupported elements explicitly.

## Figure Contract First

When the user asks to draw a figure, first provide a structured contract:

1. Core claim.
2. First-read panel.
3. Panel role table.
4. Recommended chart type for each panel and alternative options.
5. Layout skeleton.
6. Palette and visual hierarchy.
7. Required data fields and calculations.
8. Implementation route in Python or R.
9. Export plan.

End by asking for confirmation. After confirmation, keep the approved layout and style stable unless the user explicitly requests a change.

For a single-panel figure, still use a compact contract: claim, chart form, alternatives, data fields, encoding, export.

## Replication Branch

If the user provides a reference image and asks to imitate, follow replication mode:

1. Measure or estimate canvas aspect ratio.
2. Identify every panel, legend, colorbar, inset, and title box.
3. Convert panel positions to normalized coordinates.
4. Match visual hierarchy, row/column alignment, axis density, palette behavior, and typography before changing content.
5. Only after the skeleton matches, replace data marks with the user's data.

Replication mode still requires data integrity: copy grammar, not values.

## Reference Use Rules

Borrow:

- Palette behavior.
- Layout grammar.
- Main/satellite panel hierarchy.
- Legend and colorbar placement.
- Typography hierarchy.
- Expression logic.

Do not copy:

- Original data values.
- Original image assets.
- Unique icons or artwork.
- Full composition when the new research question needs a different grammar.

## Typography Baseline

Use a fixed hierarchy and protect it with layout:

- Panel letters: 14-16 pt, bold.
- Panel titles: 9-10 pt.
- Axis labels and legend titles: 8-9 pt.
- Tick labels and local legends: 7-8 pt.
- Internal annotations: 7-8 pt.

If text is unreadable or collides, change the panel box, gutter, legend position, or label selection. Do not solve layout collisions by shrinking text below readable size.

## Output For A New Figure Plan

Return the figure contract:

1. Core claim and first-read panel.
2. Recommended chart type and alternatives.
3. Recommended layout.
4. Recommended palette and visual emphasis.
5. What each panel should show and why.
6. Required data fields.
7. R / Python implementation route.
8. Similarities and differences versus closest references.
9. Data gaps or unsupported requested elements.
10. Confirmation request.

## Output For Implementation

When implementing code:

- Keep input paths and output paths explicit.
- Use structured calculations to create plotting tables.
- Name panel boxes and row groups in code.
- Use shared constants for palette, font sizes, line widths, and grid styles.
- Save SVG first when feasible, plus PDF and high-resolution PNG for inspection.
- Open or inspect the exported image before finalizing.

## Minimum Usability Bar

A figure made with this skill is not complete until:

- Every panel has a narrative role.
- Every data mark is traceable to data or documented calculation.
- Main panels dominate visually.
- Satellite panels are readable and close to what they explain.
- Units are visible on axes and colorbars.
- Font hierarchy is consistent.
- Legends and labels do not overlap data or neighboring panels.
- The exported image has no cropped text.
