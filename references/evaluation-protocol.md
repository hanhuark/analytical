# Skill Effectiveness Evaluation

Use this protocol to measure whether `$analytical` improves scientific work rather than merely producing more artifacts. The machine-readable case set is [evaluation_cases.json](../tests/evaluation_cases.json).

## Paired benchmark design

1. Freeze the skill version, model version, tools, source-access policy, time limit, and token budget.
2. Run each case once without the skill and once with the skill in independent fresh contexts. Randomize order and prevent either run from seeing reviewer invariants or the paired output.
3. Remove condition labels and identifying boilerplate before review.
4. Use at least two blinded reviewers with thermal-fluid/modeling competence. Resolve material disagreements explicitly and report inter-rater agreement.
5. Score physical correctness before style, length, or apparent sophistication.
6. Publish failures, abstentions, blocked checks, and resource use as well as successful cases.

## Scoring

Score every manifest dimension from 0 to 2 using its declared scale. Record separately:

- fatal and major balance, dimension, sign, boundary, or closure defects;
- unsupported assumptions and false validation/novelty/causality claims;
- recovery of required physical invariants and accepted baselines;
- source identity and passage verification;
- calibration leakage and physically grouped holdouts;
- falsifiable intermediate predictions and decisive tests;
- time, tool calls, tokens, and artifact burden;
- reviewer confidence and disagreement.

Do not combine a reduction in severe errors with increased time into one opaque score. Report scientific quality and efficiency separately.

## Regression rule

A release candidate fails if it introduces a new fatal error, increases false validation or causality claims, or loses a required invariant on a case previously passed. A release can remain blocked even when its mean score improves.

## Interpretation

The bundled cases are a designed challenge set, not evidence of population-wide performance. Add domain cases without changing previous expected invariants. Use third-party problems and independent reviewers before claiming broad generalization or public impact.
