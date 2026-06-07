# Chart Atlas

Use this atlas to choose panel-level grammars before coding. It complements the multi-panel layout templates by decomposing figures into reusable single-chart forms.

## Lines And Trajectories

Use for trends, pathways, model time series, and intervention response.

- `line + uncertainty ribbon`: scenario trajectories with confidence/ensemble intervals.
- `small-multiple line grid`: many indicators, SDGs, countries, or models with shared axes.
- `stacked area`: composition over time where totals and shares both matter.
- `slopegraph`: two-time-point change, ranking shifts, before/after comparisons.

Prefer direct line labels over detached legends when there are few series.

## Bars

Use for ranks, totals, group means, signed deltas, and composition.

- `ranked horizontal bars`: regional/country ordering, contribution ranking.
- `grouped bars`: scenario-by-region or category-by-year comparison.
- `stacked bars`: composition shares, sector mix, phase/status breakdown.
- `diverging bars`: positive/negative effects around zero.
- `bars + mean/reference lines`: compare groups against global or policy thresholds.
- `bar + donut inset`: combine magnitude with count/composition when the inset answers a support question.

Use opaque solid color ramps. Avoid alpha-only bar gradients that look washed out in PDF.

## Maps

Use for spatial evidence.

- `dominant choropleth map`: first-read global pattern.
- `paired maps`: two systems/scenarios with matched scales.
- `map grid`: many indicators or scenarios, only when systematic comparison is the point.
- `map + inset histogram`: spatial distribution plus frequency context.
- `map + ring/donut glyphs`: regional composition, target attainment, or local mix.
- `map + marginal profiles`: latitude/longitude gradients or regional summaries.

Do not let inset glyphs cover important geography. Put them in ocean/blank space when possible.

## Scatter And Relationship Panels

Use for explanatory relationships, socioeconomic interpretation, model performance, and tradeoffs.

- `scatter + regression`: association with uncertainty.
- `bubble scatter`: magnitude as size, group/stage as color.
- `quadrant scatter`: conceptual classification around thresholds.
- `scatter + marginal histograms/densities`: relationship plus distribution of x/y.
- `observed vs predicted + residual inset`: model diagnostics.
- `scatter matrix`: only when several pairwise relations are equally important.

Label only exemplar countries or cases.

## Distributions

Use when spread, shape, tails, or group heterogeneity are central.

- `histogram/density`: single distribution.
- `ridgeline`: ordered groups, scenario/time progression, shifting modes.
- `violin/half-violin`: distribution shape by category.
- `boxplot`: median/IQR/outliers with restrained marks.
- `box-density-scatter hybrid`: category spread plus sample points; good for compact high-level panels.
- `Lorenz/Gini curve`: inequality and concentration.

Use pale fills and darker median/trend lines. Do not make distribution panels compete with the main evidence panel unless distribution is the central claim.

## Heatmaps And Matrices

Use for indicator-by-scenario, SDG-by-year, model-by-metric, or interaction matrices.

- `simple heatmap`: ordered matrix with clear colorbar.
- `clustered heatmap`: only when clustering is substantively meaningful.
- `bubble matrix`: two variables encoded by color and size.
- `signed heatmap`: diverging palette centered at zero.
- `icon/label strip + heatmap`: SDG or domain matrices.

Protect label readability with row/column grouping rather than shrinking text excessively.

## Polar, Ring, And Glyph Panels

Use for compact multivariate summaries.

- `donut/ring`: composition, count above threshold, regional share.
- `petal/radial bar`: multi-goal or multi-domain score profile.
- `polar histogram`: directional/seasonal/circular distribution.
- `radar`: only for a few comparable dimensions; avoid when precise comparison matters.

Glyphs should be satellites unless the whole figure is a multivariate-summary figure.

## Image Plates

Use when the evidence is visual/image-derived.

- `image grid`: matched microscopy/remote-sensing/photo panels.
- `channel overlay`: consistent channel colors and scale bars.
- `zoom crop`: paired full image and local detail.
- `image + quantitative side panel`: image evidence plus measured distribution/bar/scatter.

Always include scale bars, channel labels, and consistent crop sizes.

## Choosing A Chart

1. Start from the scientific question, not the available plotting library.
2. If the answer is spatial, begin with map grammars.
3. If the answer is temporal, begin with line/area grammars.
4. If the answer is heterogeneity, begin with distribution grammars.
5. If the answer is explanation or association, begin with scatter grammars.
6. If the answer is decomposition or rank, begin with bar grammars.
7. If several answers are needed, make one main and the others satellites.

