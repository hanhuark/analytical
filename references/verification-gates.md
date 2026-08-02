# Verification Gates

## Gate 1: Definitions and dimensions

Pass only if all symbols, dimensions, SI units, signs, frames, time bases, property states, and data ordering are explicit and consistent. Every additive term must have identical dimensions. Every transcendental function must receive a dimensionless argument.

## Gate 2: Conservation and admissibility

Check mass, species, momentum, energy, charge, and entropy balances as applicable. Verify interface jump conditions, source terms, work and heat signs, positive material properties, realizability, and nonnegative entropy production when required.

## Gate 3: Limits and asymptotics

Test zero and infinite forcing, vanishing and dominant transport coefficients, equal phase properties, dilute and dense limits, large and small geometry, steady limits of transient models, and reduced-dimensional limits. Classify every singular limit as physical, removable, or evidence of invalid scope.

## Gate 4: Baseline recovery

Recover accepted results only inside their stated regimes. A model that cannot recover a credible baseline needs a documented physical reason and discriminating evidence. Do not force recovery by fitting a regime-dependent coefficient and calling it universal.

## Gate 5: Closures and identifiability

For each closure, state whether it is derived, measured, correlated, fitted, or assumed. Check parameter redundancy, covariance, practical identifiability, and whether target data were used both to define and validate the closure.

## Gate 6: Algebra, code, and numerics

Reproduce symbolic steps, unit conversions, numerical constants, and transformations independently. Test code with analytic or manufactured cases. Check precision, convergence, conditioning, discretization error, and deterministic ordering where relevant.

## Gate 7: Evidence and novelty

Verify each material citation in the primary source. Confirm that the cited definition, equation, regime, and conclusion match the claim. Search for earlier equivalent mechanisms, nondimensional groups, transforms, and counterexamples.

## Gate 8: Calibration and external validation

Partition data by physical source of domain shift, not random rows alone. Keep calibration, model selection, and final validation separate. Report uncertainty in observations and properties, experimental variability, parameter uncertainty, numerical error, and model-form discrepancy separately when possible.

## Gate 9: Discrimination and causality

Ask whether another mechanism predicts the same terminal response. Require intermediate observables or interventions that distinguish causal accounts. A correlation that predicts a threshold does not by itself identify the triggering mechanism.

## Gate 10: Reporting integrity

Maintain a claim ledger linking each conclusion to an equation, source, computation, or measurement. Preserve contradictions and failed checks. State residual risk and the evidence needed for promotion to the next claim-ladder rung.

## Severity rubric

- `fatal`: Invalidates the central derivation, mechanism, or claimed novelty.
- `major`: Changes the model form, dominant balance, scope, or principal conclusion.
- `repairable`: Local issue with a clear correction that does not change the governing mechanism.
- `applicability-limiting`: Valid result whose stated domain is too broad.
- `minor`: Presentation or reproducibility issue with no material physical effect.

Do not mark a gate passed from an author's assertion. Record the performed check and its evidence.
