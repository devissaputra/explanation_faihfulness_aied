# Research design

## Project aim

An explanation can sound convincing while being weakly connected to the prediction it claims to explain. This repo focuses on that gap. It provides model-agnostic metrics for comprehensiveness, sufficiency, and stability and keeps “plausible” separate from “faithful.”

## Research questions

1. Does removing top-attributed evidence materially change a model prediction?
2. Are the selected explanatory features stable under small input perturbations?
3. How does top-feature comprehensiveness compare with the supplied random-removal baseline?

## Baseline analytic pipeline

1. Prediction
2. Attribution
3. Perturbation
4. Faithfulness metrics
5. Stability audit

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- The demo operates on synthetic probability traces rather than a production model.
- Faithfulness and human usefulness are separate properties and should be evaluated separately.
- No single metric is sufficient to certify an explanation as trustworthy.

## Next experiments

- Connect the harness to a transformer classifier and SHAP/Integrated Gradients.
- Add deletion/insertion curves and counterfactual tests.
- Run educator studies comparing faithfulness, usefulness, and cognitive load.
