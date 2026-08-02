# Problem Contract

Use this contract before generating a new analytical model. Unknown information may remain `unknown`, but it must not be silently assumed.

## Required definition

1. **Decision or claim**: State exactly what the model must predict, bound, explain, or discriminate.
2. **Event definition**: Define how the transition, threshold, instability, failure, or response is identified experimentally or computationally.
3. **System boundary**: Identify included phases, components, interfaces, reservoirs, and external forcing.
4. **Regime**: State phase, flow, transport, equilibrium, dimensionality, compressibility, turbulence, radiation, rarefaction, and transient assumptions as applicable.
5. **Geometry and frame**: Give dimensions, orientation, coordinate frame, reference directions, and finite-size constraints.
6. **Materials or fluids**: Identify composition, state, surface condition, aging, contamination, and property sources.
7. **Operating conditions**: Give ranges and units for pressure, temperature, load, flux, flow rate, gravity, time, and other controls.
8. **Boundary and initial conditions**: State imposed and measured quantities and their uncertainty.
9. **Variables**: Define every symbol, dimension, SI unit, sign, role, property state, and evidence state.
10. **Baselines**: Record accepted theory, correlation, numerical solution, or limiting construction to beat or recover.
11. **Calibration boundary**: Declare which data may set constants and which cases remain sealed.
12. **Acceptance and falsification**: State quantitative pass/fail tests before selecting a mechanism.

## Scope test

Split the task when any candidate mechanism changes with:

- event definition;
- dominant phase topology;
- imposed versus natural flow;
- geometry or confinement class;
- transient versus quasi-steady forcing;
- continuum versus microscale assumptions;
- distinct dryout, burnout, instability, or damage processes.

## Claim ladder

Use the strongest justified label only:

1. dimensional possibility;
2. qualitative hypothesis;
3. scaling law;
4. closed analytical model;
5. calibrated correlation;
6. internally verified implementation;
7. validated in-domain model;
8. independently validated cross-domain theory.

A higher rung requires all lower-rung information plus new evidence. Predictive accuracy alone does not establish a correct mechanism.
