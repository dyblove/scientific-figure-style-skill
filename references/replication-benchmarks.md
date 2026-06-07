# Replication Benchmarks

Use this file when validating whether the skill can imitate the user's hardest preferred figures. These are not general style notes; they are concrete replication lessons from synthetic-data benchmark attempts.

## Benchmark Set

The current benchmark script is `replicate_reference_figures.py` in the user's working directory. It creates synthetic approximations for five preferred reference grammars:

1. `replicate_01_pv_map_grid`: 3x3 global map matrix with inset box diagnostics and bottom bar/boxplot panels.
2. `replicate_02_paired_maps_diagnostics`: paired maps with Lorenz curves, latitude marginals, longitude profile, and total bars.
3. `replicate_03_trend_glyph_map`: top trend/decomposition strip plus large glyph map.
4. `replicate_04_central_map_satellites`: central resource map with country satellite profiles, global marginal profile, and bottom socioeconomic scatter panels.
5. `replicate_05_bars_scatter`: scenario stacked bars plus explanatory bubble scatter.

## Lessons From First Replication Pass

- Replication requires exact layout presets, not only verbal templates. Panel ratios and whitespace strongly affect perceived quality.
- Colorbars must be treated as first-class panels. If they overlap titles or map content, the result feels amateur even when the data layers are correct.
- Map matrices need compact vertical spacing and smaller map extents. Oversized maps with too much whitespace look less like journal figures.
- Paired-map references need all diagnostic satellites. A partial replica with only maps, Lorenz curves, and marginals is not enough if the source includes bottom ranked bars and GDP scatter panels.
- Glyph maps depend on carefully chosen anchor points, glyph size scaling, and label placement. Too many or too large glyphs reduce the scientific feel.
- Central-map satellite figures require the main map to remain dominant, but side micro-panels must have consistent axes and compact labels.
- Bubble scatter replication depends on background quadrants, selective country labels, and separate bubble-size and region legends.

## Lessons From Second Replication Pass

- Hard references need manual `fig.add_axes` panel placement when GridSpec cannot preserve the original proportions. This is especially important for central-map figures and paired-map diagnostic figures.
- Map projection is part of the visual grammar. Rectangular longitude-latitude maps look unfinished when the reference uses an oval global projection; use Mollweide/Robinson-like framing for global resource maps unless there is a reason not to.
- Transparent country overlays must use an explicit `facecolor="none"`. A missing fill can silently become the Matplotlib default color and destroy the map layer hierarchy.
- Colorbars should be positioned as separate thin axes above the map, with short ticks and no collision with titles. Inset colorbars are only acceptable when the map has enough internal whitespace.
- Satellite micro-panels should be jagged and data-like, not smooth decorative waves. Use sparse peaks, shared x-limits, thin baselines, and restrained tick labels.
- Point layers on global maps should be clustered over plausible land regions instead of randomly scattered across oceans. Density should be high, but points need small size and moderate alpha.
- Paired-map figures need more than two maps. Add mirrored Lorenz panels, latitude marginals, longitude profiles, total-capacity bars, and a bottom diagnostic row to recover the source figure's information density.
- Bubble scatter panels need two separate legends: income/region color and magnitude size. Selective country labels with short leader lines are more faithful than labeling many points directly.

## Lessons From Third Replication Pass

- In paired-map reference figures, the bottom ranking strip must occupy a full-width row by itself. If it is squeezed into a side column, the layout immediately stops looking like the source figure.
- The longitudinal profile panel should read like a sampled summary of a dense spatial process: many narrow peaks, limited smoothing, and a clear zero baseline. Broad Gaussian humps are too decorative.
- Pairwise scatter diagnostics need internal clipping for all quadrant labels, "Median" markers, and leader-line annotations. Any text that escapes its axes will collide with neighboring panels and destroy the hierarchy.
- The paired-map reference expects two map stacks with mirrored diagnostics, then the explanatory strip, then the socioeconomic scatter pair. Keep that sequence fixed when matching the grammar.
- Colorbar titles should sit above the bar, not inline with ticks. This matters especially for the compact horizontal map colorbars and the narrow vertical GDP bars beside Lorenz panels.
- When multiple subplots share a row, anchor them to the same visual baseline. Do not let axis-derived labels drift independently, or the figure will look staggered even if each panel is individually correct.
- For complex asymmetric rows, define named coordinate boxes first (`top_map`, `bottom_map`, `left_top`, `left_bottom`, `right_top`, `right_bottom`) and reuse them. Scattered numeric `add_axes` calls make it too easy for panel letters, legends, and colorbars to drift out of alignment.
- When a reference map uses a cropped global projection, hide the full Mollweide outer spine. A complete oval boundary can make the replica feel unlike the source even if the internal graticule and point layer are correct.
- Main maps must be sized by narrative weight, not just fitted into leftover space. In map-dominant references, enlarge the main map boxes until the central column feels visually saturated, then tune satellites around them.
- Treat horizontal information bands as separate rows with deliberate gutters. The `g/h` summary row and `i` ranking row need visible spacing, otherwise the lower half reads as a compressed dashboard instead of a journal figure.
- Protect the final `j/k` scatter row as a fixed anchor. Create extra space between `g/h`, `i`, and `j/k` by moving or shrinking the rows above it instead of compressing the final explanation panels.
- For paired-map references, tune horizontal compactness separately from height: widen `a/d` toward the side diagnostics while preserving a narrow gutter before `c/f`. This makes the maps feel dominant without causing overlap.
- Keep the main map curvature moderate. If the projection outline feels too pronounced, widen the map box slightly and reduce its height a little rather than changing all surrounding panels.
- For short summary bands, use semi-open axes: keep left/bottom spines and remove top/right spines so the panels feel lighter and labels do not collide with a full box outline.
- After panel layout is stable, audit the whole-canvas aspect ratio separately. If the figure feels loose or fragmented but panel positions are correct, adjust `figsize` before changing axes coordinates.

## Lessons From Measured-Skeleton Pass

- For hard replicas, measure the reference before tuning: first match the canvas aspect ratio, then define normalized panel boxes for every main panel, satellite, colorbar, legend, and inset.
- Use the exact reference image aspect ratio as the first constraint. If the source is 1280x1494, work to that ratio before any panel fitting.
- After changing canvas aspect ratio, re-scale narrow vertical panels and bottom scatter panels explicitly. Side marginals can become too tall, while scatter diagnostics can become too flat if their normalized boxes are reused unchanged.
- Use the measured skeleton to reset layout when iterative visual tweaks drift too far. A correct skeleton reduces later changes to internal styling instead of repeated panel movement.
- Reference-consistent figure aspect can change the perceived size of every normalized axes box. Re-check map curvature, row gutters, and label clearance after changing `figsize`.
- Keep measured boxes in named variables rather than inline numbers. This makes it possible to adjust a whole row or column without accidentally moving one panel out of alignment.

## Lessons From Final Paired-Map Refinement

- High-quality density is controlled, not maximal. A dense figure can carry many panels only when each panel has a role, its labels are legible, and row gutters are deliberately protected.
- The final export is the truth. A panel can look correct in code but still fail if a bottom x-axis label, colorbar label, panel letter, or tick label is cropped in the PNG/PDF.
- Move rows as systems, not as isolated axes. In the paired-map benchmark, `g/h`, `i`, and `j/k` had to be treated as three horizontal bands with explicit clearance; moving only one axis created new collisions.
- Keep bottom diagnostic panels low enough to preserve hierarchy but high enough to show x-axis labels. If the label is missing, adjust the panel box or label padding rather than accepting an incomplete export.
- Do not let panel letters float into neighboring rows. Panel letters should sit close to their own axes and be checked against rotated tick labels from the row above.
- Important maps should feel spatially full but not distorted. A larger map box, moderate projection curvature, hidden or softened outer frame, and thin graticules can make a map dominant without looking inflated.
- Lorenz curves, latitude marginals, longitude profiles, rank bars, and socioeconomic scatters work best as analytical satellites. They should respond to the main maps rather than compete with them.
- Dense satellite plots should use pale grids, thin axes, small labels, and restrained legends. Semi-open axes are useful for shallow bands where a full rectangular frame crowds annotations.
- Colorbars and legends are part of the figure skeleton. Their position, length, tick density, and title placement must be planned before the final layout pass.
- Replication teaches standards, not templates to copy blindly. For new figures, borrow the logic of hierarchy, measured layout, palette restraint, local legends, and data-rich diagnostics while adapting the grammar to the actual research question and data.
- Typography is a layout problem, not only a font-size problem. If a label is unreadable, the fix may be a larger gutter, a different legend location, or a slightly different panel box rather than a bigger or smaller font alone.
- Keep one font hierarchy throughout the figure. Mixing many unrelated sizes inside the same row makes the figure look improvised even when the data and colors are correct.
- Reference images often rely on compact but fully legible labels: panel letters are bold and clear, titles are medium-sized, and axis labels remain readable without dominating the map or scatter.

## Scientific Data Integrity Lessons

- Synthetic data is acceptable only for testing layout, never for scientific interpretation.
- For real research figures, every map value, point, curve, bar, rank, scatter coordinate, and annotation must come from input data or a documented calculation.
- If a panel requires unavailable information, report the missing data and redesign the panel. Do not invent spatial patterns, country labels, values, rankings, trends, or uncertainty.
- Figure code should make the analysis path inspectable: raw inputs, cleaning, joins, aggregation, weighting, index construction, inequality metrics, and plotting tables should be traceable.
- When a plotted element is stylistic rather than empirical, such as panel layout, color choice, or reference-inspired typography, keep it separate from data-derived marks.

## Minimum Replication Bar

A benchmark replica is not acceptable until it matches:

- Panel count or an explicitly justified simplified count.
- Relative panel size hierarchy.
- Main/satellite placement.
- Map projection or geographic framing.
- Colorbar position and length.
- Legend count and placement.
- Axis tick density.
- Label density.
- Main palette roles.
- Diagnostic panel type.

## Reference-Specific Rules

### Map Grid + Bottom Diagnostics

- Use a 3x3 map matrix occupying roughly the upper 65-70% of the figure.
- Put one horizontal diverging colorbar above the map matrix, not inside any map.
- Add a mini box/whisker diagnostic at the lower-left of each map.
- Bottom row should contain one stacked capacity bar panel and two distribution/boxplot panels.
- Keep map titles centered and short.

### Paired Maps + Lorenz/Marginals

- Use two large maps stacked vertically in the center.
- Put Lorenz/Gini diagnostics to the left of each map.
- Put vertical latitude marginals to the right of each map.
- Add longitude profile and total bar below the maps.
- Add bottom socioeconomic scatter/ranking panels if the task asks for equity, development, or fairness.

### Trend Strip + Glyph Map

- Use a three-panel top strip for trends/decompositions.
- Use one large lower map with selected regional ring glyphs.
- Size glyphs by magnitude and ring segments by composition.
- Keep one size legend and one shared color legend under or inside the map.
- Direct-label area stacks when the legend would be too large.

### Central Map + Satellite Profiles

- Place a large central map in the upper-middle.
- Put country micro-profiles on both sides, with identical x-axis ranges.
- Put a global marginal profile under the central map.
- Use bottom paired scatter plots for socioeconomic explanation.
- Keep country labels and bubble legends selective.

### Scenario Bars + Bubble Scatter

- Use a 2x2 scenario bar block at left.
- Put one large explanatory bubble scatter at right.
- Use pale background quadrants to encode conceptual regions.
- Use gray/orange/blue stacked bar roles consistently.
- Use separate legends for bubble size and region colors.
