# Verification Gates

The gate IDs and order below are canonical and match `scripts/package_spec.json` and `assets/verification_report.json`. Record the performed check and inspectable evidence; an assertion that a gate passed is not evidence.

## Gate 1: Definitions and dimensions

Pass only if all symbols, dimensions, SI units, signs, frames, time bases, property states, and data ordering are explicit and consistent. Every additive term must have identical dimensions. Every transcendental function must receive a dimensionless argument.

## Gate 2: Conservation and admissibility

Check mass, species, momentum, energy, charge, and entropy balances as applicable. Verify interface jump conditions, source terms, work and heat signs, positive material properties, realizability, and nonnegative entropy production when required.

## Gate 3: Assumptions and scale ordering

Trace every deleted, combined, or modeled term to a declared dimensionless ordering or evidence. Check the expected reduction error, interactions among assumptions, and conditions that invalidate the ordering.

## Gate 4: Frame, transformation, and invariance

Verify the coordinate and physical frame, fictitious forces, tensor transformations, and applicable invariants. Use Galilean invariance for ordinary thermal fluids; require a documented `U/c` or electrodynamic-covariance rationale before using a Lorentz transformation.

## Gate 5: Limits and asymptotics

Test zero and infinite forcing, vanishing and dominant transport coefficients, equal phase properties, dilute and dense limits, large and small geometry, steady limits of transient models, and reduced-dimensional limits. Classify every singular limit as physical, removable, or evidence of invalid scope.

## Gate 6: Baseline recovery

Recover accepted results only inside their stated regimes. A model that cannot recover a credible baseline needs a documented physical reason and discriminating evidence. Do not force recovery by fitting a regime-dependent coefficient and calling it universal.

## Gate 7: Closures and identifiability

For each closure, state whether it is derived, measured, reported, correlated, fitted, assumed, or unknown. Check parameter redundancy, covariance, practical identifiability, independent measurability, and whether target data were used both to define and validate the closure.

## Gate 8: Algebra, code, and numerics

Reproduce symbolic steps, unit conversions, numerical constants, and transformations independently. Test code with analytic or manufactured cases. Check precision, convergence, conditioning, discretization error, and deterministic ordering where relevant.

## Gate 9: Mathematical prerequisites and solution conditions

Check equation classification, initial and boundary data, regularity, existence or uniqueness requirements, transform convergence and inversion, eigenfunction completeness, branch and contour choices, asymptotic uniformity, and conditioning as applicable. A formal expression is not necessarily a well-posed or physically admissible solution.

## Gate 10: Evidence and novelty

Verify each material citation in the primary source. Confirm that the cited definition, equation, regime, and conclusion match the claim. Search for earlier equivalent mechanisms, nondimensional groups, transforms, counterexamples, corrections, and negative results.

## Gate 11: Calibration and external validation

Partition data by physical source of domain shift, not random rows alone. Keep calibration, model selection, and final validation separate. Report uncertainty in observations and properties, experimental variability, parameter uncertainty, numerical error, and model-form discrepancy separately when possible.

## Gate 12: Discrimination and causality

Ask whether another mechanism predicts the same terminal response. Require intermediate observables, temporal ordering, or interventions that distinguish causal accounts. A correlation that predicts a threshold does not by itself identify the triggering mechanism.

## Gate 13: Reporting integrity

Maintain a claim ledger linking each conclusion to an equation, source, computation, or measurement. Preserve contradictions and failed checks. State residual risk and the evidence needed for promotion to the next claim-ladder rung.

## Result rules

- `pass`: the check was performed and linked evidence supports the criterion.
- `qualified-pass`: overall package status when only nonblocking failed gates remain and their applicability or required action is explicit.
- `fail`: the check found a defect; assign a non-`none` severity and required action.
- `not-applicable`: provide a physical or mathematical rationale and evidence.
- `not-run`: the check has not been performed; it blocks promotion.
- `blocked`: the check cannot be completed with available authority, source, data, or computation; state what is needed.

## Severity rubric

- `fatal`: Invalidates the central derivation, mechanism, or claimed novelty.
- `major`: Changes the model form, dominant balance, scope, or principal conclusion.
- `repairable`: Local issue with a clear correction that does not change the governing mechanism.
- `applicability-limiting`: Valid result whose stated domain is too broad.
- `minor`: Presentation or reproducibility issue with no material physical effect.
- `none`: No defect was identified by the recorded check.

The package validator rejects stage promotion when any gate is `not-run` or `blocked`, or when an unresolved `major` or `fatal` failure remains. This is a consistency check on the record, not independent scientific validation.

Record every `major` or `fatal` failed gate in `blocking_findings` with a unique `F<number>` ID, the linked gate ID, matching severity, finding, and required action. A pass or qualified pass cannot retain a blocking finding.
