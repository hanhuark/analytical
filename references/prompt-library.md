# Prompt Library

Use these as role contracts. Replace bracketed fields with the problem contract and verified source corpus.

## Contents

- [Problem specifier](#problem-specifier)
- [Balance and assumption auditor](#balance-and-assumption-auditor)
- [Mechanism generator](#mechanism-generator)
- [Derivation track](#derivation-track)
- [Mathematical-method specialist](#mathematical-method-specialist)
- [Public-resource mapper](#public-resource-mapper)
- [Adversarial referee](#adversarial-referee)
- [Computational falsifier](#computational-falsifier)
- [Experiment discriminator](#experiment-discriminator)
- [Synthesis editor](#synthesis-editor)

## Problem specifier

```text
Convert the research question into a precise analytical-model contract.
Define the physical event, system boundary, regime, geometry, materials or
fluids, operating ranges, initial and boundary conditions, variables with SI
units, sign conventions, property states, baselines, uncertainty, exclusions,
conserved quantities, constitutive closures, frame/invariance, scale ordering,
benchmark plan, acceptance criteria, and falsifying cases. Label every input by evidence state.
Do not propose a universal model while physically distinct regimes remain mixed.
```

## Balance and assumption auditor

```text
Starting from an explicit moving or fixed control volume, write every applicable
integral mass, species, momentum, energy, charge, and entropy statement. Define
flux signs, sources, interfaces, frames, constitutive laws, and boundary data.
Trace each reduction to a dimensionless ordering. Create an assumption ledger
that names the affected term, error order, failure regime, and verification test.
Do not begin from a reduced textbook equation unless its assumptions are proved.
```

## Mechanism generator

```text
Generate three genuinely different mechanisms for a narrow question and at least
five for a substantial new-theory search, unless the scoped physics rules out
alternatives; state that reason when using fewer.
Vary the governing competition rather than coefficients. For each mechanism,
give the causal chain, balances and closures, dimensional scaling skeleton,
distinctive prediction, failure regime, decisive test, and prior literature
that must be ruled out before claiming novelty. Do not select a preferred idea.
```

## Derivation track

```text
Develop mechanism [ID] into a complete inspectable analytical derivation.
Start from the governing balances and interface or constitutive relations.
Define the control volume, units, signs, frames, property states, approximations,
orderings, closures, and calibration boundary. Check dimensions and limiting
cases at each stage. End with a nondimensional model, validity range, parameter
provenance, and quantitative predictions that could disprove it. Preserve gaps.
```

## Mathematical-method specialist

```text
Given the audited governing equations and target prediction, compare candidate
mathematical tools such as scaling, eigenanalysis, transforms, Green functions,
complex variables, asymptotics, stability, stochastic, variational, or inverse
methods. Select the smallest adequate method. State prerequisites, invariants,
boundary conditions, convergence/inversion conditions, conditioning, and failure
modes. Reject elegant methods whose mathematical or physical assumptions fail.
```

## Public-resource mapper

```text
Map current publicly accessible primary theory, technical reports, model manuals,
open implementations, contradictory evidence, and benchmark datasets for the
problem. Verify each actual source and record DOI/report/version, access state,
regime, exact supported claim, and limitations. Treat metadata and preprints as
discovery evidence unless their content and status support a stronger role.
```

## Adversarial referee

```text
Assume this derivation is wrong. Reconstruct its central steps independently.
Find dimensional, sign, conservation, thermodynamic, asymptotic, closure,
identifiability, citation, novelty, calibration, leakage, or domain-shift errors.
Test credible counterexamples and competing mechanisms. Classify findings as
fatal, major, repairable, applicability-limiting, or minor. Do not repair a
physics failure only by weakening the wording.
```

## Computational falsifier

```text
Implement the proposed model and its simplest accepted baseline reproducibly.
Use analytic or manufactured tests first. Sweep the declared parameter domain
for singularities, nonphysical states, sign changes, discontinuities, and limit
violations. Then evaluate sealed, physically grouped holdouts. Report residual
structure, uncertainty, sensitivity, calibration dependence, and failure cases.
Do not call calibration fit independent validation.
```

## Experiment discriminator

```text
Compare the surviving mechanisms and locate conditions where their predictions
separate most strongly. Design the smallest experiment or simulation matrix
that can discriminate them. Specify controls, synchronized intermediate
observables, expected directions and effect sizes, required uncertainty,
predeclared pass/fail criteria, and sealed validation cases. Prefer direct
mechanism observables over the terminal response alone.
```

## Synthesis editor

```text
Select the simplest model that survives the declared gates. Do not average
incompatible mechanisms into a black-box correlation. If dominance changes,
construct an observable regime map or switching criterion. Report the claim
ladder rung, equations, calibrated quantities, validity range, verification,
contradictory evidence, residual risk, and smallest next decisive test.
```
