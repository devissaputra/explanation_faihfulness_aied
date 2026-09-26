# Calculation guide

## Question and evidence

Do chosen features retain and explain a prediction?

Synthetic original, feature-removed and feature-only probabilities plus feature sets.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Calculate clipped probability drops, set overlap and a declared weighted summary.

## Calculation and interpretation

`Comprehensiveness = max(0,p-p_without); sufficiency gap = max(0,p-p_only).`

Jaccard overlap measures set stability. Clipping discards negative effects. The weighted faithfulness index is a heuristic on supplied synthetic probabilities, not a validated explanation metric or a model perturbation experiment.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| comprehensiveness | 0.197 | unitless | `comprehensiveness` |
| sufficiency_gap | 0.074 | unitless | `sufficiency_gap` |
| stability_jaccard | 0.837 | unitless | `stability_jaccard` |
| faithfulness_index | 0.562 | unitless | `faithfulness_index` |

Source: [results/demo_metrics.json](results/demo_metrics.json). Values resolve directly from this file when figures are regenerated.

This prototype makes explanation diagnostics explicit through probability-drop and feature-overlap calculations on synthetic cases. It distinguishes comprehensiveness, sufficiency gap, and stability, while labeling the combined index as a hand-weighted heuristic. The current software accepts supplied perturbation outputs; a substantive empirical study would need actual model interventions and suitable random-feature controls.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`main`](src/explanation_faithfulness_aied/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`comprehensiveness`](src/explanation_faithfulness_aied/core.py#L8) | Inspect the explicit implementation and its callers. |
| [`sufficiency_gap`](src/explanation_faithfulness_aied/core.py#L9) | Inspect the explicit implementation and its callers. |
| [`jaccard`](src/explanation_faithfulness_aied/core.py#L10) | Inspect the explicit implementation and its callers. |
| [`faithfulness_index`](src/explanation_faithfulness_aied/core.py#L12) | Inspect the explicit implementation and its callers. |
| [`evaluate_cases`](src/explanation_faithfulness_aied/core.py#L14) | Inspect the explicit implementation and its callers. |
| [`make_cases`](src/explanation_faithfulness_aied/synthetic.py#L3) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

Jaccard overlap measures set stability. Clipping discards negative effects. The weighted faithfulness index is a heuristic on supplied synthetic probabilities, not a validated explanation metric or a model perturbation experiment. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
