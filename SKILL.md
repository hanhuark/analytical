---
name: analytical
description: Develop, challenge, and validate analytical or mechanistic models in engineering and the physical sciences. Use for conservation-law and governing-equation derivations, assumption audits, scaling laws, nondimensional criteria, closure relations, instability thresholds, reduced-order theories, asymptotic or transform methods, mathematical-physics analysis, theoretical thermal-fluid development, boiling and critical-heat-flux mechanisms, literature and model mapping, benchmark selection, or any request to create, audit, falsify, or experimentally discriminate a physics-based model.
---

# Analytical

Build inspectable, falsifiable theories rather than plausible equations. Preserve the physical problem, evidence status, units, frames, property states, applicability limits, and unresolved uncertainty from the fundamental balances through independent validation.

## Select the mode

- `explore`: define the problem and generate genuinely different mechanisms.
- `derive`: develop one specified mechanism into a closed analytical model.
- `audit`: challenge an existing derivation, assumption, correlation, or claimed theory.
- `validate`: test a model computationally or against independent data.
- `full`: run the complete workflow. Use this by default for a new model.

## Run the workflow

### 1. Establish the problem contract

Define the decision or claim, event, system boundary, regime, geometry, materials or fluids, operating conditions, initial and boundary conditions, dependent variables, governing variables, SI units, coordinates, signs, reference frame, property-evaluation states, uncertainty, exclusions, baselines, calibration boundary, and falsification conditions.

Do not combine physically distinct events under one target. For example, keep saturated pool-boiling CHF, subcooled departure from nucleate boiling, annular-film dryout, and confined-channel crisis separate unless a derivation explicitly connects them.

Read [problem-contract.md](references/problem-contract.md) and instantiate [problem-contract.json](assets/problem-contract.json) for a reusable package.

### 2. Construct the balance hierarchy

Begin with a control volume and the most general applicable conservation statements. Include mass, species, linear and angular momentum, total energy, charge, and entropy as applicable. Define storage, advective and non-advective fluxes, volume and surface sources, interfacial transfers, constitutive laws, and boundary conditions before reducing the equations.

Preserve this hierarchy:

1. exact integral balance;
2. local differential balance and regularity assumptions;
3. frame and coordinate representation;
4. averaging or coarse-graining operation;
5. constitutive and interfacial closures;
6. nondimensional form and scale ordering;
7. reduced governing equation.

Record every deleted, combined, or modeled term in [balance-audit.md](assets/balance-audit.md). Read [governing-physics.md](references/governing-physics.md) for canonical balances, interface conditions, and reduction tests.

### 3. Audit governing-equation assumptions

For each assumption state:

- the exact term or relation affected;
- its physical and mathematical meaning;
- the dimensionless ordering or evidence that supports it;
- whether it is local, global, constitutive, geometric, statistical, or numerical;
- the expected error order and failure regime;
- an observable or benchmark that can test it.

Do not use labels such as `steady`, `incompressible`, `one-dimensional`, `adiabatic`, `equilibrium`, or `negligible inertia` without connecting them to terms and scales. Keep assumptions distinct from boundary conditions, closures, measured facts, and numerical choices. Use [assumption-ledger.md](assets/assumption-ledger.md).

### 4. Build the evidence, model, and novelty map

- Search current, public, primary sources for the governing theory, prior mechanisms, accepted baselines, existing implementations, contradictory results, and validation data.
- Verify the actual source; treat snippets, metadata, repositories, preprints, and AI summaries according to their evidence role.
- Record definitions, regimes, property states, access conditions, version or date, provenance, uncertainty, and applicability limits.
- Distinguish a new rearrangement from a new mechanism, closure, observable prediction, or validated domain.

Label inputs and outputs as `measured`, `reported`, `simulated`, `derived`, `assumed`, `inferred`, `illustrative`, `screening-level`, `proposed`, `independently-validated`, or `unknown`.

Read [public-resources.md](references/public-resources.md). Use [resource-register.md](assets/resource-register.md) and [evidence-map.md](assets/evidence-map.md). Recheck online resources when used; bundled links are starting points, not frozen evidence.

### 5. Generate mechanism diversity

Generate at least five mutually distinct hypotheses when scope permits. Vary the governing competition, not merely coefficients or fitting functions. Include relevant alternatives based on conservation, instability, competing timescales, topology or connectivity, interfacial physics, conjugate response, stochasticity, or a physically defensible bridge from another field.

For each hypothesis record the causal chain, required balances and closures, scaling skeleton, distinctive prediction, likely failure regime, decisive test, and prior work that could defeat novelty. Use [hypothesis-matrix.md](assets/hypothesis-matrix.md). Do not select a winner before defining the verification criteria.

### 6. Select mathematics by the physical question

Choose the smallest mathematical tool that exposes the mechanism or makes a decisive prediction. Candidate tools include vector and tensor calculus, integral theorems, linear algebra, eigenanalysis, singular-value decomposition, ODE/PDE theory, Green functions, Fourier or Laplace transforms, complex variables and residues, conformal mapping, asymptotics, perturbation methods, calculus of variations, stability and bifurcation theory, symmetry and invariance, probability, stochastic processes, topology, optimization, and inverse methods.

Do not select a sophisticated method by analogy alone. State its prerequisites, transformed variables, inversion conditions, uniqueness or regularity assumptions, and failure modes. For ordinary thermal-fluid models, test Galilean invariance; use Lorentz transformations only when relativistic speeds, electrodynamic covariance, or spacetime physics is material. Read [mathematical-toolkit.md](references/mathematical-toolkit.md).

### 7. Derive independently

Develop promising mechanisms in separate reasoning contexts when feasible. Start from the audited balances, interface relations, and closures. At each reduction, check dimensions, signs, conservation, entropy admissibility, boundary conditions, well-posedness, and limiting cases.

Do not use target data to choose the functional form before the model is physically and dimensionally closed. Separate universal constants, material properties, measurable states, nuisance parameters, and calibrated closures. Request inspectable equations and claim provenance, not private chain-of-thought. Preserve failed routes when they reveal a bound, incompatibility, or discriminating test.

### 8. Apply verification gates

Read [verification-gates.md](references/verification-gates.md). Check definitions, dimensions, frames, conservation, thermodynamic admissibility, assumptions, asymptotic limits, accepted baselines, closure independence, identifiability, algebra, numerics, citations, novelty, uncertainty, domain shift, and failure modes.

Classify findings as `fatal`, `major`, `repairable`, `applicability-limiting`, or `minor`. Fix scientific-validity problems in the derivation, data, experiment, or model; do not repair them only by weakening prose.

### 9. Falsify computationally and empirically

- Use exact, manufactured, or synthetic cases with known answers before experimental data.
- Compare against the simplest accepted baseline.
- Probe the parameter space for singularities, sign changes, nonphysical states, discontinuities, ill-conditioning, and violated assumptions.
- Separate calibration, model selection, and sealed validation.
- Group holdouts by physical domain shift: fluid, material, surface, geometry, laboratory, pressure, forcing, or simulation family.
- Report residual structure, measurement uncertainty, variability, parameter sensitivity, numerical error, and model-form discrepancy separately.

Read [benchmark-data.md](references/benchmark-data.md), populate [benchmark-register.md](assets/benchmark-register.md), and use [validation-summary.md](assets/validation-summary.md). Do not call a model validated because it fits construction or calibration data.

### 10. Synthesize and design a discriminating study

Select the simplest model that survives the gates and answers the scoped question. If mechanisms dominate different regimes, construct an observable regime map or switching criterion. Do not hide incompatible causal accounts inside an unconstrained blend.

Report whether the result is a hypothesis, scaling law, closed model, calibrated correlation, screening tool, or independently validated theory. Use [model-card.md](assets/model-card.md), [verification-report.md](assets/verification-report.md), and [experiment-plan.md](assets/experiment-plan.md).

Identify conditions where surviving mechanisms make materially different predictions. Design the smallest experiment or simulation matrix with controlled variables, synchronized intermediate observables, predicted directions or effect sizes, measurement uncertainty, predeclared acceptance criteria, and sealed validation cases.

## Use independent roles

For complex `full` work, use independent agents or contexts when available:

- problem specifier and balance auditor;
- source, implementation, and dataset mapper;
- several mechanism generators or derivation tracks;
- mathematical-method specialist;
- citation and novelty verifier;
- adversarial physics referee;
- computational falsifier and benchmark curator;
- experiment designer;
- expert synthesis and final accountability.

Do not count a model judging its own derivation as independent validation. Give verification roles the raw problem, derivation, sources, data, and acceptance criteria without revealing a preferred conclusion.

## Route detailed guidance

| Need | Read |
|---|---|
| Physical contract and claim ladder | [problem-contract.md](references/problem-contract.md) |
| Conservation laws, interfaces, assumptions, and reductions | [governing-physics.md](references/governing-physics.md) |
| Mathematical theory and tool selection | [mathematical-toolkit.md](references/mathematical-toolkit.md) |
| Public theory, literature, and implementation resources | [public-resources.md](references/public-resources.md) |
| Experimental data, benchmarks, and uncertainty | [benchmark-data.md](references/benchmark-data.md) |
| Reusable role prompts | [prompt-library.md](references/prompt-library.md) |
| Thermal fluids, boiling crisis, and CHF | [thermal-fluids.md](references/thermal-fluids.md) |
| Pass/fail verification rubric | [verification-gates.md](references/verification-gates.md) |

## Produce a traceable package

For substantial work, produce the smallest applicable set:

```text
analysis-package/
|-- problem_contract.json
|-- balance_audit.md
|-- assumption_ledger.md
|-- evidence_map.md
|-- resource_register.md
|-- hypothesis_matrix.md
|-- derivations/
|-- model_card.md
|-- verification_report.md
|-- benchmark_register.md
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

Lead with model status and physical meaning. State the balances retained, assumptions tested, mathematical method, source and data provenance, what is directly verified, what remains proposed, validity range, calibration dependence, uncertainty, contradictory evidence, and the smallest next calculation, source check, benchmark, simulation, or experiment. Never describe an unrun check, unavailable source, fitted explanation, or planned experiment as completed or validated.
