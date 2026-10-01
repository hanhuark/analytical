# Evidence and Novelty Map

| ID | Primary source or dataset | Verified identity | Specific claim supported | Evidence state | Definitions and regime | Applicability limits | Uncertainty or conflict | Verification status |
|---|---|---|---|---|---|---|---|---|
| E1 | Hu, Weibel, Garimella, IJHMT 136 (2019), DOI 10.1016/j.ijheatmasstransfer.2019.03.005 | yes, local PDF inspected | Global coupled wicking--evaporation baseline and its dry-spot relation. | reported | Saturated pool boiling on structured surfaces. | Does not establish local mass balance. | Characteristic-flux conventions must be retained exactly. | identity and equation inspected |
| E2 | Current user-provided working manuscript and supplementary document | yes, local DOCX/PDF render inspected | Local continuity derivation, `R(x)`, and candidate geometry calculations. | derived working draft | Homogeneous pillar arrays under declared assumptions. | Unpublished draft; not public validation evidence. | Data table and input provenance incomplete. | local audit only |
| E3 | Literature compilation package `test7_pool_boiling_CHF` | yes, local package and source records inspected | Source-audited experimental CHF/geometry assembly with fit-prohibited screening records. | reported and screening-level | Water pool boiling on micropillar arrays, with each record retaining source state and extraction status. | Forty-one plot-ready records are not prediction-ready; experimental points without supported closure inputs cannot validate a forward model. | Primary-source auditing, uncertainty recovery, and closure availability remain incomplete. | local compilation status inspected |
| E4 | Allred, Weibel, Garimella, *International Journal of Heat and Mass Transfer* 135 (2019) 403--412, [PII S0017931018351044](https://www.sciencedirect.com/science/article/pii/S0017931018351044) | yes, local author-supplied PDF inspected | Static and receding contact angles are physically distinct measurements and can evolve during boiling. | reported | Sessile-drop wetting characterization and pool-boiling study of smooth/coated reference surfaces. | Does not supply transferable wetting values for silicon micropillar arrays or validate the present local-balance model. | Measurement protocol and surface chemistry differ from the target arrays. | identity, table, and wetting-role discussion inspected |
| E5 | BoilingLab `micropillar_chf_local_balance` Figure 2 parity fixture and flat-angle-basis sensitivity run | yes, local code/tests and output inspected | Twelve MATLAB-exported Figure 2 rows reproduce in Python; intrinsic-versus-apparent flat-baseline change shifts the normalized ordinate but not `R` or `x`. | derived | Current Figure 2 closure chain, six source-audited circular-silicon screening points for angle sensitivity. | Internal parity and sensitivity do not establish source-wide accuracy or physical validity. | Result depends on the archived input fixture and stated wetting convention. | executable local tests passed |

## Search strategy and date

On 2026-09-21 through 2026-10-01, this audit inspected the locally supplied 2019 PDF, current manuscript, supplementary derivation, active MATLAB scripts, BoilingLab Python replica and regression fixture, the supplied wetting paper, and the source-audited literature-compilation status. It did not perform a complete novelty search or a source-by-source closure audit for every experimental record.

## Inclusion and exclusion criteria

Use only original experimental records with source locators, CHF event definition, pressure/state, geometry, surface/coating state, and declared extraction method for quantitative comparison. Exclude inferred contact angles, unresolved coating states, and values without a checkable figure/table/text location from prediction validation.

## Competing or contradictory evidence

Terminal CHF agreement can also arise from hydrodynamic, dry-spot-connectivity, contact-line, vapor-recoil, or conjugate-wall mechanisms. The local supply mechanism requires intermediate dry-area or radial-liquid-flow evidence to distinguish it.

## Novelty threats

Replacing a global balance by a local continuity balance is a mathematical and mechanistic extension only if the boundary conditions, closure domain, and discriminating prediction are explicit. A fitted master curve or terminal CHF comparison alone does not establish causal novelty.
