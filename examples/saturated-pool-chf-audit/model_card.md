# Analytical Model Card

## Status and claim-ladder rung

Reported classical scaling law, rung 3. The audit result is qualified: it is a useful baseline but not an independently validated universal mechanism.

## Scoped physical question

Assess the Zuber-form saturated pool-boiling CHF scaling for a gravity-dominated macroscale upward-facing heater.

## Governing mechanism

The source theory associates the boiling crisis with a hydrodynamic gravity-capillary-inertial limit of vapor/liquid structures.

## Equations and variable definitions

`q''_CHF=C_Z h_fg rho_v^(1/2)[sigma g(rho_l-rho_v)]^(1/4)`, with `C_Z=pi/24` only for the declared convention. The audit also records `lambda_RT,d=2pi[3sigma/{g(rho_l-rho_v)}]^(1/2)` as a model-specific wavelength.

## Conservation-law ancestry and balance residuals

Mass, momentum, interface, and energy ancestry is required, but the terminal formula does not itself close those balances. No experiment-specific energy residual was available.

## Assumptions, scale orderings, and closures

Assumptions A1-A5 and closure C1 define the scope. Finite heater, viscosity, surface, and conjugate-wall effects remain unresolved.

## Mathematical method and solution conditions

The hydrodynamic interpretation requires a valid base state, interface disturbance problem, admissible modes, and finite-domain assessment. A terminal dimensional fit is not a stability derivation.

## Parameter provenance and calibration

Fluid properties must be independently sourced at one declared saturation state. `C_Z` is fixed from the selected source convention and is not calibrated to validation cases.

## Dimensional and conservation checks

The property group has units `W m^-2`; density difference and all positive properties must remain physically admissible. Dimensional success does not identify the trigger.

## Limiting cases and baseline recovery

The formula tends to zero as `g` or `sigma` tends to zero and becomes singular in applicability near vanishing density contrast unless the full near-critical physics is reconsidered.

## Validation evidence and uncertainty

No sealed pool-boiling dataset was evaluated in this example. Property uncertainty, event uncertainty, experimental variability, and model discrepancy remain separate required quantities.

## Public resources, existing models, and benchmark provenance

R1 is the primary baseline starting point and R2 is a property source. Neither supplies independent causal validation across surfaces and heaters.

## Known failures, exclusions, and domain shift

Do not transfer this result directly to forced-flow DNB, film dryout, confinement, subcooling, reduced gravity, structured surfaces, or transient/conjugate crises.

## Reproducible implementation

Archive the exact source equation, coefficient convention, property queries, units, and `L_h/lambda_RT,d`; then compute the property scale without fitting target CHF data.

## Smallest next decisive test

Use a heater-size or substrate intervention that leaves the classical bulk property scale nearly fixed while measuring predicted wavelength, dry-area evolution, and wall-temperature timing before CHF.
