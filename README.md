# Scientific Figure Style Skill

A Codex skill for designing, critiquing, replicating, and implementing high-density scientific figures in a Nature/Science-style visual language.

This skill is built around a simple principle: a research figure is a scientific argument, not a collection of isolated charts. Before drawing, it forces the figure logic to become explicit: what the figure claims, which panel the reader should see first, which panels are supporting evidence, what data each mark requires, and how visual hierarchy should guide attention.

## What It Does

- Builds a **figure contract** before plotting new scientific figures.
- Separates **main evidence panels** from quieter satellite, diagnostic, explanation, and summary panels.
- Uses a curated **chart atlas** to choose appropriate chart grammars instead of defaulting to generic plots.
- Supports a dedicated **reference replication mode** for imitating a provided figure's layout grammar, panel proportions, legend placement, typography, and palette behavior.
- Encourages **SVG-first** publication output, with PDF and PNG exports where appropriate.
- Enforces **data integrity**: every map value, point, bar, ribbon, threshold, and annotation must come from data or a documented calculation.

## Core Workflow

1. Classify the task: new figure, revision, critique, code/debug, or reference replication.
2. For a new figure, write a figure contract and wait for confirmation before coding.
3. Decide the first-read panel and evidence hierarchy.
4. Select panel-level chart forms from the chart atlas.
5. Retrieve matching reference examples by chart grammar and narrative role.
6. Map every planned visual mark to raw fields or derived calculations.
7. Build the figure skeleton: canvas ratio, panel boxes, gutters, colorbars, legends, and labels.
8. Render data-derived marks only.
9. Export SVG/PDF/PNG and inspect the final files, not just notebook previews.

## Included References

The skill includes compact design references and operational checklists:

- `references/figure-contract.md` - contract template for new figure design.
- `references/chart-atlas.md` - reusable chart grammars for maps, bars, scatters, distributions, heatmaps, glyphs, and image plates.
- `references/layout-templates.md` - multi-panel layout patterns.
- `references/palette-system.md` - palette rules and scenario/gradient guidance.
- `references/source-preferences.md` - distilled user style preferences.
- `references/preference-checklist.md` - hierarchy, typography, palette, legend, and panel-role checks.
- `references/replication-benchmarks.md` - concrete lessons from hard reference replication attempts.
- `references/gallery-annotations.md` and `references/gallery-index.jsonl` - searchable gallery notes.
- `references/gallery-scan-manifest.json` and `references/gallery_palette_summary.json` - scanned gallery metadata.

## Design Philosophy

High-quality scientific figures rarely make every panel equally large, equally bright, or equally important. The best figures control attention:

- the main panel carries the core claim;
- supporting panels explain, validate, decompose, or contextualize;
- color saturation follows scientific importance;
- legends, colorbars, labels, and gutters are treated as layout objects;
- blank space is allowed when it protects hierarchy and readability.

The goal is not decoration. The goal is a figure that makes the scientific argument clear, rigorous, and memorable.

## Replication Mode

When the user provides a reference image and asks to match it, the skill switches to replication mode:

- lock the output canvas to the reference aspect ratio;
- measure visible panel boxes as normalized coordinates;
- place legends, colorbars, insets, and labels before internal data styling;
- match main-versus-satellite hierarchy;
- preserve palette roles while adapting semantics to the user's data;
- only generalize after the skeleton is stable.

This copies visual grammar, not data values or scientific content.

## Installation

Clone or copy this folder into your Codex skills directory:

```powershell
git clone https://github.com/dyblove/scientific-figure-style-skill.git "$env:USERPROFILE\.codex\skills\scientific-figure-style"
```

Then use it by naming `scientific-figure-style` in a Codex task, or by asking for publication-style scientific figure design, critique, revision, or replication.

## Repository Structure

```text
scientific-figure-style/
├── SKILL.md
├── README.md
├── agents/
├── references/
│   ├── figure-contract.md
│   ├── chart-atlas.md
│   ├── layout-templates.md
│   ├── palette-system.md
│   ├── preference-checklist.md
│   ├── replication-benchmarks.md
│   └── ...
└── scripts/
    └── scan_gallery.py
```

## Notes

This skill is intended for research workflows where accuracy and traceability matter. Synthetic data may be used for layout testing, but final scientific figures should only present data-derived marks from documented inputs and calculations.
