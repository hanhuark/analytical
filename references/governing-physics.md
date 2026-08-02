# Governing Physics and Assumption Audit

Use this reference to move from fundamental conservation laws to a reduced model without losing the physical meaning of discarded terms.

## Contents

- [Start with a transport statement](#start-with-a-transport-statement)
- [Canonical local balances](#canonical-local-balances)
- [Interfaces and phase change](#interfaces-and-phase-change)
- [Balance-to-model hierarchy](#balance-to-model-hierarchy)
- [Common assumptions and evidence](#common-assumptions-and-the-evidence-they-require)
- [Frames and transformations](#frames-and-transformations)
- [Boundary, initial, and closure sufficiency](#boundary-initial-and-closure-sufficiency)
- [Minimum balance audit](#minimum-balance-audit)

## Start with a transport statement

For a control volume that may move with boundary velocity `w`, write a generic extensive balance using one declared flux convention:

```text
d/dt integral_CV(rho phi dV)
+ integral_CS [rho phi (u - w) + j_phi] dot n dA
= integral_CV s_phi dV + integral_CS s_phi,A dA
```

Here `phi` is the specific conserved quantity, `j_phi` is its non-advective outward flux, and the `s` terms are volumetric and surface sources. Define signs before specializing this equation. State the regularity needed to use Reynolds transport and divergence theorems.

## Canonical local balances

Use equations consistent with the chosen sign convention and formulation.

### Total mass

```text
partial rho/partial t + div(rho u) = S_m
```

Set `S_m = 0` only for a closed nonrelativistic total-mass balance without modeled mass injection. Phase change transfers mass between phases but does not create total mass.

### Species mass

```text
partial(rho Y_k)/partial t + div(rho Y_k u + j_k) = omega_k + S_k
```

Require `sum_k Y_k = 1`, `sum_k j_k = 0` in the mass-average frame, and reaction/source consistency with total mass.

### Linear momentum

```text
partial(rho u)/partial t + div(rho u tensor u) = div(sigma) + rho b + f_other
sigma = -p I + tau
```

Distinguish pressure, viscous or non-Newtonian stress, body force, interphase momentum exchange, capillary stress, electromagnetic force, and porous resistance. Angular-momentum balance implies a symmetric Cauchy stress only when couple stresses and body couples are absent.

### Total energy

With `E = e + |u|^2/2` and conductive heat flux `q` positive in its vector direction:

```text
partial(rho E)/partial t + div(rho E u)
= div(sigma dot u - q) + rho b dot u + S_E
```

Derive internal-energy, enthalpy, sensible-enthalpy, or temperature forms from this equation. Track pressure work, viscous work and dissipation, kinetic and potential energy, latent heat, species diffusion enthalpy, radiation, Joule heating, reaction heat, and interfacial transfer. Never switch energy variables without transforming all terms and reference states consistently.

### Entropy admissibility

For a simple continuum, construct an entropy balance of the form

```text
partial(rho s)/partial t + div(rho s u + entropy_flux)
= entropy_supply + sigma_s,    sigma_s >= 0
```

Derive the formulation-specific entropy flux and production. Use the inequality to test constitutive signs and coupled transport; do not treat it as an optional conservation equation.

### Charge and fields

Use charge conservation and Maxwell equations only when electrical, magnetic, plasma, electrohydrodynamic, or relativistic effects materially couple to the model:

```text
partial rho_e/partial t + div(J) = 0
```

Track electromagnetic energy and momentum consistently rather than inserting a Lorentz-force term alone.

## Interfaces and phase change

For each moving interface, define its normal, velocity, surface storage, and jump convention. Derive mass, momentum, energy, species, and entropy jump conditions from a pillbox balance. Include as applicable:

- mass flux and Stefan velocity;
- traction and surface-tension curvature terms;
- tangential Marangoni stress;
- latent heat and interfacial heat fluxes;
- kinetic, capillary, or nonequilibrium temperature jumps;
- contact-angle and contact-line laws;
- interfacial area transport and topology change.

Equal temperature, local saturation, no slip, no mass transfer, and mechanical equilibrium are separate assumptions. Do not collapse them into a generic `equilibrium interface` label.

### Sign-explicit sharp-interface starting point

For a liquid-vapor interface `Gamma(t)`, let `n` point from liquid `l` to vapor `v`, let `u_I` be the interface velocity, and define `[[a]] = a_v - a_l`. Define positive evaporation mass flux by

```text
m'' = rho_l (u_l - u_I) dot n = rho_v (u_v - u_I) dot n > 0.
```

With zero surface mass, momentum, and energy storage, the corresponding jump skeleton is

```text
[[rho (u - u_I) dot n]] = 0

[[m'' u - sigma dot n]] = div_s(gamma P_s) + f_s

[[m'' (e + |u|^2/2) - (sigma dot u) dot n + q dot n]] = q''_Gamma

[[m'' s + J_s dot n]] = s''_Gamma + sigma''_Gamma,   sigma''_Gamma >= 0
```

Here `P_s = I - n tensor n`, `gamma` is surface tension, `f_s` is any additional declared surface force, `q''_Gamma` is declared interfacial energy supply, `J_s` is non-advective entropy flux, `s''_Gamma` is entropy supply, and `sigma''_Gamma` is interfacial entropy production. For constant `gamma` and curvature convention `kappa = div_s(n)`, `div_s(gamma P_s) = -gamma kappa n`; the static normal-momentum limit then gives `p_l - p_v = gamma kappa` for a spherical liquid domain with outward `n`.

Do not insert `m'' h_fg = q''` independently of the total-energy jump. Derive the latent-heat form after declaring negligible kinetic/stress-work terms, pressure convention, property reference states, and any interfacial resistance. If surface excess mass, momentum, energy, or entropy is retained, add its material surface derivative and surface transport before reducing these equations.

For a conjugate solid-fluid boundary with one common spatial normal and conductive heat flux `q = -k grad(T)`, zero interfacial energy storage requires continuity of normal total energy flux. Temperature continuity is an additional perfect-contact assumption. With an area-specific thermal contact resistance `R''_t`, use a sign-consistent relation such as `T_s - T_f = R''_t q_n` rather than imposing equal temperatures.

At a three-phase contact line, state whether the contact angle is equilibrium, advancing/receding, or dynamically closed. Young's equilibrium force balance, a dynamic contact-angle law, precursor-film treatment, slip length, and contact-line evaporation are distinct closures; do not combine them implicitly.

## Balance-to-model hierarchy

Record each transition explicitly:

| Level | Required record |
|---|---|
| Control-volume balance | Boundary motion, flux directions, surface and volume sources |
| Local equation | Smoothness, discontinuities, distributional or weak interpretation |
| Coordinate/frame form | Inertial or accelerating frame, metric/Jacobian, fictitious forces |
| Averaged equation | Time, ensemble, volume, phase, Favre, or surface average and unresolved correlations |
| Constitutive closure | Newtonian stress, Fourier/Fick transport, equation of state, kinetics, turbulence, interfacial laws |
| Nondimensional equation | Reference scales, dimensionless groups, retained coefficients |
| Reduced model | Ordering parameter, deleted terms, error estimate, revised boundary conditions |

An averaged equation is not the original equation with averaged symbols. Derive or document unresolved correlations and closure requirements.

## Common assumptions and the evidence they require

| Assumption | Required scale or test | Typical failure signal |
|---|---|---|
| Continuum | `Kn = lambda/L << 1` or independent continuum evidence | Rarefaction, temperature/velocity slip |
| Incompressible density | Small material density change; often `Ma << 1` plus bounded heating/composition effects | Acoustic coupling, strong thermal expansion, phase change |
| Boussinesq | Density variation small except in buoyancy term | Large property variation or stratification |
| Steady/quasi-steady | Observation and forcing times long relative to relaxation times; small Strouhal-type ratio | Hysteresis, phase lag, transient storage |
| Inviscid outer flow | Viscous terms asymptotically small away from layers | Separation, drag, boundary-layer control |
| Creeping flow | `Re << 1` with compatible unsteadiness | Inertial wake or convective acceleration |
| Boundary layer | `delta/L << 1` with ordered streamwise and normal gradients | Separation, strong curvature, interaction |
| One-dimensional | Transverse equilibration fast and transverse gradients bounded | Hot spots, secondary flow, finite-edge effects |
| Lumped temperature | `Bi << 1` for the chosen body and length scale | Internal thermal gradients |
| Constant properties | Sensitivity over the full state range is negligible | Near-critical, large-temperature, or phase-transition behavior |
| Negligible viscous heating | Brinkman/Eckert ordering supports omission | High shear, high speed, viscous liquids |
| Local phase equilibrium | Interfacial relaxation fast relative to forcing | Superheat, kinetic resistance, metastability |
| Local thermal equilibrium in porous/multiphase media | Interphase heat exchange time is short | Persistent phase-temperature difference |
| Newtonian/Fourier/Fick closure | Linear local response and material evidence | Memory, nonlocality, shear thinning, ballistic transport |
| Turbulence closure | Averaging definition, wall treatment, and calibration domain match | Anisotropy, transition, separation, multiphase coupling |
| Negligible radiation | Radiative-to-conductive/convective scale is small | High temperature or optically participating media |

Replace heuristic thresholds by an error budget or sensitivity study whenever the intended claim is consequential.

## Frames and transformations

- Use Galilean transformations for ordinary nonrelativistic inertial-frame changes. Verify that constitutive relations and reduced equations preserve material objectivity where required.
- Add Coriolis, centrifugal, Euler, and translational inertial terms in rotating or accelerating frames.
- Use Lorentz transformations only when `U/c` is not negligible for the required accuracy or when electrodynamic covariance or spacetime physics is central. For ordinary thermal-fluid systems, Lorentz corrections are normally far below modeling uncertainty; document that scale test rather than invoking relativity decoratively.
- Preserve tensor transformation rules under curvilinear coordinates and distinguish coordinate covariance from physical frame invariance.

## Boundary, initial, and closure sufficiency

Count dependent fields and independent equations after every reduction. Check compatibility and well-posedness for the PDE class. At conjugate boundaries enforce the appropriate continuity or jump in temperature, heat flux, velocity, traction, species flux, electric potential, or radiation. A constitutive relation does not replace an initial or boundary condition.

## Minimum balance audit

Before accepting a reduced model, confirm:

1. every retained term has a physical origin and consistent unit;
2. every omitted term has a declared ordering or evidence;
3. phase and interface source terms cancel in the total-system balance where required;
4. the energy variable and reference state remain consistent;
5. entropy production and material-property signs are admissible;
6. boundary and initial conditions match the reduced equation order;
7. the model recovers exact integral conservation on its stated domain;
8. a benchmark or measurement exists for each consequential assumption or closure.
