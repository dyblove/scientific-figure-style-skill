# Preference Checklist

Use this checklist when translating the gallery into a new figure.

## Overall Aesthetic

- Scientific, information-dense, and restrained.
- One or two main panels should dominate; supporting panels should be smaller but analytically necessary.
- Decide the figure's first-read panel before arranging anything. The reader should know where to look first within one or two seconds.
- Do not make all panels equally bright, equally large, or equally detailed unless the explicit purpose is systematic comparison.
- Visual hierarchy should follow scientific hierarchy: central finding strongest, explanatory panels quieter, context palest.
- White-space should separate panel groups, not create a sparse poster.
- Prefer compact labels, direct annotations, and local legends over large detached legends.
- The figure should read as a paper result, not a dashboard or presentation slide.

## Main Panel Rules

- For spatial questions, use a large map as the primary evidence panel.
- For scenario questions, use one main trend panel plus maps or diagnostic panels.
- For paired comparisons, keep scales, projections, and axes matched.
- Do not give all panels the same visual weight unless the figure is explicitly a systematic matrix.
- If a map is the main panel, satellites may sit in unused map space only when they do not cover key geography and directly explain the map.
- If a scatter is the main panel, marginal histograms/densities, residual insets, or quadrant annotations can support it, but should not overpower the point cloud.

## Satellite Panel Rules

- Each satellite panel must answer one support question: where, why, who, how much, when, under which scenario, or how unequal.
- Put diagnostic panels close to the main panel they explain.
- Prefer small multiples when the same visual grammar repeats across scenarios, SDGs, countries, or years.
- Use inset bars, marginal distributions, Lorenz curves, scatter panels, or ring glyphs only when they explain the main map/trend.
- Satellite panels should borrow the main panel's color logic but usually use lower saturation, smaller marks, or lighter gridlines.
- Do not add a satellite panel only to fill blank space. Blank space is acceptable if it protects hierarchy and readability.
- Use ridgelines for ordered distribution comparisons, box-density-scatter hybrids for category spread, and marginal distributions for scatter diagnostics.

## Palette Rules

- Use low-saturation fills and medium-saturation lines.
- Use green/blue for improvement or sustainable pathways, orange for delayed or transitional pathways, pink/red for decline or risk.
- Use red-white-blue diverging palettes only for signed change maps.
- Use black/dark map backgrounds only when imitating reference figures with projected world maps and pale graticules.
- Keep scenario colors identical across lines, maps, petals, bars, and legends.
- Avoid making every color equally saturated. Keep one or two attention colors; make secondary categories paler or thinner.
- For bars, prefer solid color ramps or carefully chosen light-to-dark families over alpha-only gradients that look transparent in PDF.
- For donut/ring glyphs, use color as composition or scenario encoding only when it matches the surrounding panels.

## Legend Rules

- Put colorbars directly above, below, or inside the map block.
- Put size legends inside empty map space when possible.
- Use one shared legend for repeated panels.
- Prefer direct line labels for scenario trends.
- Use local mini legends for inset diagnostics only when the encoding changes.

## Typography Rules

- Use bold lowercase panel letters.
- Use short panel titles that state metric, time, and scenario.
- Put units in axis labels and colorbars.
- Use smaller labels inside dense panels; do not use hero-size typography.
- Label only exemplar countries or reference thresholds.
- Use a fixed font hierarchy rather than ad hoc sizes:
  - panel letters: about 14-16 pt
  - main map / panel titles: about 9-10 pt
  - axis labels and legend titles: about 8-9 pt
  - tick labels and local legends: about 7-8 pt
  - internal annotations and threshold notes: about 7-8 pt
- Keep font weights consistent: use bold only for panel letters, main titles, and selected key values.
- Prefer dark text on light backgrounds; do not use pale gray labels for core information.
- If a label becomes unreadable at final export size, enlarge the panel, move the legend, or simplify the panel rather than shrinking the font below the readable range.
- In dense journal figures, avoid mixing many unrelated font sizes within the same row.
- Rotated tick labels and vertical y-axis titles need extra gutter; protect them with layout, not with smaller fonts.
- Keep legends and panel titles close to the panel they explain, but outside the data region when they would cover marks.
- Use wrapping only when the axis is too narrow; otherwise keep labels on one line for clarity.

## Gini / Inequality Rules

- Do not default to a standalone Gini time-series if it feels detached.
- For map-dominant figures, use Lorenz/Gini mini-panels, binned country strips, or marginal distributions to explain spatial inequality.
- For trend-dominant figures, use Gini as a small diagnostic next to the main trend or as shaded convergence/divergence markers.
- Always connect Gini to the substantive claim: improvement can coexist with divergence.

## Replication Quality Bar

Before generalizing from a reference, confirm these can be reproduced:

- Panel count and hierarchy.
- Relative panel sizes.
- Main/satellite relationship.
- Colorbar and legend placement.
- Axis/grid density.
- Label density and direct annotations.
- Palette roles and saturation.
- Figure-level reading order.
- Main-versus-satellite hierarchy: which panel is remembered after a quick glance?
- Intentional weakening of auxiliary information: quieter grids, smaller labels, lower saturation, or smaller panel size.
