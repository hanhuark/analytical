# Assumption Ledger

| ID | Assumption | Type | Equation/term affected | Supporting scale or evidence | Expected error/order | Failure regime | Verification observable/benchmark | Status |
|---|---|---|---|---|---|---|---|---|
| A1 | One axisymmetric bubble represents the CHF liquid-supply path. | geometric | Radial control volume and `db`. | Working-model scope only. | Unquantified. | Coalescence, percolation, finite heater. | Bubble/dry-area topology before CHF. | unverified |
| A2 | Array features are small relative to the bubble and homogenizable. | geometric | `K`, `H`, uniform `j_e`. | Required scale separation not reported per literature point. | Unquantified. | Sparse, graded, radial, mixed-wetting structures. | Direct resolved-flow or homogenization comparison. | unverified |
| A3 | Darcy transport is adequate. | constitutive | C1. | Effective-permeability correlation. | Inertia/tortuosity error unquantified. | High pore Reynolds number or entrance loss. | Independent permeability/wicking test. | reported closure |
| A4 | `j_e` is uniform over the wetted bubble footprint. | constitutive | Continuity sink. | Assumed. | Potentially order one. | Nonuniform heater, bubble, or meniscus field. | Spatial heat-flux/meniscus measurement. | unverified |
| A5 | Quasi-steady liquid balance applies. | physical | Deletes storage. | Assumed. | Unknown time-scale ratio. | Rapid heating or dry-spot transients. | Time-resolved dry-area and liquid-flow response. | unverified |
| A6 | Saturation properties and no subcooling apply. | physical | Properties and latent conversion. | Declared scope. | Out of scope, not small error. | Subcooled/pressurized nonequilibrium tests. | Bulk state record. | applicability-limiting |
| A7 | `x=0` for `R>=1` is an evaporation-limited saturation extension. | mathematical | Piecewise solution. | Derived domain of `R(x)`. | Does not predict a finite dry spot. | Claims about positive dry-spot flow above unity. | Independent dry-area measurement. | derived |
| A8 | Static contact angle affects only the declared Dhir--Liaw flat-CHF baseline; receding angle affects the evaporation closure. | closure/input-role | Flat baseline and `j_e`, not the local `R(x)` algebra. | Legacy Figure 2 code path and source-model convention. | Baseline ordinate can change while `R` does not. | Treating one angle as a universal wetting input. | Source-specific static/receding measurements or a documented common assumption. | partially source-audited |
| A9 | The Figure 2 conduction path retains the meniscus integral before applying an effective-conduction correction. | implementation | Effective `j_e` closure. | Active legacy flag `index_cond=1` and MATLAB-to-Python parity fixture. | Model-form error remains unquantified. | Describing the code as bypassing all meniscus integrations. | Direct code-path inspection and parity regression. | implementation-checked |

## Interactions among assumptions

Finite heater size, bubble coalescence, and nonuniform evaporation all alter the outer length and source distribution together. Contact angle, coating state, and permeability cannot be treated as independent when coating changes both wetting and flow passages. Switching the flat-surface angle from intrinsic to apparent changes the normalized comparison ordinate through `q''CHF,flat`, but it does not change the locally derived `R` or `x` when all structure closures are held fixed.

## Assumptions inherited from source models or datasets

The permeability and meniscus-evaporation relations are inherited closures. Reported literature CHF and geometry values do not independently establish the dynamic equilibrium/receding contact angles used as model inputs.

## Sensitivity and removal tests

Sweep `K`, `Pc`, `j_e`, `db`, and contact angles independently; then compare the predicted `R=1` boundary to measurements of dry-area fraction and CHF. Hold bulk properties fixed while changing wick geometry to test the liquid-supply mechanism.

## Assumptions that remain unverified

A1--A6 remain unverified for the target literature corpus. No model-predicted radial flow, dry-spot diameter, or spatial evaporation field has yet been compared to sealed data.
