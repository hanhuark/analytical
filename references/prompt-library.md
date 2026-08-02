# Prompt Library

Use these as role contracts. Replace bracketed fields with the problem contract and verified source corpus.

## Problem specifier

```text
Convert the research question into a precise analytical-model contract.
Define the physical event, system boundary, regime, geometry, materials or
fluids, operating ranges, initial and boundary conditions, variables with SI
units, sign conventions, property states, baselines, uncertainty, exclusions,
acceptance criteria, and falsifying cases. Label every input by evidence state.
Do not propose a universal model while physically distinct regimes remain mixed.
```

## Mechanism generator

```text
Generate at least five genuinely different mechanisms for [problem contract].
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
