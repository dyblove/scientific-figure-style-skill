---
name: scientific-figure-style
description: Design, analyze, and implement high-density Nature/Science-style scientific figures using a curated reference gallery of multi-panel research graphics. Use when Codex needs to create, critique, or revise publication figures, SDG/climate/energy/water maps, multi-panel layouts, palettes, legends, panel roles, or figure templates based on the user's preferred scientific visualization style.
---

# Scientific Figure Style

## Core Rule

Design figures as a scientific argument, not as isolated charts. Prefer one or two dominant main panels that carry the finding, surrounded by smaller satellite panels that explain, validate, decompose, or contextualize the main result.

Before drawing a new scientific figure, create a figure contract and get confirmation. A figure contract states the core claim, first-read panel, panel roles, chart forms, layout skeleton, palette, required data, and export plan. This prevents aesthetic polishing from hiding weak scientific logic.

## Scientific Data Integrity

Every research figure must be rendered from data or from calculations that are traceable to data. Do not invent values, spatial patterns, rankings, uncertainty, labels, or relationships to make a figure look complete.

- Before plotting, identify the raw data files, fields, units, spatial keys, temporal keys, and scenario keys used by every panel.
- Derive plotting tables through explicit calculations, such as aggregation, population weighting, normalization, Gini/Lorenz computation, trend fitting, or scenario comparison.
- Keep decorative style separate from empirical content. Palettes, layout, typography, and reference-inspired grammar may be borrowed; data marks must come from the user's data or from clearly documented calculations.
- If a requested panel cannot be supported by available data, report the missing fields and either omit the panel, replace it with a supported analysis, or mark it explicitly as a synthetic demonstration.
- If synthetic data is used only to test a layout, state that clearly in the output and do not present the result as a scientific finding.

## Workflow

1. Decide whether the task is a new figure, a revision of an approved figure, a code/debug task, or a reference replication task.
2. For a new figure, prepare a `references/figure-contract.md` style contract before plotting. Include recommended chart type(s), alternatives, layout skeleton, palette, data fields, and export plan. Ask the user to confirm before implementation.
3. Classify the figure grammar first, not by topic. Decide whether it is a map-dominant figure, scenario dashboard, small-multiple matrix, trend-plus-diagnostics layout, distribution diagnosis, sensitivity figure, or image plate.
4. Use `references/chart-atlas.md` to choose panel-level chart forms. For multi-panel figures, also select a layout template from `references/layout-templates.md`.
5. Search `references/gallery-annotations.md`, `references/gallery-index.jsonl`, and `references/gallery-scan-manifest.json` for 3-5 references that match both chart grammar and narrative role.
6. Build a data provenance plan: map every intended panel to raw fields and derived plotting tables before rendering.
7. If the user asks to imitate a reference, use replication mode instead of the new-figure contract: measure canvas, panel boxes, legend positions, scale behavior, palette, and typography before drawing.
8. If the user confirms the contract, implement with data-derived marks only.
9. Select colors from `references/palette-system.md`; keep variable-color mappings consistent across all panels.
10. Check extracted style preferences in `references/source-preferences.md`.
11. If using or expanding the user's local gallery, run `scripts/scan_gallery.py` to refresh thumbnails and palette metadata.
12. Before finalizing, apply `references/figure-checklist.md` and export SVG/PDF/PNG when feasible.

## Reference Retrieval Protocol

When designing a new figure, always build a reference shortlist in this order:

1. Same chart grammar.
2. Same panel role in the narrative.
3. Same layout family.
4. Same palette behavior.
5. Same level of density.

Use the gallery notes to find 3-5 similar examples. Do not rely on file names alone. If one reference is visually close but narratively different, keep it as a secondary reference, not the lead.

## Required Output For New Figures

When responding to a figure-design task, output a figure contract and wait for confirmation before implementation unless the user explicitly says to skip planning. Include:

1. Core claim.
2. First-read panel and evidence hierarchy.
3. Panel-by-panel logic table.
4. Recommended chart type plus alternatives for key panels.
5. Recommended layout skeleton.
6. Recommended palette and visual emphasis strategy.
7. Required data fields and derived calculations.
8. R / Python implementation route.
9. Similarities and differences versus the closest references.
10. Export plan, preferably SVG + PDF + PNG.

## Panel Grammar

- Use `main_panel` for the central map, paired maps, main trajectory, or principal comparison. It should usually occupy 40-65% of the canvas.
- Use `satellite_panel` for small plots that directly answer why, where, who, how much, or under which scenario.
- Use `diagnostic_panel` for Lorenz curves, boxplots, violins, marginal distributions, uncertainty ribbons, or sensitivity tests.
- Use `explanation_panel` for scatter/regression/quadrant plots using GDP, income group, scenario, region, or technology type.
- Use `summary_panel` for compact ranking bars, stacked bars, total-value bars, or headline numbers.

Every panel must have a role. If a panel cannot be named with one of these roles, remove it or merge it.

## Layout Defaults

- Prefer wide journal figures with a clear visual hierarchy.
- For spatial studies, make the main map large and use small charts around it, not the reverse.
- For two-system comparisons, use paired maps or paired main plots with identical scales and mirrored supporting panels.
- For scenario studies, use small multiples ordered consistently by time, scenario severity, region, or policy pathway.
- For SDG/system figures, group panels by domain using subtle section labels or icon strips, then repeat a simple line-chart grammar inside each group.
- Align axes across repeated panels; repeated structure is what keeps high information density from becoming clutter.
- For hard multi-panel layouts, lock the canvas aspect ratio and measured axes boxes before styling internal marks.
- Treat row gutters, panel labels, colorbars, legends, and axis labels as first-class layout objects; overlaps or cropped labels are failures, not minor polish issues.

## Styling Defaults

- Use a white background, pale gridlines, thin axes, and generous inner whitespace.
- Use bold lowercase panel letters. Keep panel titles short and data-facing.
- Put units in axis labels and colorbars. Do not leave units only in captions.
- Prefer direct labels on lines, areas, countries, or regions when this removes legend lookups.
- Use compact horizontal colorbars for maps. Use local legends inside empty map space or next to the related panel.
- Use saturation to encode importance: pale fills for context, medium saturation for data, strong color only for highlights.
- Use semi-open axes for short dense summary bands when full borders would compete with labels.
- Keep labels small but complete: every axis, colorbar, threshold, and derived metric needs units or definitions visible at publication scale.

## Replication Mode

When the user asks to "copy", "replicate", "match", or "follow the example", preserve the visible grammar first:

- Lock the output canvas to the reference aspect ratio before placing panels.
- Measure each visible panel as normalized coordinates `[x0, y0, width, height]` on the reference canvas.
- Record panel aspect ratios, gutters, baselines, and colorbar/legend boxes before drawing internal marks.
- Keep the same panel proportions and relative spacing.
- Keep the same main-panel dominance.
- Keep map projection, aspect, and legend placement close to the reference.
- Keep the same axis density, title style, and annotation style.
- Keep the same palette roles, but adapt exact values if data semantics demand it.

Only generalize after replication is stable.

## Reference Measurement Protocol

For hard replicas, build the figure skeleton before styling:

1. Determine the reference image width, height, and aspect ratio.
2. Draw or estimate bounding boxes for every panel, legend, colorbar, inset, and major annotation.
3. Convert boxes to normalized figure coordinates so they can be used directly with `fig.add_axes`.
4. Group boxes into named rows and columns, such as `top_map`, `left_top`, `right_top`, `summary_strip`, and `scatter_left`.
5. Match main-panel and satellite-panel aspect ratios before plotting internal data.
6. Only after the skeleton matches, tune internal map projection, point density, lines, labels, legends, and palettes.

If the skeleton is wrong, do not compensate by changing data marks. Fix the canvas ratio and panel boxes first.

## SVG-First Export

When implementing figures, prefer editable vector output:

- Save `*.svg` whenever the figure is mostly vector marks.
- Save `*.pdf` for publication/vector sharing.
- Save high-resolution `*.png` for fast visual inspection.
- If raster layers are unavoidable, such as official icons, image plates, or bitmap maps, keep the raster source high-resolution and document it.
- Inspect exported files, not only notebook previews.

## Resources

- `references/gallery-annotations.md`: human-readable image-by-image notes and tags.
- `references/gallery-scan-manifest.json`: latest scanned gallery manifest with dimensions, aspect ratios, and dominant palettes.
- `references/gallery-contact-sheet.jpg`: latest contact sheet for quick visual review of the scanned gallery.
- `references/figure-contract.md`: mandatory planning template for new figures before implementation.
- `references/chart-atlas.md`: panel-level chart grammar atlas for bars, lines, maps, scatters, distributions, heatmaps, glyphs, and image plates.
- `references/preference-checklist.md`: overall aesthetic, panel hierarchy, legend, palette, typography, and Gini rules.
- `references/replication-benchmarks.md`: hard-reference replication tests and concrete lessons from benchmark attempts.
- `references/source-preferences.md`: extracted user taste and narrative principles from the 34-image corpus.
- `references/layout-templates.md`: reusable multi-panel figure templates.
- `references/palette-system.md`: color systems and palette rules.
- `references/usage-guide.md`: operational guidance for when to use the skill and how to structure requests.
- `references/gallery-index.jsonl`: searchable image-level annotations for the local corpus.
- `references/figure-checklist.md`: final design audit.
- `scripts/scan_gallery.py`: generate contact sheets and palette metadata from a folder of reference figures.
