# Assumption Ledger

| ID | Assumption | Type | Equation/term affected | Supporting scale or evidence | Expected error/order | Failure regime | Verification observable/benchmark | Status |
|---|---|---|---|---|---|---|---|---|
| A1 | Saturated pool boiling with negligible imposed flow | physical | Excludes subcooling and forced-convection terms | Declared boundary conditions and measured bulk state | Not quantified by baseline | Subcooling, mass flux, confinement | Pressure/temperature/flow measurements | proposed |
| A2 | Gravity-capillary hydrodynamic control | physical | Selects Zuber property group | Source derivation and capillary length | Model-form error unbounded a priori | Surface-controlled or supply-limited crisis | Wavelength/growth and intermediate topology | proposed |
| A3 | Infinite or sufficiently large heated domain | geometric | Permits periodic most-dangerous wavelength construction | `L_h/lambda_RT,d` must be large | Finite-domain correction unquantified | Small or patterned heaters | Heater-size sweep and finite-domain eigenproblem | proposed |
| A4 | Saturation properties define the relevant state | constitutive | Sets `h_fg`, densities, and `sigma` | Equilibrium-property database | Property uncertainty plus nonequilibrium discrepancy | Near-critical or strong interfacial nonequilibrium | State-resolved property sensitivity | proposed |
| A5 | Surface and conjugate-wall effects are secondary | physical | Deletes wickability, contact-line, and wall-storage closures | No universal support in terminal formula | Potentially order one | Structured/wetting surfaces or low-effusivity heaters | Surface/substrate interventions with synchronized fields | unverified |

## Interactions among assumptions

Finite heater size, surface patterning, and conjugate spreading can alter the observed structure wavelength and event detection, so they cannot be tested independently by terminal CHF alone.

## Assumptions inherited from source models or datasets

A2-A4 are inherited from the hydrodynamic baseline. Any validation dataset also brings its heater, conditioning, property, detection, and heat-loss assumptions.

## Sensitivity and removal tests

Vary `L_h/lambda_RT,d`, surface liquid-supply capacity, substrate effusivity/thickness, pressure, and gravity separately while monitoring wavelength, dry-area topology, and wall temperature before CHF.

## Assumptions that remain unverified

A1-A5 require experiment-specific support. In particular, A5 prevents treating the baseline as a universal causal theory.
