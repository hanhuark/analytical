# Analytical Model Card

## Status and claim-ladder rung

Derived closed local-balance model, rung 4. The derivation and singular-limit repair are audited; predictive validation is not established.

## Scoped physical question

Under the declared Darcy, uniform-evaporation, and single-bubble assumptions, how does a local liquid-volume balance determine a dry-spot ratio and the structure-induced CHF enhancement of a homogeneous micropillar array?

## Governing mechanism

Evaporation progressively removes liquid from the inward radial wicking stream. Unlike a global-balance model with a radially constant wicking rate, the local model requires the flow rate to decline to zero at the dry-spot edge.

## Equations and variable definitions

`(1/r)d(r u_r)/dr+2j_e/H=0` and `dP/dr=-(mu/K)u_r` yield a velocity field satisfying `P(db/2)=Psat`, `P(ddry/2)=Psat-Pc`, and `Phi_w(ddry/2)=0`. Defining `x=ddry/db` and `R=phi_w,ch/phi_e,ch=8PcKH/(mu j_e db^2)` gives `R=1-[1+2 ln(1/x)]x^2`. The enhancement is `q''CHF,s=rho_l h_fg phi_e,ch(1-x^2)`, with `phi_e,ch=pi j_e/4`.

## Conservation-law ancestry and balance residuals

The local liquid-volume equation retains the evaporative sink. Its radial integral closes the wet annulus for `0<x<=1`. The model does not close a combined liquid-vapor momentum/energy system, and no experimental energy residual was available.

## Assumptions, scale orderings, and closures

The critical closures are Darcy permeability, uniform effective evaporation, and a Rayleigh--Taylor-based bubble-length convention. Their error and interactions are unquantified for the literature corpus; see the assumption ledger.

## Mathematical method and solution conditions

`R(x)` is continuous and strictly decreasing from one to zero on `0<x<=1`, so `0<R<1` has a unique positive root. `R>=1` has no positive root. It must be written piecewise as a dry-spot-free saturation extension rather than solved with an unconstrained root finder.

## Parameter provenance and calibration

The implementation uses declared saturation properties and geometry closures. The local equation is not fitted to CHF data. In the current manuscript comparison, contact angles, coatings, superheat, and bubble length are partly assumed; they must be separated from reported inputs. Static contact angle belongs to the Dhir--Liaw flat-CHF calculation, while receding contact angle belongs to the evaporation closure; intrinsic and apparent angles are alternative flat-baseline input bases, not interchangeable measurements.

## Dimensional and conservation checks

`Pc K H/(mu j_e db^2)` is dimensionless and `rho_l h_fg phi_e,ch` has W/m2. The local limit is `R->1` as `x->0`, removing the global model's divergence. The nomenclature must list dynamic viscosity in Pa s, not m2/s.

## Limiting cases and baseline recovery

At `R=0`, `x=1` and the structure-induced enhancement vanishes. As `R` approaches one from below, `x` approaches zero and the enhancement approaches `rho_l h_fg phi_e,ch`. The `R>1` branch does not increase the model enhancement. The global 2019 relation is a comparison baseline, not recovered by this local conservation law.

## Validation evidence and uncertainty

The current master-curve comparison is consistency evidence only: it derives the plotted enhancement by subtracting a modeled flat-surface CHF and normalizes it with a closure-based evaporation flux. A six-point source-audited circular-silicon screening subset found that changing only the flat baseline from intrinsic to apparent angle leaves `R` and `x` unchanged but shifts the plotted ordinate by 0.051--0.206. This is a sensitivity result, not a choice of the apparently better basis. The corpus has no sealed data split, source-level uncertainty for all inputs, generally reported receding angles, or an error metric. It does not validate the proposed mechanism.

## Public resources, existing models, and benchmark provenance

The 2019 model is the documented global-balance baseline. `test7_pool_boiling_CHF` is the required source-audited record for independent data assembly. No restricted experimental data or unpublished draft data are released in this audit package.

## Known failures, exclusions, and domain shift

Do not transfer to subcooled boiling, forced flow, finite or patterned heaters, mixed wettability, radial arrays, transient power ramps, or cases without independently defensible `K`, contact angle, `j_e`, and `db` inputs.

## Reproducible implementation

The BoilingLab Python example implements deterministic bracketing for `R(x)` and regression tests for the finite singular limit. A stored MATLAB export of 12 Figure 2 input rows is reproduced by the Python implementation; this establishes limited named-case implementation parity only. It neither certifies every MATLAB figure nor validates the physical evaporation, wicking, or wetting closures.

## Smallest next decisive test

For at least three square-array geometries spanning `R<1`, near `R=1`, and `R>1`, independently measure pressure/state, geometry, dynamic contact angles, wick permeability, dry-area fraction, and CHF. Predeclare the bubble-length convention and use one sealed surface/laboratory group for validation.
