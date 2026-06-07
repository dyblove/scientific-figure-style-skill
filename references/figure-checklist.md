# Figure Checklist

Use this before finalizing any figure or code.

## Narrative

- Is there a one-sentence claim?
- Are there one or two clear main panels?
- Can a reader identify the first-read panel within one or two seconds?
- Is the most important result visually dominant by size, placement, contrast, or annotation?
- Does every satellite panel explain or validate the main panel?
- Are any panels competing for attention despite being only supporting evidence?
- Does the reading order match the panel lettering?
- Are repeated scenarios, regions, or years ordered consistently?

## Data Provenance

- Is every plotted mark backed by raw data or a documented derived table?
- Are the raw input files, join keys, units, years, regions, and scenarios known?
- Are population weights, Gini/Lorenz values, trends, ranks, and normalized indices computed explicitly rather than hand-set?
- Is any synthetic or placeholder data clearly reported as a layout test rather than a result?
- Are unsupported panels removed, replaced, or flagged instead of visually invented?

## Layout

- Is the main panel large enough to dominate?
- Are supporting panels intentionally smaller, quieter, or more compact than the main result?
- Are axes aligned across repeated panels?
- Are maps and satellites visually connected without arrows unless arrows add meaning?
- Is there enough white space between panel groups?
- Are panel letters visible but not oversized?
- Does the canvas aspect ratio match the reference or target journal format?
- Are panel boxes aligned by measured baselines, not by visual guesswork alone?
- Are row gutters large enough that labels from adjacent rows cannot collide?
- Are colorbars, legends, panel letters, axis labels, and tick labels fully inside the exported image?

## Data Encoding

- Are units present on every axis and colorbar?
- Are color meanings consistent across panels?
- Is the strongest color reserved for the most important comparison or result?
- Are contextual marks muted enough that they do not compete with the main finding?
- Are diverging colorbars labeled with direction and neutral point?
- Are log scales, normalized values, and index baselines explicitly marked?
- Are uncertainty ribbons, percentiles, and medians explained locally?
- Are maps using a projection and geographic framing appropriate to the spatial claim?
- Are map color scales shared when comparing panels and separated only when the metric genuinely changes?
- If using marginal histograms, ridgelines, donuts, or inset bars, do they answer a specific support question rather than decorate the layout?

## Legend And Labels

- Can direct labels replace part of the legend?
- Is each legend placed near the data it explains?
- Are repeated legends removed?
- Are country labels limited to key exemplars?
- Are small-panel labels readable at final publication size?
- Are labels dense enough to make the panel interpretable without the caption, but not so dense that they cover data?
- Do compact panels use local legends or direct annotations instead of detached legend blocks?
- Are font sizes consistent within each hierarchy level across the figure?
- Are panel titles, axis labels, tick labels, legends, and annotations visually distinct without becoming mismatched?
- Do rotated labels, vertical labels, and outside legends have enough gutter to avoid colliding with neighboring panels?
- Are key labels dark and legible rather than faint or decorative?

## Style

- Does the palette remain low-saturation and harmonious?
- Are gridlines pale and axes thin?
- Are decorative elements absent?
- Are large filled areas slightly muted?
- Does the final figure work in both screen view and printed PDF?
- Do dense summary panels use light or semi-open axes where full borders would create clutter?
- Does visual emphasis follow evidence hierarchy: main panels strongest, diagnostics quieter, context palest?
- Are alpha-only gradients avoided when solid light-to-dark color ramps would export more cleanly?
- Do distribution panels choose the right grammar: ridgeline for ordered groups, box-density-scatter for category spread, marginal density for scatter context?

## Export Audit

- Open the exported PNG/PDF and inspect the whole canvas, not just individual panels.
- Check the top, bottom, left, and right edges for cropped labels.
- Check every row boundary for overlap between tick labels, titles, panel letters, legends, and neighboring panels.
- Confirm that bottom-row x-axis labels and colorbar labels are visible after export.
- Compare the exported figure against the intended reference scale, not just the on-screen preview.
