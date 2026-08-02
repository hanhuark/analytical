# Analytical Model Card

## Status and claim-ladder rung

Derived closed analytical model, claim-ladder rung 4. It is not experimentally validated.

## Scoped physical question

Predict `T(x)` and `q_x` in a constant-k plane wall with `T(0)=T_H`, `T(L)=T_C`, and no internal generation.

## Governing mechanism

Steady energy conservation makes conductive heat flux spatially constant; Fourier closure then makes the temperature gradient constant.

## Equations and variable definitions

`d(q_x)/dx=0`, `q_x=-k dT/dx`, `T(x)=T_H-(T_H-T_C)x/L`, and `q_x=k(T_H-T_C)/L` with `q_x>0` toward the cold face.

## Conservation-law ancestry and balance residuals

The local equation follows from a stationary slice balance. The global residual `A[q_x(0)-q_x(L)]` is exactly zero.

## Assumptions, scale orderings, and closures

Assumptions A1-A4 and closure C1 are recorded in the package. Physical application requires their independent support.

## Mathematical method and solution conditions

Direct integration of a linear second-order ODE with two Dirichlet conditions. `k>0` and `L>0` ensure a unique regular solution.

## Parameter provenance and calibration

`k`, `L`, `T_H`, and `T_C` are inputs. No parameter is calibrated to the solution.

## Dimensional and conservation checks

`k DeltaT/L` has units `W m^-2`; substitution gives zero ODE and boundary residuals. Heat flows toward decreasing temperature.

## Limiting cases and baseline recovery

`T_H=T_C` gives zero heat flux and a uniform temperature. Increasing `L` at fixed temperatures reduces flux as `1/L`.

## Validation evidence and uncertainty

Only internal analytical verification is provided. An application must propagate uncertainty in the four inputs and test edge/contact/property effects.

## Public resources, existing models, and benchmark provenance

Resource R1 provides public instructional context. The exact solution itself is derived locally and is used as a software-verification benchmark.

## Known failures, exclusions, and domain shift

The model can fail for transient storage, lateral loss, generation, contact resistance, anisotropy, strong `k(T)`, or nonlocal transport.

## Reproducible implementation

Evaluate `T(x)=T_H-(T_H-T_C)x/L` and `q_x=k(T_H-T_C)/L`; independently substitute into the ODE and boundary conditions.

## Smallest next decisive test

For a proposed physical wall, estimate Fourier time, aspect ratio, conductivity variation, and contact resistance before comparing measured profiles.
