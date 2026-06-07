# Figure Contract

Use this before writing plotting code for any new scientific figure, whether it is a single panel or a multi-panel composite. The contract is not a decorative plan; it is the logic gate that decides what the figure is allowed to contain.

## When Required

Prepare a figure contract before implementation when the user asks to create, redesign, or substantially revise a scientific figure.

Do not skip directly into Python/R unless:

- the user explicitly asks only for a small mechanical edit to an existing figure, or
- the user has already approved a figure contract in the current task, or
- the task is a pure code/debug request rather than a design request.

## Contract Template

Return this structure to the user and wait for confirmation before implementing:

### 1. Core Claim

One sentence:

```text
This figure should convince the reader that ...
```

### 2. First-Read Panel

Identify the panel the reader should see first.

```text
First-read panel: ...
Reason: ...
```

The first-read panel must be visually dominant through size, placement, contrast, or direct annotation.

### 3. Panel Logic

For each panel:

| panel | role | scientific question | chart type | required data | why it belongs |
| --- | --- | --- | --- | --- | --- |
| a | main / satellite / diagnostic / explanation / summary | ... | ... | ... | ... |

If a panel cannot be tied to a scientific question, propose removing or merging it.

### 4. Evidence Hierarchy

Rank panels by importance:

1. Main evidence
2. Mechanism or decomposition
3. Inequality / uncertainty / robustness
4. Socioeconomic explanation
5. Context or annotation

Only the first level should receive the strongest visual emphasis.

### 5. Candidate Chart Forms

For every important panel, give a primary chart choice plus at least one alternative:

| panel | recommended form | alternative form | reason for choosing |
| --- | --- | --- | --- |

Use `chart-atlas.md` for this step.

### 6. Layout Skeleton

For multi-panel figures, describe the proposed layout before code:

- Canvas orientation and approximate aspect ratio.
- Main panel size and position.
- Satellite panel groups.
- Shared legends/colorbars.
- Reading order.
- Which information should be visually weakened.

For single-panel figures, describe:

- Axes and scale.
- Marginal or inset diagnostics, if any.
- Annotation strategy.

### 7. Palette And Encoding

Specify:

- Main variable palette.
- Scenario/group colors.
- Uncertainty or missing-data encoding.
- Which color is the attention color.
- Which marks should be muted.

### 8. Data Provenance

List the required data fields and derived calculations. Every plotted mark must map to a field or calculation.

| output mark | raw fields | derived calculation | unit / range |
| --- | --- | --- | --- |

If data are not yet available, define a logical interface rather than inventing values.

### 9. Export Contract

Default export should be SVG-first:

- `*.svg` editable vector output when feasible.
- `*.pdf` publication/vector output.
- `*.png` high-resolution preview.

State any raster-only components, such as map tiles, images, or official icons.

### 10. Approval Prompt

End with a concrete confirmation request:

```text
If this contract is correct, I will implement this layout and keep style parameters stable.
```

