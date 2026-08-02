# Assumption Ledger

| ID | Assumption | Type | Equation/term affected | Supporting scale or evidence | Expected error/order | Failure regime | Verification observable/benchmark | Status |
|---|---|---|---|---|---|---|---|---|
| A1 | Steady state | physical | Deletes `rho c partial T/partial t` | Observation time much longer than `L^2/alpha` | Transient correction decays with Fourier time | Startup or changing boundary temperatures | Time-resolved temperature or storage/conduction ratio | proposed |
| A2 | One-dimensional field | geometric | Deletes lateral derivatives | Heated lateral dimension `W` much larger than `L` and observation away from edges | Nominally order `(L/W)^2` | Edge cooling or localized heating | Multi-location temperature field | proposed |
| A3 | Constant isotropic k | constitutive | Makes `d2T/dx2=0` | Small property variation over `T_C` to `T_H` | First-order in relative k variation | Large temperature range or anisotropy | Independent k(T) data and profile curvature | proposed |
| A4 | Perfect face temperatures | boundary | Imposes Dirichlet conditions | Negligible contact resistance and uniform reservoirs | Set by boundary uncertainty | Contact resistance or nonuniform face heating | Surface temperature maps and contact-drop estimate | proposed |

## Interactions among assumptions

Contact resistance can mimic internal profile offsets, while lateral loss can mimic volumetric generation. They must be separated before attributing curvature to variable conductivity.

## Assumptions inherited from source models or datasets

No dataset is used. Fourier locality and continuum behavior are inherited from closure C1.

## Sensitivity and removal tests

Restore transient storage, lateral conduction, `k(T)`, or thermal contact resistance one at a time and compare their dimensionless corrections with the intended error tolerance.

## Assumptions that remain unverified

All physical assumptions remain proposed because this package is an exact mathematical derivation, not an experiment-specific validation.
