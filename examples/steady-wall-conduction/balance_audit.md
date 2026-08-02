# Balance Audit

## Control volume, boundary motion, and flux signs

Use a stationary differential slice from `x` to `x+dx`. Positive conductive flux points in `+x`; no mass crosses the solid boundary.

## Conserved quantities and integral balances

| Quantity | Storage | Advective flux | Non-advective flux | Volume source | Surface/interface source | Status |
|---|---|---|---|---|---|---|
| Total energy | Zero at steady state | None in a stationary solid | `q_x A` through the two x faces | Zero | Prescribed face temperatures establish external heat exchange | retained |

The slice balance is `q_x(x)A-q_x(x+dx)A=0`, hence `dq_x/dx=0`.

## Local equations and regularity

Assume `T` is twice differentiable on `(0,L)` and continuous at the faces. With `q_x=-k dT/dx` and constant `k>0`, `d2T/dx2=0`.

## Frames, coordinates, and invariants

The stationary Cartesian frame is declared. Translating the origin does not change `dT/dx` or `q_x`.

## Averaging or coarse-graining

No averaging is used. One-dimensionality is a physical reduction, not an averaging operation.

## Constitutive and interfacial closures

| Closure ID | Exact balance term closed | Relation | Provenance/status | Independent measurability | Failure regime |
|---|---|---|---|---|---|
| C1 | Conductive energy flux | `q_x=-k dT/dx` | Fourier closure; assumed | `k` can be measured independently | Nonlocal, anisotropic, temperature-dependent, or ballistic transport |

## Nondimensional equations and scale ordering

| Term | Reference scale | Dimensionless coefficient | Retain/delete/model | Expected error | Evidence |
|---|---|---|---|---|---|
| Normal conduction | `k DeltaT/L^2` | 1 | retain | exact in stated problem | governing balance |
| Transient storage | `rho c DeltaT/t_ref` | Fourier-number inverse | delete by steady definition | physical startup excluded | problem contract |
| Lateral conduction | `k DeltaT/W^2` | `(L/W)^2` | delete | order `(L/W)^2` away from edges | large-aspect-ratio assumption |

## Interface-transfer cancellation

There is no internal interface. Energy entering the hot face equals energy leaving the cold face in the exact solution.

## Boundary/initial-condition sufficiency

The second-order ODE has two independent Dirichlet conditions. No initial condition is required for the steady boundary-value problem.

## Global conservation residuals

`R_E=A[q_x(0)-q_x(L)]=0` exactly.

## Unresolved balance defects

Physical edge losses and contact resistance are outside scope and must be bounded before application to a finite experiment.
