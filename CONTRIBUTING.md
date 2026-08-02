# Contributing to Analytical

Analytical welcomes contributions that make physics-based model development more traceable, falsifiable, and reproducible. Useful contributions include scientific defect reports, governing-physics guidance, public theory or benchmark records, completed examples, package templates, validator rules, tests, and documentation corrections.

## Before contributing

- Search existing issues and pull requests for related work.
- Use public material that you have the right to share.
- Do not submit confidential research, restricted or licensed data, credentials, reviewer identities, student records, or sponsor-controlled information.
- Preserve epistemic status. Distinguish measured, reported, simulated, derived, assumed, inferred, illustrative, proposed, and independently validated content.
- Prefer primary sources for governing theory, datasets, standards, and model definitions. A reachable URL or search result is not evidence that a claim is supported.

## Choose the right contribution path

- **Scientific or validation defect:** use the scientific-defect issue form for problems involving balances, dimensions, assumptions, closures, interfaces, mathematical validity, sources, benchmarks, leakage, or claim status.
- **Theory, model, data, or benchmark:** use the resource issue form and provide provenance, access conditions, regime, variables, units, uncertainty, and the specific role the resource could play.
- **Workflow or documentation improvement:** use the improvement issue form and describe the affected user task and an observable acceptance criterion.
- **Ready implementation:** open a focused pull request using the repository template.

## Scientific contribution standard

For a material change to physics or model guidance, identify:

1. the physical event, system boundary, regime, and affected claim;
2. variables, units, signs, coordinates, frames, and property-evaluation states;
3. the balance term, assumption, closure, or mathematical condition being changed;
4. supporting and contradictory primary evidence;
5. applicability limits, uncertainty, and failure modes;
6. dimensional, conservation, limiting-case, baseline, or benchmark checks;
7. whether the change is directly verified, derived, reported, proposed, or illustrative.

Do not resolve a scientific-validity defect only by softening the wording. Repair the derivation, evidence, data, validation, or experimental design when required.

## Local development and checks

The package scripts and tests use the Python standard library. From the repository root, run:

```bash
python scripts/check_skill.py
python -m unittest discover -s tests -v
python scripts/validate_package.py examples/steady-wall-conduction --mode derive
python scripts/validate_package.py examples/saturated-pool-chf-audit --mode audit
python scripts/check_resources.py --max-age-days 365
```

If changing a script, add or update a regression test. If changing a schema, template, mode contract, or validation rule, verify every bundled example and confirm that older packages are either explicitly supported or explicitly rejected with migration guidance.

For public-resource changes, also run the online reachability check when network access is available:

```bash
python scripts/check_resources.py --max-age-days 365 --online
```

Reachability does not validate the scientific content of a source; inspect the supporting passage and record its evidence role.

## Pull requests

Keep each pull request focused. In the description:

- state what changed and why;
- identify affected modes, artifacts, schemas, or scientific regimes;
- list commands actually run and their results;
- separate scientific evidence from software checks;
- disclose remaining limitations and unrun checks;
- confirm that no confidential or restricted material is included.

Maintainers may request a smaller change, additional primary evidence, a balance or dimensional audit, a benchmark, or an independent forward test before merging.
