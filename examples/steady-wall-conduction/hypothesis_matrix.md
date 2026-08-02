# Hypothesis Matrix

| ID | Mechanism and causal chain | Governing balances | Required closures | Scaling skeleton | Distinctive prediction | Failure regime | Decisive test | Novelty threats | Status |
|---|---|---|---|---|---|---|---|---|---|
| H1 | Local Fourier conduction transports energy down a constant temperature gradient | Steady total energy | C1 Fourier law | `q_ref=k DeltaT/L` | Linear `T(x)` and constant `q_x` | Variable/nonlocal k or unmodeled sources | Profile linearity plus global energy closure | Canonical result; no novelty | retained |
| H2 | Internal heat generation creates profile curvature | Steady total energy with source | Generation-rate closure | `q''' L^2/(k DeltaT)` | Nonzero `d2T/dx2` | Declared zero-generation problem | Independently measure generation and curvature | Not applicable unless source exists | rejected |

## Selection criteria fixed before evaluation

- Physical closure: Retain only mechanisms consistent with the declared zero-source wall.
- Baseline recovery: Recover a linear profile as generation and lateral loss vanish.
- Falsifiability: Curvature or flux imbalance falsifies H1 within the stated uncertainty.
- Identifiability: `k` must be independently specified; the exact profile alone cannot separate k from heat flux if neither is known.
- Validation boundary: This example verifies an analytical derivation, not a material law.
