# Balance Audit

## Control volume, boundary motion, and flux signs

Use an annular liquid-layer control volume from `r` to `r+dr`, height `H`, beneath one nominal bubble. `r` is positive outward. `u_r<0` is inward capillary-fed liquid velocity. `j_e>0` is liquid-to-vapor volumetric evaporation per footprint area. The inner dry-spot edge is `ddry/2`; the outer bubble edge is `db/2`.

## Conserved quantities and integral balances

| Quantity | Storage | Advective flux | Non-advective flux | Volume source | Surface/interface source | Status |
|---|---|---|---|---|---|---|
| Liquid volume | Deleted by quasi-steady reduction | `2 pi r H u_r` | None | None | Distributed evaporation `2 pi r dr j_e` | Retained locally |
| Liquid momentum | Deleted in Darcy closure | Not resolved | Viscous resistance | None | Capillary pressure difference | Modeled by C1 |
| Energy | Not resolved locally | Not resolved | Solid/liquid conduction folded into `j_e` | Heater input not explicit | Latent heat maps `j_e` to heat flux | Closure C2 |

## Local equations and regularity

The retained local equation is `(1/r) d(r u_r)/dr + 2j_e/H = 0`; the Darcy closure is `dP/dr=-(mu/K)u_r`. With the stated pressure boundaries, imposing `Phi_w(ddry/2)=0` gives `R=1-[1+2 ln(1/x)]x^2`, where `R=8PcKH/(mu j_e db^2)` and `x=ddry/db`. This derivation requires `0<x<=1`; the logarithm is dimensionless. On this domain `R` is strictly decreasing from one to zero, so a positive root exists only for `0<R<1`.

## Frames, coordinates, and invariants

This is a stationary gravity-aligned laboratory-frame, depth-averaged axisymmetric model. No imposed translation is retained, so the result does not assert Galilean-invariant behavior under forced flow.

## Averaging or coarse-graining

The pillar field is homogenized into `K`, `H`, and a footprint-normalized `j_e`. The meniscus shape, local temperature field, and three-dimensional velocity are unresolved.

## Constitutive and interfacial closures

| Closure ID | Exact balance term closed | Relation | Provenance/status | Independent measurability | Failure regime |
|---|---|---|---|---|---|
| C1 | Momentum/viscous resistance | Darcy law with effective `K` | Assumed geometry correlation | Permeability/wicking experiment | Inertia, heterogeneous or non-Darcy arrays |
| C2 | Evaporation sink | Uniform effective `j_e` | Assumed meniscus closure | Local thermal/meniscus measurement | Nonuniform heater, bubble, or menisci |
| C3 | Outer length | `db=pi sqrt(sigma/[g Delta rho])` | Reported convention | Bubble-footprint imaging | Finite heater, coalescence, altered gravity |

## Nondimensional equations and scale ordering

| Term | Reference scale | Dimensionless coefficient | Retain/delete/model | Expected error | Evidence |
|---|---|---|---|---|---|
| Distributed evaporation | `j_e/H` | 1 | Retain | Spatial-closure error | C2 only |
| Darcy transport | `Pc K/(mu db)` | `R` | Retain | Permeability error | C1 only |
| Liquid storage | `H/t` | quasi-steady ratio unknown | Delete | Unquantified | No transient record |
| Inertia | `rho u^2` | pore Reynolds number unknown | Delete | Unquantified | No velocity record |

## Interface-transfer cancellation

Latent phase transfer is a sink for the liquid-only control volume and would cancel only in a combined liquid-vapor balance. The model does not resolve the vapor momentum or energy receiving that transfer.

## Boundary/initial-condition sufficiency

For `0<R<1`, the two pressure boundaries and zero inner flow specify the reduced solution. For `R>=1`, there is no positive dry-spot root; `x=0` is a declared saturation extension, not the same boundary-value problem. The executable branch must therefore be `x=solve(R)` for `0<R<1` and `x=0` for `R>=1`; attempting a generic zero search first can create a numerical warning even if the later branch overwrites the result.

## Global conservation residuals

The local volume balance integrates to total evaporation for a positive dry spot. No experiment-specific heater energy residual, heat loss, or transient solid storage residual was supplied.

## Unresolved balance defects

The manuscript must state the piecewise `R>=1` extension; otherwise it implies an unphysical positive root. It must also define whether `db` is a neutral or most-dangerous Rayleigh--Taylor wavelength convention.
