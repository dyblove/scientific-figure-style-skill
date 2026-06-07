# Gallery Annotations

Use this file before designing a new figure. Match by chart grammar and panel role first, then by topic. Each note describes what the figure teaches; do not copy original data, exact figure content, unique icons, or full composition.

## Tag Taxonomy

- `main-map`: one dominant spatial panel.
- `paired-map`: two main maps compared with matched scale.
- `map-grid`: many maps in a repeated matrix.
- `trend-main`: line/area trends are the main narrative.
- `scenario-dashboard`: scenarios repeated across panels.
- `glyph-map`: pie, donut, or ring glyphs over geography.
- `diagnostic`: Lorenz, Gini, violin, boxplot, density, ridgeline, uncertainty, or sensitivity panel.
- `explanation-scatter`: scatter, regression, bubble, or quadrant plot explaining drivers.
- `composition`: stacked bar, stacked area, donut, or sector decomposition.
- `reference-style`: strong visual example for layout, palette, or legend design.

## Figure Notes

### fig01 - `1780058936004.jpg`

- Tags: `trend-main`, `composition`, `main-map`, `map-triptych`, `donut-glyph`.
- Subplots: stacked historical trend at upper left; composition donuts at upper right; three choropleth maps underneath.
- Layout lesson: use compact composition summaries above maps, then let maps deliver spatial evidence.
- Borrow: muted gray/purple/red/green palette, large bottom map row, local legends next to subpanels.
- Avoid: copying the exact gas/sector categories.

### fig02 - `1780061729079.jpg`

- Tags: `main-map`, `regional-insets`, `explanation-scatter`, `ranked-bar`, `scenario-dashboard`.
- Subplots: world map plus regional zoom maps; two scatter panels; three ranked country bars with scenario mini-bars.
- Layout lesson: one geography panel can be paired with ranked national distributions and scenario diagnostics.
- Borrow: top-left spatial context, right-side ranking panels, embedded scenario bars, direct country labels.
- Avoid: overloading every panel with separate legends.

### fig03 - `1780061763024.jpg`

- Tags: `scenario-dashboard`, `composition`, `explanation-scatter`, `bubble`.
- Subplots: four scenario stacked-bar panels; one bubble scatter with regional colors and background quadrants.
- Layout lesson: compact scenario multiples can support one explanatory scatter panel.
- Borrow: gray/orange/blue share encoding, translucent quadrant background, bubble-size legend.
- Avoid: treating topic similarity as more important than stacked-bar-plus-scatter grammar.

### fig04 - `1780061790590.jpg`

- Tags: `scenario-dashboard`, `diagnostic`, `composition`, `small-multiple`.
- Subplots: dot/rank strips, line trends, bar comparisons, violin diagnostics, and country group panels.
- Layout lesson: a dense dashboard works when each block answers a different diagnostic question.
- Borrow: purple-gray hierarchy, small inset distributions, panel grouping by developed/developing countries.
- Avoid: equal emphasis for every block if the final figure needs a main finding.

### fig05 - `1780061814990.jpg`

- Tags: `trend-main`, `glyph-map`, `main-map`, `composition`, `reference-style`.
- Subplots: three top trend/decomposition panels; one large world map with regional donut glyphs.
- Layout lesson: top strip explains the temporal mechanism; large map shows regional consequences.
- Borrow: large map dominance, donut glyphs sized by magnitude, compact color and size legends under map.
- Avoid: too many glyphs; use selected anchor regions only.

### fig06 - `1780061922317.jpg`

- Tags: `main-map`, `diagnostic`, `ridgeline`, `violin`, `explanation-scatter`.
- Subplots: global point map; ridgeline density panels; climate-zone violin/scatter diagnostics.
- Layout lesson: pair spatial occurrence with distribution panels to explain mechanisms.
- Borrow: pastel density fills, repeated distribution axes, light map background.
- Avoid: adding distributions without a direct link to the map variable.

### fig07 - `1780061968705.jpg`

- Tags: `explanation-scatter`, `regression`, `small-multiple`, `diagnostic`.
- Subplots: paired scatter panels with regression and confidence regions.
- Layout lesson: repeated scatter grammar makes model comparison legible.
- Borrow: two-color category scheme, faint point clouds, confidence bands, direct regression annotations.
- Avoid: mixing unrelated scatter encodings inside one panel.

### fig08 - `1780062075410.jpg`

- Tags: `glyph-map`, `main-map`, `composition`, `SDG`.
- Subplots: world map with many multi-color pie glyphs; global average and SDG legend boxes.
- Layout lesson: glyph maps work best when glyphs are placed at regional anchors and legends are explicit.
- Borrow: compact glyph legend, global-average inset, spatially distributed composition markers.
- Avoid: placing glyphs over every country.

### fig09 - `1780062106629.jpg`

- Tags: `trend-main`, `glyph-map`, `composition`, `stacked-bar`.
- Subplots: stacked temporal bar; world map with category pie glyphs; long category legend.
- Layout lesson: use temporal accumulation plus spatial glyph summary to show diffusion of categories.
- Borrow: consistent category colors across bars and glyphs, compact color legend.
- Avoid: letting the legend dominate the figure.

### fig10 - `1780062187561.jpg`

- Tags: `scenario-dashboard`, `composition`, `grouped-bar`, `small-multiple`.
- Subplots: land-use bars, calorie/intake stacks, supply-demand bars, bioenergy stacks.
- Layout lesson: scenario ordering is the anchor; repeated bar grammar keeps many variables readable.
- Borrow: subdued greens/yellows/grays, repeated scenario-year axes, local legends.
- Avoid: changing scenario order across panels.

### fig11 - `1780062299545.jpg`

- Tags: `flow-map`, `paired-map`, `trend-main`, `composition`.
- Subplots: two flow maps comparing synergy and tradeoff; line/bar diagnostics on the side.
- Layout lesson: flow maps can be main panels when supported by compact temporal and categorical summaries.
- Borrow: paired network maps, consistent arrow semantics, small diagnostic panels at right.
- Avoid: decorative flow arcs without quantitative meaning.

### fig12 - `1780062362336.jpg`

- Tags: `SDG`, `small-multiple`, `trend-main`, `scenario-dashboard`, `reference-style`.
- Subplots: many line panels grouped by SDG badges and system blocks.
- Layout lesson: repeated small line charts can support a full SDG system narrative.
- Borrow: left SDG badge rail, same line colors across all panels, compact panel titles.
- Avoid: changing visual grammar from one indicator to another.

### fig13 - `1780062387725.jpg`

- Tags: `scenario-dashboard`, `stacked-area`, `horizontal-stacked-bar`, `composition`.
- Subplots: top stacked-area panels by scenario; bottom seasonal horizontal stacked bars.
- Layout lesson: temporal stock/flow panels pair well with seasonal or category bars.
- Borrow: supply palette separated from withdrawal palette, shared axes, row grouping.
- Avoid: using unrelated palettes for the same categories across rows.

### fig14 - `1780062435753.jpg`

- Tags: `map-grid`, `scenario-dashboard`, `composition`, `stacked-bar`.
- Subplots: top summary bars; 3x3 China maps by indicator/scenario.
- Layout lesson: a map matrix is powerful when each map shares the same geographic frame and scale logic.
- Borrow: scenario rows, indicator columns, compact top summaries.
- Avoid: independent color scales unless explicitly marked.

### fig15 - `1780064147622.jpg`

- Tags: `diagnostic`, `model-grid`, `heatmap`, `line`, `scatter`, `density`.
- Subplots: dense method panels with lattice heatmaps, time lines, log axes, and schematic diagrams.
- Layout lesson: dense method figures need tight repetition and small local legends.
- Borrow: miniature heatmaps, compact model diagnostics, consistent colorbars.
- Avoid: using this density for a first-result figure unless the audience expects methods detail.

### fig16 - `1780064844032.jpg`

- Tags: `explanation-scatter`, `quadrant`, `radar`, `map-grid`, `heatmap-table`.
- Subplots: six labeled country scatter quadrants; radar charts; maps and heatmap table.
- Layout lesson: scatter quadrants can be the main explanatory engine, with maps/tables as satellites.
- Borrow: country labels for exemplars, quadrant shading, developed/developing shape legend.
- Avoid: labeling every point.

### fig17 - `1780064867483.jpg`

- Tags: `dense-dashboard`, `map`, `donut`, `scatter`, `bar`, `line`, `diagnostic`.
- Subplots: many evidence blocks combining maps, donuts, bars, scatter, and time series.
- Layout lesson: mixed evidence grids need visual block boundaries and repeated internal grammar.
- Borrow: block-level organization, local legends, small multiples for repeated diagnostics.
- Avoid: using every chart type unless each has a defined role.

### fig18 - `1780064891853.jpg`

- Tags: `explanation-scatter`, `quadrant`, `bubble`, `country-label`, `diagnostic`.
- Subplots: six scatter/quadrant panels with country labels and bubble-size/income encodings.
- Layout lesson: repeated scatter panels can compare frequency, duration, and intensity cleanly.
- Borrow: quadrant background, bubble size legend, selective labels, shape for country group.
- Avoid: changing axis semantics between repeated scatter panels.

### fig19 - `1780064925210.jpg`

- Tags: `main-map`, `diagnostic`, `histogram`, `time-series`, `composition`.
- Subplots: world map with inset regions; frequency distributions; time series below.
- Layout lesson: map first, then distribution and temporal diagnostics.
- Borrow: top spatial context, bottom diagnostic strip, two-region comparison.
- Avoid: separating diagnostics so far from the map that the link is lost.

### fig20 - `1780064968271.jpg`

- Tags: `trend-main`, `bar-line-combo`, `small-multiple`, `percentile`.
- Subplots: four panels combining histograms/bars with percentile trend lines.
- Layout lesson: use background bars for distribution and overlaid lines for change.
- Borrow: pale bar fills with sharper line overlays, percentile titles.
- Avoid: making bars and lines compete with equal saturation.

### fig21 - `1780065005636.jpg`

- Tags: `main-map`, `histogram`, `spatial-context`, `physical-geography`.
- Subplots: global context map with highlighted regions; distance and elevation histograms.
- Layout lesson: one map plus two physical distributions can explain spatial exposure.
- Borrow: map labels, compact histograms embedded next to spatial context.
- Avoid: overcomplicating a context figure with too many response variables.

### fig22 - `1780065073108.jpg`

- Tags: `scenario-dashboard`, `map`, `bar`, `boxplot`, `warming`.
- Subplots: cohort bars, warming maps, regional pies/boxplots.
- Layout lesson: exposure narratives benefit from cohort/time summaries plus spatial end states.
- Borrow: maps as outcome panels, cohort bars as explanation, boxplots for distribution.
- Avoid: mixing scenario colors with map colors without a legend hierarchy.

### fig23 - `1780067590654.jpg`

- Tags: `sensitivity`, `diagnostic`, `cost-curve`, `waterfall`, `violin`, `radial-composition`.
- Subplots: marginal abatement/cost curve; waterfall sensitivity; violin uncertainty; radial cost/revenue ring.
- Layout lesson: pathway uncertainty can be shown through one main curve and three complementary diagnostics.
- Borrow: pathway curve with uncertainty band, cost waterfall, violin distributions, radial decomposition.
- Avoid: using radial decomposition for categories that are not compositional.

### fig24 - `1780067613269.jpg`

- Tags: `main-map`, `chord`, `line`, `bar`, `regional-insets`.
- Subplots: regional map, trend panels, circular/chord relation panel, small charts.
- Layout lesson: two anchor panels can coexist when satellites explain different evidence streams.
- Borrow: map plus chord as dual main panels, small trend diagnostics around them.
- Avoid: chord diagrams without a clear flow or relation interpretation.

### fig25 - `1780067648834.jpg`

- Tags: `paired-map`, `scenario-dashboard`, `seasonal-density`, `line`, `bar`, `scatter`.
- Subplots: paired technology maps; seasonal density curves; scenario lines; investment bars and scatter.
- Layout lesson: paired maps should share diagnostics and scenario structure.
- Borrow: technology pair comparison, seasonal distributions, feasibility/investment satellite panels.
- Avoid: placing diagnostic panels in a different order for the two technologies.

### fig26 - `1780068633770.jpg`

- Tags: `paired-map`, `diagnostic`, `marginal-distribution`, `scatter`, `line`.
- Subplots: paired global power-plant maps; side distributions; bottom scatter/line diagnostics.
- Layout lesson: paired technology maps need mirrored marginal distributions and bottom explanatory panels.
- Borrow: stacked map rows, side marginal bars, repeated bottom scatter panels.
- Avoid: unpaired diagnostics that favor one technology.

### fig27 - `1780068670042.jpg`

- Tags: `scenario-dashboard`, `trend-main`, `grouped-bar`, `pie-small-multiple`, `regional-bar`.
- Subplots: global stock bars; consumption line/ribbon; regional pie multiples; regional horizontal bars.
- Layout lesson: scenario colors can unify bars, ribbons, pies, and regional summaries.
- Borrow: consistent scenario palette across chart types, uncertainty ribbon, regional summary strip.
- Avoid: using different scenario palettes in each panel.

### fig28 - `1780069243434.jpg`

- Tags: `regional-map`, `small-multiple`, `inset-bar`, `income-group`.
- Subplots: regional maps with tiny bars and income-group labels.
- Layout lesson: repeated regional map cards can summarize many groups compactly.
- Borrow: regional card layout, small inset bars, income group annotation.
- Avoid: large legends repeated in each card.

### fig29 - `44ceac9559e47b949931ad6de24463c.jpg`

- Tags: `scenario-dashboard`, `trend-main`, `grouped-bar`, `line-ribbon`, `pie-small-multiple`, `regional-bar`, `reference-style`.
- Subplots: global stock grouped bars; global consumption line/ribbon; scenario pies; regional horizontal bars.
- Layout lesson: two major top panels can be supported by regional composition satellites below.
- Borrow: saturated scenario colors with pale ribbons, pie small multiples, regional mirrored bars.
- Avoid: letting pie labels collide; keep pies sparse.

### fig30 - `62afbca80fe2a8963f2b341d220cd05.jpg`

- Tags: `map-grid`, `trend-main`, `change-map`, `diverging-palette`, `reference-style`.
- Subplots: left global trend lines; maps for baseline years and changes across indicators.
- Layout lesson: a left trend column can orient a large map matrix.
- Borrow: repeated map scale logic, left sparkline column, indicator rows.
- Avoid: using divergent colors without a neutral midpoint.

### fig31 - `89f0af285afb9eee26fbabd9216d6c6c_.jpg`

- Tags: `main-map`, `satellite-panels`, `country-sparklines`, `marginal-distribution`, `explanation-scatter`, `reference-style`.
- Subplots: central black-background world map; country micro-panels at both sides; global distribution strip; two bottom scatter panels.
- Layout lesson: this is a high-priority template for one large map plus explanatory satellites.
- Borrow: black map background, side country profiles, bottom socioeconomic scatter, compact in-map legend.
- Avoid: copying the exact solar/PV variables or country selection.

### fig32 - `9f3dd823cf549457321cb158fc9da0f0_.jpg`

- Tags: `paired-map`, `lorenz`, `diagnostic`, `ranking-bar`, `explanation-scatter`, `reference-style`.
- Subplots: two main maps; left Lorenz curves; right latitudinal distributions; bottom ranking bars and GDP scatter.
- Layout lesson: paired maps become scientific when fairness, marginal, and socioeconomic diagnostics are attached.
- Borrow: two-row map comparison, Lorenz/Gini satellites, marginal distributions, bottom explanation panels.
- Avoid: drawing paired maps without matched colorbar and mirrored diagnostics.

### fig33 - `a64d7695ca8c502edd1044203a072aeb_.jpg`

- Tags: `main-map`, `diagnostic`, `side-distribution`, `ranking-bar`, `explanation-scatter`.
- Subplots: large world maps; side latitude profiles; bottom country ranking bars and GDP scatter.
- Layout lesson: a spatial capacity figure should include inequality and socioeconomic explanation.
- Borrow: horizontal colorbar over map, side distribution panels, bottom scatter with quadrant labels.
- Avoid: overusing labels on the map itself.

### fig34 - `ac284231350de50596373958fe1dd5c.png`

- Tags: `map-grid`, `change-map`, `diverging-palette`, `inset-bar`, `reference-style`.
- Subplots: nine repeated difference maps, each with a positive/negative proportion inset bar and a colorbar.
- Layout lesson: repeated difference maps need local sign summaries and clear colorbar direction.
- Borrow: red-white-blue diverging maps, small positive/negative inset bars, identical panel grammar.
- Avoid: interpreting red as bad unless the metric definition supports it.
# 2026-06-04 Added Reference Notes

The gallery was rescanned after adding new examples. The current scanned corpus contains 50 images. New transferable grammars include map-plus-ring/donut compositions, solid light-to-dark bar color families, scatter plots with marginal distributions and residual insets, ridgeline distributions, and box-density-scatter hybrids.

## New Grammar: Map Plus Ring / Donut / Inset Summary

- Use large maps as the first-read evidence panel.
- Place donut/ring glyphs or histograms in unused map space only when they summarize composition, target attainment, or regional structure directly tied to the map.
- Keep glyphs compact and avoid covering important geography. If a glyph competes with the map, shrink it or move it into ocean/blank space.
- Reuse the same variable-color mapping between map, ring, and legend.

Relevant indexed figures: `fig43`, `fig44`, `fig46`, `fig49`, `fig50`.

## New Grammar: Bars With Solid Light-Dark Color Families

- Prefer opaque color ramps over alpha-only gradients, especially for PDF export.
- Use light-to-medium solid color families for most bars; reserve the darkest tone for endpoints, highlights, or the most important comparison.
- Bars should support the panel's metric, not become decorative color strips. If a categorical scenario color is already defined, keep it recognizable across all panels.

Relevant indexed figures: `fig35`, `fig36`, `fig47`.

## New Grammar: Scatter With Distribution Context

- Use marginal histograms, marginal densities, residual boxplots, or quadrant labels when the scatter relationship alone is not enough.
- The main scatter remains dominant; marginal diagnostics should be visually quieter and smaller.
- Key countries or cases may be annotated, but labels should be sparse and tied to the main claim.

Relevant indexed figures: `fig40`, `fig42`, `fig49`.

## New Grammar: Ridgeline And Box-Density-Scatter Panels

- Use ridgelines for ordered distribution comparisons where shape and shifting modes matter.
- Use half-violin/box/jitter hybrids when showing category spread, medians, sample density, and outliers in a single compact panel.
- Keep density fills pale, median or trend lines darker, and points small enough to avoid hiding distribution shape.

Relevant indexed figures: `fig37`, `fig39`, `fig41`.

## Added Design Principle: Controlled Visual Hierarchy

High-level figures rarely make every panel equal. Before designing or revising a figure, decide:

1. What is the central scientific message?
2. Which panel should be read first?
3. Which panels only explain, validate, or decompose that message?
4. Which information can be weakened through smaller size, lower saturation, thinner marks, or fewer labels?

If every panel is the same size, every color is bright, and every result is emphasized, the reader remembers less. The strongest figure is often not the one with the most information, but the one that guides attention to the result that matters.
