# Experimental Data and Benchmark Verification

Use the lowest-complexity evidence that can falsify the assumption, closure, or model claim. Public availability does not remove the need to audit provenance, uncertainty, and domain match.

## Evidence ladder

1. **Exact analytical case**: checks algebra and implementation in an idealized regime.
2. **Manufactured solution**: checks code order and equation implementation, not physical validity.
3. **High-accuracy reference solution**: checks numerical behavior for a specified mathematical problem.
4. **Separate-effects experiment**: tests one assumption, closure, or mechanism observable.
5. **Integral-effects experiment**: tests coupled system response under controlled conditions.
6. **Application benchmark**: tests prediction in the target configuration.
7. **Independent cross-domain validation**: tests transport across fluid, geometry, surface, laboratory, or operating regime.

Do not substitute code-to-code agreement for experimental validation when both codes share the same closure.

## Benchmark contract

Record before using any dataset:

- persistent identifier, version, creator, hosting repository, license, and access date;
- measured, simulated, or derived status for every field;
- geometry, material/fluid, surface, coordinate frame, and system boundary;
- operating, initial, and boundary conditions with units and uncertainty;
- instrumentation, calibration, sampling, bandwidth, synchronization, and detection rule;
- preprocessing, exclusions, corrections, derived quantities, and property sources;
- repeat count, variability, censoring, missingness, and covariance where available;
- calibration/model-selection/validation role and leakage group;
- domain relation to the intended application;
- checksum or immutable version identifier when files are downloaded.

Reject or downgrade a benchmark when consequential boundary conditions, units, geometry, provenance, or uncertainty cannot be recovered.

## Public starting resources

### Properties and reference states

- [NIST Chemistry WebBook fluid properties](https://webbook.nist.gov/chemistry/fluid/) provides public density, heat capacities, energy, entropy, viscosity, conductivity, sound speed, and saturation surface tension for selected fluids. Record the state convention and query conditions.
- [CoolProp](https://coolprop.org/) provides open, versioned property calculations. Cite the underlying formulation as well as the software version; cross-check consequential points against an independent source.

### Single-phase and turbulence verification

- [NASA Turbulence Modeling Resource](https://www.nasa.gov/nasa-turbulence-modeling-resource/) provides model definitions, grids, verification cases, experimental validation cases, and DNS/LES references.
- [Johns Hopkins Turbulence Database](https://turbulence.idies.jhu.edu/database) provides queryable DNS fields for several canonical flows. Some access paths require a token or account; record interpolation and differentiation options.

### Boiling and critical-heat-flux data

- [KTH/HWAT boiling two-phase-flow databank](https://doi.org/10.5281/zenodo.14627088) provides experimental boundary conditions and measured axial/radial profiles for LWR-relevant boiling flow. Treat it as flow-boiling evidence, not saturated pool-boiling evidence.
- [KAERI uniform and non-uniform heating CHF dataset](https://doi.org/10.5281/zenodo.18404759) provides a public digitized collection of 1,539 water tube-flow CHF cases derived from KAERI/TR-1665/2000. Treat the Zenodo files as a secondary digitization: verify definitions, corrections, and values against the cited technical report before consequential use.
- [NRC RBHT TRACE assessment, NUREG/IA-0480](https://www.nrc.gov/reading-rm/doc-collections/nuregs/agreement/ia0480/index) is a public report connecting reflood heat-transfer experiments with code assessment. Determine whether the report contains sufficient numerical data for the intended test; a plotted comparison alone is not a reusable raw dataset.

Search discipline-specific repositories for additional public pool-boiling, surface, and CHF data, but require a persistent identifier and benchmark contract. Publisher supplementary files may be public even when the article is not; verify reuse terms separately.

### Experimental design and uncertainty

- [BIPM/JCGM metrology guides](https://www.bipm.org/en/publications/guides) provide public guidance for measurement uncertainty and Monte Carlo propagation.
- [NIST Technical Note 1297](https://doi.org/10.6028/NIST.tn.1297) provides public NIST measurement-uncertainty guidance.
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) provides public experiment-design and statistical-analysis guidance.

## Assumption-to-test mapping

| Assumption or closure | Minimum useful evidence |
|---|---|
| Steady or quasi-steady | Time-resolved storage term or phase-lag bound |
| One-dimensional transport | Multi-location or field measurements bounding transverse gradients |
| Constant properties | State-resolved property sensitivity across the experiment |
| Local thermal equilibrium | Simultaneous phase/solid temperature measurements or exchange-time estimate |
| Interfacial equilibrium | Interfacial temperature/pressure or kinetic nonequilibrium estimate |
| Turbulence closure | Mean and fluctuation profiles, stresses, wall quantities, and independent geometry |
| Heat-flux partitioning | Synchronized wall temperature, phase topology, bubble/contact-line observables, and energy closure |
| CHF trigger mechanism | Intermediate dry-area, liquid-supply, film, interface, or instability observable before terminal excursion |
| Conjugate-heater simplification | Heater temperature field and substrate property/time-scale sensitivity |
| Universal coefficient | Cross-fluid, pressure, geometry, surface, and laboratory holdouts |

## Calibration and validation partition

- Group repeated frames, time windows, runs from one specimen, and data reduced with one calibration together.
- Seal validation cases before choosing the model form or coefficient.
- Preserve a baseline with no new calibrated parameters.
- Report interpolation separately from extrapolation.
- If data are too scarce for a sealed test, label the result calibrated or screening-level rather than validated.

## Comparison metrics

Use dimensional residuals and nondimensional residuals when both are informative. Report bias, spread, residual trends, coverage, and worst physically relevant errors. Weighting must reflect declared uncertainty or decision cost, not merely improve a headline score. Compare predicted intermediate observables before the terminal response.

## Uncertainty and discrepancy

Keep separate when possible:

- measurement uncertainty and calibration covariance;
- run-to-run and specimen-to-specimen variability;
- fluid-property and boundary-condition uncertainty;
- parameter-estimation uncertainty;
- numerical discretization and iterative error;
- preprocessing and event-detection uncertainty;
- model-form discrepancy and domain shift.

Propagate input uncertainty through the model and compare the predictive distribution with held-out observations. A confidence interval on a fitted mean is not a predictive uncertainty interval.
