---
name: analytical
description: Develop, challenge, and validate analytical or mechanistic models in engineering and the physical sciences. Use for governing-equation derivations, scaling laws, nondimensional criteria, closure relations, instability thresholds, reduced-order theories, asymptotic models, theoretical thermal-fluid development, boiling and critical-heat-flux mechanisms, or any request to create, audit, falsify, or experimentally discriminate a physics-based model.
---

# Analytical

Build inspectable, falsifiable theories rather than plausible equations. Preserve the physical problem, evidence status, units, property states, applicability limits, and unresolved uncertainty from intake through validation.

## Select the mode

- `explore`: define the problem and generate genuinely different mechanisms.
- `derive`: develop one specified mechanism into a closed analytical model.
- `audit`: challenge an existing derivation, correlation, or claimed theory.
- `validate`: test a model computationally or against independent data.
- `full`: run the complete workflow. Use this by default for requests to develop a new model.

## Run the workflow

### 1. Establish the problem contract

Define the decision or claim, system boundary, regime, geometry, materials or fluids, operating conditions, initial and boundary conditions, dependent variables, governing variables, units, coordinate and sign conventions, property-evaluation states, assumptions, exclusions, baselines, uncertainty, and falsification conditions.

Do not combine physically distinct events under one target. For example, keep saturated pool-boiling CHF, subcooled departure from nucleate boiling, annular-film dryout, and confined-channel crisis separate unless a derivation explicitly connects them.

Read [problem-contract.md](references/problem-contract.md) and instantiate [problem-contract.json](assets/problem-contract.json) when producing a reusable research package.

### 2. Build the evidence and novelty map

- Trace established equations, correlations, constants, and mechanisms to primary sources.
- Record definitions, regimes, property states, data provenance, uncertainty, and applicability limits.
- Treat snippets, summaries, and model recollection as discovery aids, not evidence.
- Distinguish a new mathematical rearrangement from a new physical mechanism or prediction.
- Search deliberately for prior cross-domain formulations before claiming novelty.

Label important inputs and outputs as `measured`, `reported`, `simulated`, `derived`, `assumed`, `inferred`, `illustrative`, `screening-level`, `proposed`, `independently-validated`, or `unknown`.

Use [evidence-map.md](assets/evidence-map.md) for source-to-claim traceability.

### 3. Generate mechanism diversity

Generate at least five mutually distinct hypotheses when the scope permits. Vary the governing competition, not merely coefficients or fitting functions. Include relevant alternatives based on conservation, instability, competing timescales, topology or connectivity, interfacial physics, conjugate response, stochasticity, or an unexpected but physically defensible bridge from another field.

For each hypothesis record:

- governing competition and causal chain;
- required closures and observables;
- dimensional or asymptotic scaling skeleton;
- distinctive prediction;
- likely failure regime;
- decisive test;
- literature that could defeat the novelty claim.

Use [hypothesis-matrix.md](assets/hypothesis-matrix.md). Do not select a winner before the verification criteria are defined.

### 4. Derive independently

Develop promising mechanisms in separate reasoning contexts when feasible. Start from the relevant mass, momentum, energy, species, entropy, interfacial, constitutive, or geometric relations. For every approximation, state what term is neglected, the ordering that permits it, and the expected failure regime.

Do not use target data to choose the functional form before the model is dimensionally and physically closed. Separate universal constants, material properties, measurable state variables, nuisance parameters, and calibrated closures.

Request inspectable equations and claim provenance, not private chain-of-thought. Preserve failed routes when they reveal a bound, incompatibility, or discriminating experiment.

### 5. Apply verification gates

Read [verification-gates.md](references/verification-gates.md). At minimum check:

1. definitions, dimensions, units, signs, frames, and time bases;
2. conservation and thermodynamic admissibility;
3. limiting and asymptotic cases;
4. recovery of accepted baselines inside their regimes;
5. closure independence and parameter identifiability;
6. numerical or symbolic reproducibility;
7. citations and novelty;
8. uncertainty and sensitivity;
9. domain shift and extrapolation;
10. failure modes and residual risk.

Classify findings as `fatal`, `major`, `repairable`, `applicability-limiting`, or `minor`. Fix scientific-validity problems in the derivation, data, experiment, or model; do not repair them only by weakening prose.

### 6. Falsify computationally and empirically

- Compare against the simplest accepted baseline.
- Test dimensions and algebra symbolically where possible.
- Probe the parameter space for singularities, sign changes, nonphysical states, and discontinuities.
- Use synthetic cases with known answers before experimental data.
- Separate calibration from validation.
- Keep holdouts grouped by meaningful sources of domain shift such as fluid, material, surface, geometry, laboratory, pressure, or simulation family.
- Report residual structure, uncertainty, sensitivity, and failure cases, not only aggregate error.

Do not call a model validated because it fits the data used to construct or calibrate it.
Use [validation-summary.md](assets/validation-summary.md) to preserve the split, provenance, baseline, and residual evidence.

### 7. Synthesize without averaging mechanisms away

Select the simplest model that survives the gates and answers the scoped question. If different mechanisms dominate different regimes, construct a regime map or switching criterion with observable boundaries. Do not hide incompatible causal accounts inside an unconstrained blended correlation.

Report whether the outcome is a hypothesis, scaling law, closed model, calibrated correlation, screening tool, or independently validated theory. Use [model-card.md](assets/model-card.md) and [verification-report.md](assets/verification-report.md).

### 8. Design a discriminating validation

Identify conditions where surviving mechanisms make materially different predictions. Propose the smallest experiment or simulation matrix that can distinguish them, with controlled variables, synchronized observables, predicted directions or effect sizes, measurement uncertainty, predeclared acceptance criteria, and sealed validation cases.

Prefer intermediate mechanism measurements over the terminal response alone. Use [experiment-plan.md](assets/experiment-plan.md).

## Use independent roles

For complex `full` work, use independent agents or contexts when available:

- problem specifier and evidence mapper;
- several mechanism generators or derivation tracks;
- citation and novelty verifier;
- adversarial physics referee;
- computational falsifier;
- experiment designer;
- expert synthesis and final accountability.

Do not count a model judging its own derivation as independent validation. Give verification roles the raw problem, derivation, sources, and acceptance criteria without revealing the preferred conclusion.

## Route detailed guidance

- Read [prompt-library.md](references/prompt-library.md) for reusable prompts and role contracts.
- Read [thermal-fluids.md](references/thermal-fluids.md) for thermal-fluid invariants, boiling-crisis scoping, CHF baselines, and validation variables.
- Read [verification-gates.md](references/verification-gates.md) for the full pass/fail rubric.

## Produce a traceable package

For substantial work, produce the smallest applicable set:

```text
analysis-package/
|-- problem_contract.json
|-- evidence_map.md
|-- hypothesis_matrix.md
|-- derivations/
|-- model_card.md
|-- verification_report.md
|-- validation_summary.md
`-- experiment_plan.md
```

Validate staged packages with:

```bash
python scripts/validate_package.py <analysis-package> --stage contract
python scripts/validate_package.py <analysis-package> --stage theory
python scripts/validate_package.py <analysis-package> --stage verified
```

## Completion standard

Lead with the model status and engineering meaning. State what is directly verified, what remains proposed, the validity range, calibration dependence, uncertainty, contradictory evidence, and the smallest next calculation, dataset, simulation, or experiment needed. Never describe an unrun check, unavailable source, fitted explanation, or planned experiment as completed or validated.
