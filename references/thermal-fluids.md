# Thermal-Fluid Analytical Development

## Preserve the physical specification

Define the fluid and phase composition, pressure, temperature and reference state, geometry, orientation, gravity, imposed flow, heat and mass fluxes, conjugate solid, surface condition, initial and boundary conditions, and whether properties are local, bulk, film, wall, saturation, or reference-state values.

Use mass, momentum, energy, species, entropy, interface jump, contact-line, and constitutive relations as applicable. Check Reynolds, Prandtl, Nusselt, Péclet, Jakob, Weber, Bond, Capillary, Ohnesorge, Biot, Fourier, Mach, density-ratio, viscosity-ratio, and geometry groups only when supported by the scoped balance.

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
