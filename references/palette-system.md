# Palette System

Prefer low-saturation palettes with one or two saturated anchors. Use pale fills, medium lines, and dark text. Keep the same meaning-color mapping across panels.

## Core Neutral System

- Canvas: `#FFFFFF`
- Panel background: `#FFFFFF` or `#FAFAF8`
- Gridline: `#E6E6E6`
- Coast/country boundary: `#CFCFCF`
- Axis/text: `#222222`
- Secondary text: `#666666`

## PV / Technology Pair Palette

Use when two technologies are compared.

- Utility-scale PV: `#2C7FB8`
- Distributed PV: `#C55A9D`
- Both/overlap: `#111111`
- Pale utility fill: `#B9D7E8`
- Pale distributed fill: `#E5B6D7`
- Solar/radiation background low: `#CFE8E8`
- Solar/radiation background high: `#F2C66D`
- Hotspot accent: `#E87755`

## Water / Supply-Demand Palette

Use for water supply and withdrawal systems.

- Surface water: `#78B7CD`
- Groundwater: `#A9CBE3`
- Wastewater/reuse: `#B98BC0`
- Desalination: `#F0C36D`
- Agriculture: `#B9DD8A`
- Recharge/ecosystem: `#58B99C`
- Building/urban: `#AFC9DA`
- Industry: `#416FA3`
- Upstream/energy demand: `#F2A3A0`

## SDG / System Palette

Use for multi-domain SDG and integrated assessment figures.

- Energy blue: `#3478B8`
- Climate green: `#2F9A43`
- Water cyan: `#24A7C9`
- Land green: `#76B852`
- Food/gold: `#D69A24`
- Industry orange: `#E97722`
- Health red: `#C9413A`
- Equity/purple: `#7D68A8`
- Neutral gray: `#B9B9B9`

## Scenario Line Palette

Use for SSP/NDC/policy pathways. Pair colored lines with translucent ribbons.

- Low/green pathway: `#4C9A2A`
- Middle/blue pathway: `#2E78B7`
- Orange pathway: `#F28E2B`
- Purple pathway: `#8B6FB4`
- Pink pathway: `#D65F9E`
- Red/high pathway: `#D94C4C`
- Gold/high-demand pathway: `#F2B01E`

## Diverging Change Palette

Use for maps of difference or relative change.

- Strong negative: `#B54A3A`
- Mild negative: `#E8B5A8`
- Neutral: `#F7F7F3`
- Mild positive: `#9EC3D8`
- Strong positive: `#2F6F95`

Do not assume red is always bad. Label the colorbar explicitly with negative/positive or lower/higher.

## Multicategory Area Palette

Use for stacked area and decomposition panels.

`#F6D9A8`, `#F2B96D`, `#79B76D`, `#2FB99F`, `#8BD1CC`, `#7FB7DD`, `#9D8AC4`, `#D182B8`, `#8E8E8E`

## Rules

- Use 4-7 categorical colors in one panel when possible; more categories require grouping small classes into "Other".
- Use alpha 0.15-0.35 for uncertainty ribbons and 0.55-0.8 for area fills.
- Use darker outlines of the same hue for area boundaries.
- Avoid neon cyan, pure red, pure blue, pure green, and default Matplotlib tab colors without muting.
- If a figure contains maps and charts, let the map use a continuous palette and reserve categorical colors for overlays, legends, or satellites.
- For publication bars, prefer opaque light-to-dark color families over alpha-only gradients. Alpha-only bars often look washed out in exported PDF/SVG.
- Reserve the strongest saturation for the main evidence panel or the focal scenario. Supporting panels should usually use softer fills, thinner lines, or reduced contrast.
- When using SVG-first output, check that transparent ribbons, raster icons, and semi-transparent overlays export as intended.
