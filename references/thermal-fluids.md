# Thermal-Fluid Analytical Development

## Contents

- [Preserve the physical specification](#preserve-the-physical-specification)
- [Thermal-fluid reduction conditions](#thermal-fluid-reduction-conditions)
- [Boiling-crisis scoping](#boiling-crisis-scoping)
- [Mandatory pool-boiling baseline](#mandatory-pool-boiling-baseline)
- [Candidate mechanism families](#candidate-mechanism-families)
- [Mechanism-specific falsification signatures](#mechanism-specific-falsification-signatures)
- [CHF validation variables](#chf-validation-variables)
- [Decisive checks](#decisive-checks)

## Preserve the physical specification

Define the fluid and phase composition, pressure, temperature and reference state, geometry, orientation, gravity, imposed flow, heat and mass fluxes, conjugate solid, surface condition, initial and boundary conditions, and whether properties are local, bulk, film, wall, saturation, or reference-state values.

Derive phase and total mass, momentum, total/internal energy, species, entropy, interface jump, contact-line, solid-conduction, and constitutive relations as applicable. Require interphase mass, momentum, and energy transfers to cancel in the combined-system balance except for declared storage or external sources. Keep latent heat, sensible energy, pressure work, kinetic energy, viscous dissipation, conjugate storage, and radiation terms visible until scale analysis supports a reduction.

Check Reynolds, Prandtl, Nusselt, Péclet, Jakob, Weber, Bond, Capillary, Ohnesorge, Biot, Fourier, Mach, density-ratio, viscosity-ratio, property-variation, and geometry groups only when supported by the scoped balance. Record whether each group orders a deleted term, a boundary condition, a closure, or a response; a dimensionless group by itself is not a mechanism.

## Thermal-fluid reduction conditions

Audit at minimum:

- incompressible versus low-Mach versus compressible formulation;
- constant-density versus Boussinesq buoyancy treatment;
- steady, quasi-steady, periodic, or transient storage;
- laminar, transitional, RANS, LES, DNS, or unresolved turbulence;
- single-temperature versus separate phase/solid energy equations;
- equilibrium versus kinetic phase change;
- resolved interface versus averaged two-fluid, mixture, drift-flux, or heat-flux-partition model;
- one-dimensional, boundary-layer, axisymmetric, periodic, or finite-domain geometry;
- imposed wall temperature, imposed heat flux, conjugate heating, or finite thermal-mass boundary;
- constant versus state-dependent properties and the declared evaluation state.

For every reduction identify the omitted term, ordering parameter, expected error, and an observable or benchmark that can test it.

## Boiling-crisis scoping

Do not treat `CHF` as one universal event. Distinguish at minimum:

- saturated pool-boiling crisis;
- subcooled pool boiling;
- departure from nucleate boiling in forced flow;
- annular-film dryout;
- confined or microchannel crisis;
- transient power excursion;
- reduced-gravity or body-force-controlled boiling;
- surface-structure, wettability, wicking, or conjugate-heater effects.

Record how CHF is detected: imposed heat-flux limit, wall-temperature excursion, dry-area connectivity, irreversible dryout, heater failure, or another operational criterion. Preserve heating protocol and detection bandwidth.

## Mandatory pool-boiling baseline

For saturated, gravity-dominated pool boiling on a macroscale upward-facing surface, include the classical hydrodynamic scaling as a baseline:

```text
q''_CHF = C_Z h_fg rho_v^(1/2) [sigma g (rho_l - rho_v)]^(1/4)
```

Evaluate fluid properties at the declared saturation state unless another state is justified. Treat `C_Z` as a model-specific coefficient with documented convention, geometry, and source rather than a universal measured constant.

The corresponding derived nondimensional response is:

```text
Ku_CHF = q''_CHF /
         {h_fg rho_v^(1/2) [sigma g (rho_l - rho_v)]^(1/4)}
```

Use this as a benchmark, not as proof that hydrodynamic instability triggers every crisis.

Trace the convention to the primary source. A public starting point is Zuber's 1959 report, [*Hydrodynamic Aspects of Boiling Heat Transfer*](https://doi.org/10.2172/4175511), report AECU-4439. The commonly quoted infinite-horizontal-surface Zuber convention uses `C_Z = pi/24` (about `0.131`), but coefficient definitions differ with geometry, wavelength construction, and property convention; verify the exact equation in the source used rather than transferring the number by memory.

For the inviscid Rayleigh-Taylor wavelength convention used in many hydrodynamic CHF discussions, record

```text
lambda_RT,d = 2 pi [3 sigma / {g (rho_l - rho_v)}]^(1/2)
```

as a model-specific most-dangerous wavelength, not a universal observed bubble spacing. Also record the capillary length `l_c = [sigma/{g(rho_l-rho_v)}]^(1/2)` and the finite-heater ratio `L_h/lambda_RT,d`. When the heated dimension is not large compared with the assumed cell wavelength, the infinite-periodic-domain construction requires a finite-domain stability calculation or an applicability limitation.

Before numerical evaluation, archive the fluid-property query, saturation temperature or pressure, reference-state convention, units, and source version. Public NIST WebBook values or a versioned property library can reproduce the property state, but neither validates the CHF mechanism.

## Candidate mechanism families

Consider, without presuming equivalence:

- far-field or near-wall hydrodynamic instability;
- vapor-column, stem, or macrolayer dynamics;
- liquid-supply depletion and rewetting competition;
- microlayer and contact-line evaporation;
- dry-spot growth, coalescence, and connectivity;
- vapor recoil or evaporation momentum flux;
- capillary wicking and surface-structure transport;
- conjugate heater thermal response;
- stochastic nucleation and finite-area extreme events;
- imposed-flow entrainment, deposition, and film depletion.

Require every proposed bridge to explain an observable and to survive a novelty search. A cross-domain analogy is not a mechanism until mapped to dimensional physical variables and balances.

## Mechanism-specific falsification signatures

| Mechanism family | Intermediate prediction required before terminal CHF | Example discriminating intervention or failure signature |
|---|---|---|
| Far-field hydrodynamic instability | Dominant vapor/liquid structure wavelength and growth rate consistent with the stated dispersion relation | Change heater dimension relative to `lambda_RT,d`; failure of wavelength or finite-size prediction weakens the mechanism even if terminal CHF is fitted |
| Macrolayer or liquid-supply depletion | Measured liquid inventory or film thickness reaches a predeclared depletion condition before wall-temperature excursion | Change replenishment path while holding the classical property group nearly fixed |
| Dry-spot growth and connectivity | Dry-area clusters acquire a predicted size/connectivity transition before the terminal event | Change field of view/heater area and test finite-size scaling; a terminal threshold without the predicted topology is insufficient |
| Contact-line evaporation or vapor recoil | Local evaporation flux, contact-line density, and interfacial momentum scale predict where irreversible dry growth begins | Modify contact-line availability or local heat spreading while monitoring the intermediate response, not only CHF |
| Capillary wicking | Independently measured permeability/capillary-pressure/liquid-supply relation predicts rewetting capacity | Alter wick geometry or orientation at comparable bulk fluid properties; fitted wettability alone is not a transport closure |
| Conjugate heater feedback | Wall-temperature mode, substrate diffusion time, or effusivity predicts dry-patch survival and runaway | Change substrate thickness, effusivity, or power protocol while preserving the nominal boiling condition |
| Stochastic finite-area trigger | Event-time or maximum-dry-cluster distribution scales with area and observation time | Test independent heaters/runs and censored waiting times; frames within one run are not independent replicates |

A mechanism survives only when its intermediate prediction, timing, and intervention response are supported within uncertainty. Agreement with `q''_CHF` alone is not causal validation.

## CHF validation variables

Where feasible, collect synchronized:

- imposed and local heat flux;
- wall-temperature field and uncertainty;
- dry-area fraction, cluster size, connectivity, and residence time;
- nucleation-site density;
- bubble footprint, growth, departure, coalescence, and frequency;
- liquid-film or macrolayer thickness;
- contact angles and hysteresis under relevant dynamic conditions;
- surface roughness, porosity, permeability, wickability, aging, and contamination;
- substrate thickness, conductivity, heat capacity, and thermal effusivity;
- fluid properties with evaluation state and source;
- pressure, subcooling, mass flux, quality, gravity, orientation, and geometry;
- CHF detection method, heating history, and censoring or failure mode.

Group validation by experiment, surface specimen, fluid, pressure, geometry, and laboratory. Frame-level or time-window random splits do not establish transfer to new conditions.

## Decisive checks

- Does the model recover its declared gravity, capillary, inertial, viscous, and geometric limits?
- Does it distinguish surface-controlled from bulk-controlled behavior?
- Can fitted surface parameters be measured independently?
- Does one parameter merely absorb pressure, property, or laboratory effects?
- Are intermediate predictions correct before the terminal CHF value is compared?
- Can an intervention change the proposed mechanism while holding the baseline scaling nearly fixed?
