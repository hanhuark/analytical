# Balance Audit

## Control volume, boundary motion, and flux signs

Take a combined liquid-vapor control volume above the upward-facing heater. Heat flux is positive from solid to fluid; the interface normal points from liquid to vapor and positive interfacial mass flux denotes evaporation.

## Conserved quantities and integral balances

| Quantity | Storage | Advective flux | Non-advective flux | Volume source | Surface/interface source | Status |
|---|---|---|---|---|---|---|
| Total mass | Neglected only in a statistically stationary reduced argument | Liquid/vapor transport | Diffusion normally absent for pure total mass | Zero | Phase-transfer terms cancel in combined system | required ancestry, not resolved by terminal scaling |
| Momentum | Transient disturbance growth is implicit | Phase momentum transport | Pressure, viscous, and capillary stress | Gravity | Recoil/traction transfer cancels in combined system | reduced to hydrodynamic competition |
| Total energy | Heater/near-wall storage omitted by baseline | Enthalpy and kinetic transport | Conduction and stress work | External heater input | Latent/interfacial exchange cancels in combined system | reduced to `h_fg` evaporation scale |

The terminal correlation is not itself a complete local balance model; causal use requires reconstructing the instability derivation and interface conditions.

## Local equations and regularity

The source theory invokes liquid/vapor hydrodynamics and interface disturbance analysis. This audit does not replace those equations with the final dimensional formula.

## Frames, coordinates, and invariants

Use a stationary gravity-aligned laboratory frame. The formula is nonrelativistic and uses only scalar property magnitudes and body acceleration.

## Averaging or coarse-graining

The terminal CHF and inferred cell scale are aggregate quantities. Near-wall topology, microlayer, and conjugate-wall fields are unresolved and cannot be inferred from averaging alone.

## Constitutive and interfacial closures

| Closure ID | Exact balance term closed | Relation | Provenance/status | Independent measurability | Failure regime |
|---|---|---|---|---|---|
| C1 | Reduces instability/geometry details to one coefficient | `C_Z=pi/24` in the declared convention | Reported from Zuber baseline | Fixed from source, not measured per test | Different geometry, confinement, surface, flow, or coefficient convention |

## Nondimensional equations and scale ordering

| Term | Reference scale | Dimensionless coefficient | Retain/delete/model | Expected error | Evidence |
|---|---|---|---|---|---|
| Gravity-capillary competition | `sigma/l_c^2` | 1 by `l_c` definition | retain | property uncertainty plus model form | baseline derivation |
| Viscous effects | hydrodynamic inertial scale | not explicit in terminal formula | delete/model implicitly | unquantified | applicability limitation |
| Finite heater size | `lambda_RT,d` | `lambda_RT,d/L_h` | delete in infinite-domain form | unquantified if not small | must be reported |
| Conjugate wall storage | fluid hydrodynamic time | wall Fourier/effusivity ratios | delete | unquantified | requires separate test |

## Interface-transfer cancellation

Interphase mass, momentum, and energy exchange must cancel in the combined system. The final scaling alone cannot demonstrate that cancellation; the source derivation and any extension must retain sign-explicit jump conditions.

## Boundary/initial-condition sufficiency

The terminal formula does not encode heater dimensions, pool boundaries, power-ramp history, initial wetting, or conjugate-solid conditions. These must be supplied for application.

## Global conservation residuals

No experiment-specific mass or energy residual is available in this audit. A validation package must report heater power, heat loss, and transient storage closure.

## Unresolved balance defects

Viscosity, near-wall liquid supply, contact-line physics, finite geometry, and conjugate heating are unresolved; they are applicability limitations rather than silently zero terms.
