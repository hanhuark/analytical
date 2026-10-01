# Public Resource Register

| ID | Title and persistent identifier | Source type | Version/year | Access state | Access checked | Exact claim/equation/model supported | Regime | Evidence status | Limitations/license |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Hu et al., DOI 10.1016/j.ijheatmasstransfer.2019.03.005 | primary paper | 2019 | local-author copy | 2026-09-21 | Global wicking--evaporation balance and characteristic-flux definitions | Saturated pool boiling on structured surfaces | reported | Recheck the publisher version before public quotation or reproduction |
| R2 | NIST Chemistry WebBook SRD 69 | property database | accessed 2026-09-21 | public database | not queried in this audit | Declared saturation-property source for future records | State-specific properties | reported | Properties do not validate the CHF model |
| R3 | User-provided current manuscript and supplementary document | working document | current draft | confidential local source | 2026-09-21 | Local-continuity extension and working equations | Scoped local model | derived | Not a public evidence source or release asset |
| R4 | Allred, Weibel, Garimella, *International Journal of Heat and Mass Transfer* 135 (2019) 403--412, [PII S0017931018351044](https://www.sciencedirect.com/science/article/pii/S0017931018351044) | primary paper | 2019 | local-author copy; publisher page restricted | 2026-09-28 | Static/receding contact-angle distinction, measurement protocol, and boiling-induced wetting evolution | Pool boiling on smooth/coated surfaces | reported | Do not transfer its wetting values to silicon micropillar arrays; publisher rights apply |
| R5 | BoilingLab, [`theoretical-model/micropillar_chf_local_balance`](https://github.com/UARK-NED3/BoilingLab/tree/main/theoretical-model/micropillar_chf_local_balance) | public code repository | local audit 2026-09-28 | open code and local checkout | 2026-09-28 | Deterministic local-root implementation, 12-row Figure 2 MATLAB parity fixture, and angle-basis sensitivity | Current model implementation | derived | Internal code parity is not experimental validation; verify repository revision before reuse |
| R6 | Literature Compiler, [`examples/test7_pool_boiling_CHF`](https://github.com/hanhuark/literature-compiler/tree/main/examples/test7_pool_boiling_CHF) | public code/data-compilation repository | local audit 2026-09-28 | open code and local checkout | 2026-09-28 | Source-audited record schema and fit-prohibited separation | Water pool boiling on micropillar arrays | screening-level | Current records remain incomplete for forward prediction; verify source locators and rights before release |

## Search record

| Date | Database | Query | Filters | Material results | Negative/counter evidence |
|---|---|---|---|---|---|
| 2026-09-21 | Local supplied files | coupled wicking evaporation CHF | Current manuscript, supplementary derivation, MATLAB | Local relation `R(x)` and implementation paths | No source-level experimental validation table |
| 2026-09-28 | Local supplied files and repositories | static receding contact angle boiling; Figure 2 parity | Supplied wetting PDF, BoilingLab, Literature Compiler | Distinct wetting-input roles; limited MATLAB--Python parity; 41 plot-ready and 0 prediction-ready records | No source-wide dynamic-angle data or sealed validation set |

## Conflicting definitions, models, or findings

The working `db` equation corresponds to half the neutral Rayleigh--Taylor wavelength `2 pi sqrt(sigma/[g Delta rho])`, whereas a most-dangerous wavelength convention includes a factor `sqrt(3)`. The manuscript must name its convention rather than call both simply critical.

## Sources requiring access or identity verification

Every experimental paper used in the master curve needs original-source verification of geometry, coating/oxide state, pressure, CHF criterion, contact-angle basis, and uncertainty.
