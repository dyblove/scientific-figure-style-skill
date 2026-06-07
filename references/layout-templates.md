# Layout Templates

Use these templates as reusable figure grammars. Adapt dimensions to the target journal column width, but preserve the main-panel/satellite-panel logic.

## Central Map With Satellite Diagnostics

Use for global spatial findings with country examples.

- Main panel: one large central world map, 45-60% of canvas.
- Satellites: country mini line/density plots on left and right, one global marginal distribution below, one or two bottom scatter plots.
- Best for: PV potential, resource exposure, climate risk, facility siting, spatial inequality.
- Design cues: align country mini-panels to the map edges; keep axes identical; use two strong colors for two technologies and black/gray for overlap.

## Paired Main Maps With Diagnostic Panels

Use when comparing two technologies, scenarios, or allocation rules.

- Main panels: two large maps stacked vertically or side-by-side with identical projection and colorbar scale.
- Left satellites: Lorenz/fairness curves or cumulative distribution plots.
- Right satellites: latitudinal/longitudinal marginal histograms.
- Bottom satellites: ranking bars and two socioeconomic scatter plots.
- Best for: utility-scale vs distributed systems, current vs future, baseline vs policy, equity analysis.

## Trend Strip Plus Glyph Map

Use when time trajectories explain a spatial composition map.

- Top strip: three compact panels showing total trend, regional decomposition, and technology/sector decomposition.
- Main panel: large world map with regional donut/ring glyphs.
- Legends: one compact size legend and one shared color legend under the map.
- Best for: employment, SDG co-benefits, regional composition, technology mixes.

## Scenario Small-Multiple Dashboard

Use when the same metric is compared across scenarios and years.

- Arrange panels in a matrix ordered by scenario severity, policy pathway, or time.
- Use shared axes wherever possible.
- Use direct labels on trajectory lines and short scenario tags above panels.
- Best for: SSP pathways, NDC/CN60/CN60-SDG comparisons, pathway sensitivity.

## Stacked Area Plus Seasonal Bars

Use for supply/demand systems with temporal and seasonal breakdowns.

- Top row: scenario-specific stacked areas with shared y-axis.
- Bottom row: horizontal stacked bars grouped by season and scenario.
- Use one palette family per side of the system, such as water supply blues/purples and withdrawals greens/oranges.
- Best for: water supply, water withdrawal, energy mix, agricultural inputs.

## Difference Map Grid

Use when many indicators share the same geographic comparison.

- Arrange maps in a 3x3 or 4x4 grid.
- Each panel gets a small inset positive/negative proportion bar if sign balance matters.
- Use the same diverging palette family and symmetric colorbar logic where possible.
- Best for: SDG tradeoffs, water/energy/food differences, indicator sensitivity.

## SDG Section Matrix

Use for many time-series indicators organized by theme.

- Left rail: theme labels and SDG icons or compact colored badges.
- Right: repeated small line charts, 3-4 columns wide.
- Use the same scenario colors across all panels.
- Best for: SDG pathways, integrated assessment, multisystem policy narratives.

## Map Plus Socioeconomic Explanation

Use when a physical result needs equity/development interpretation.

- Main panel: map or mapped point layer.
- Explanation panels: GDP/capita or income-level scatter plots with bubble size as magnitude.
- Add quadrant labels, medians, or 45-degree reference lines sparingly.
- Best for: capacity inequality, employment impacts, embodied labor, resource fairness.

## Sensitivity Pathway Figure

Use when explaining model pathway robustness.

- Main panel: cost or abatement curve.
- Satellites: waterfall bars, violin distributions, radial cost/revenue decomposition.
- Use pale fills for uncertainty and colored symbols for sensitivity cases.
- Best for: mitigation cost, model sensitivity, abatement pathways, infrastructure uncertainty.

## Hard Reference Layouts

Use these when the user asks for replication-quality imitation.

### 3x3 Map Matrix With Bottom Diagnostics

- Upper block: 3 columns x 3 rows of matched world maps, each with a small inset box/whisker diagnostic.
- Top colorbar: one shared horizontal colorbar centered above the maps.
- Bottom block: one stacked capacity bar panel at left, two boxplot/distribution panels at center and right.
- Best for: policy allocation scenarios, model/leader alternatives, relative change maps.
- Critical detail: keep map titles short, map panels compressed, and bottom diagnostics visually subordinate but readable.

### Paired Maps With Full Equity Diagnostics

- Center: two large maps stacked vertically, one per system or pathway.
- Left: one Lorenz/Gini panel aligned with each map.
- Right: one latitude/marginal distribution panel aligned with each map.
- Lower strip: longitude profile, total summary bar, ranked country bars, or GDP scatter.
- Best for: spatial inequality, utility vs distributed systems, fairness and allocation analysis.
- Critical detail: the map pair must use matched geographic frame and a shared palette logic.

### Trend Strip Plus Large Glyph Map

- Top row: three equally sized trend/decomposition panels.
- Lower row: one large world map with regional donut/ring glyphs.
- Legends: size legend and composition legend live inside the map's empty space or just under it.
- Best for: regional employment, sector composition, SDG co-benefits.
- Critical detail: glyph count must be limited; chosen anchors should carry the narrative.

### Central Map With Country Profile Satellites

- Center: large map or resource surface with point overlays.
- Left and right: vertically stacked country micro-profiles using identical axes.
- Middle-bottom: global marginal profile matching the micro-profile x-axis.
- Bottom: two explanatory scatter/bubble panels.
- Best for: resource suitability, global infrastructure siting, technology allocation.
- Critical detail: side profiles should look like miniature replicas, not independent plots.

### Scenario Bars Plus Explanatory Bubble Scatter

- Left: 2x2 small-multiple scenario stacked bars.
- Right: one large bubble scatter with conceptual background quadrants.
- Legends: one bar role legend below the left block; bubble-size and region legends inside the scatter.
- Best for: share decomposition plus labor/income/equity explanation.
- Critical detail: scatter background shading and selective labels carry much of the narrative.
