# Mathematical Toolkit for Analytical Modeling

Choose mathematics after defining the physical balance and desired prediction. State prerequisites and inversion, uniqueness, convergence, and conditioning requirements.

## Tool-selection map

| Physical or analytical need | Candidate tools | Required checks |
|---|---|---|
| Convert local to global information | Gradient, divergence, Stokes, and Reynolds transport theorems | Smoothness, orientation, moving boundaries, jump terms |
| Expose controlling parameters | Nondimensionalization, Buckingham Pi, scaling, dominant balance | Independent dimensions, scale choice, hidden geometry/property ratios |
| Solve coupled linear balances | Matrix factorization, eigenanalysis, generalized eigenproblems | Rank, conditioning, symmetry, positive definiteness, units under scaling |
| Identify dominant structures | SVD, proper orthogonal decomposition, low-rank approximation | Energy norm, weighting, truncation error, domain dependence |
| Solve linear initial-value systems | Matrix exponential, Laplace transform, convolution, Green functions | Causality, initial data, poles, region of convergence, inversion |
| Resolve periodic or spatial spectra | Fourier series/transform, Sturm-Liouville theory, spectral decomposition | Boundary conditions, completeness, aliasing, convergence at discontinuities |
| Treat cylindrical/spherical geometry | Hankel/Bessel, Legendre/spherical-harmonic expansions | Regularity at origin/axis, orthogonality weight, boundary spectrum |
| Evaluate hard real integrals | Complexification, residues, contour deformation, steepest descent | Analyticity, branch cuts, arc contributions, asymptotic validity |
| Map two-dimensional potential fields | Complex potential and conformal mapping | Analyticity, topology, boundary mapping, loss of 3-D/viscous physics |
| Obtain small/large-parameter behavior | Regular/singular perturbation, matched asymptotics, multiple scales, WKB | Uniform validity, secular terms, overlap, exponentially small effects |
| Determine threshold or instability | Linearization, normal modes, dispersion relations, energy methods | Base-state validity, spectrum, non-normality, finite-amplitude effects |
| Track qualitative state changes | Phase plane, bifurcation, center manifold, normal forms | Parameter identifiability, structural stability, hysteresis |
| Derive stationary principles | Calculus of variations, constrained optimization, adjoints | Admissible function space, boundary terms, convexity, second variation |
| Infer parameters or hidden states | Inverse problems, regularization, Bayesian inference, observability | Nonuniqueness, prior influence, noise model, sloppiness, validation leakage |
| Model variability or rare events | Probability, stochastic processes, Fokker-Planck, first passage, extreme-value theory | Stationarity, dependence, tail support, sample size, censoring |
| Model connectivity or morphology | Graph theory, percolation, topology, Minkowski functionals | Resolution dependence, finite-size scaling, causal interpretation |
| Transform frames and exploit symmetry | Galilean/rotating coordinates, Lie symmetries, dimensional invariance, Lorentz transformations | Preserved invariant, transformation domain, physical relevance |

## Core methods

### Calculus and integral methods

Use exact differentiation and integration where possible. Check differentiation under the integral sign, interchange of limits, convergence of improper integrals, boundary contributions, and singular measures. Use weak or distributional forms for shocks, interfaces, point sources, and discontinuous fields.

### Linear algebra

Scale variables before interpreting matrix rank or condition number. Prefer solving linear systems over forming explicit inverses. Use eigenvalues for modal growth only when the operator assumptions support it; inspect eigenvectors, pseudospectra, and transient growth for non-normal systems. Use SVD for identifiability, observability, and low-rank structure.

### ODE and PDE theory

Classify equations and specify initial/boundary data before solving. Check existence, uniqueness, regularity, maximum principles, conserved quantities, energy estimates, characteristic directions, and shock or interface conditions as relevant. Distinguish a formal closed form from a physically admissible solution.

### Integral transforms and Green functions

Use Laplace transforms for causal initial-value problems, Fourier methods for translation-invariant or periodic structure, and geometry-matched transforms for radial domains. State transform conventions, convergence regions, boundary terms, inversion contours, poles, branch cuts, and distributional components.

### Complex variables

Use analytic functions, contour integration, residues, analytic continuation, and conformal maps when their analyticity and dimensional assumptions hold. Do not infer a three-dimensional, viscous, or nonlinear flow mechanism solely from a two-dimensional potential-flow mapping.

### Asymptotic and perturbation methods

Identify the small parameter from the nondimensional equations. State whether the expansion is regular or singular, its distinguished limit, matching region, remainder order, and range of uniform validity. Test asymptotic predictions against the unreduced equation or a high-accuracy numerical solution.

### Stability and nonlinear dynamics

Define the base state, perturbation norm, admissible modes, boundary conditions, and control parameter. Separate temporal from spatial growth, convective from absolute instability, linear threshold from nonlinear transition, and modal from non-modal amplification. A fitted threshold does not establish the instability mechanism.

### Symmetry and frame transformations

Use symmetry to identify invariants, similarity variables, conservation laws, and admissible functional forms. For nonrelativistic thermal fluids, Galilean transformations are normally the relevant inertial-frame test. Use Lorentz transformations only when the invariant spacetime interval and finite signal speed are physically material, such as relativistic flow or electrodynamics; first estimate `U/c` and the required error tolerance.

### Statistics, inverse problems, and uncertainty

Separate aleatory variability, measurement uncertainty, parameter uncertainty, numerical error, and model-form discrepancy. Check identifiability before calibration. Do not use the same observations to invent the model, select its form, estimate parameters, and claim validation.

## Open learning and reference resources

- [NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/) for definitions, identities, asymptotics, and computation of special functions.
- [MIT OCW Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) for linear systems, eigenanalysis, SVD, and matrix methods.
- [MIT OCW Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) for ODEs, systems, Fourier series, Laplace transforms, and stability.
- [MIT OCW Linear Partial Differential Equations](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/) for heat, wave, Laplace, Green-function, transform, and characteristic methods.
- [MIT OCW Complex Variables with Applications](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/) for complex integration, residues, conformal maps, and transform applications.
- [MIT OCW Lorentz Transformation lecture](https://ocw.mit.edu/courses/8-20-introduction-to-special-relativity-january-iap-2021/resources/lecture-4-4/) and [Einstein Online](https://www.einstein-online.info/en/explandict/lorentz-transformation-2/) for the relativistic transformation and its domain.

Use course material to understand a method, not as the sole primary source for a research novelty claim.

## Open computational tools

- [SymPy](https://docs.sympy.org/) for symbolic algebra, calculus, equation manipulation, transforms, and unit-aware checks.
- [SciPy](https://scipy.org/) for integration, linear algebra, optimization, interpolation, root finding, statistics, and differential equations.
- [mpmath](https://mpmath.org/) for arbitrary-precision and interval-supported numerical checks.
- [SageMath](https://www.sagemath.org/) for an integrated open mathematical system.

Preserve exact expressions until numerical evaluation is necessary. Record software version, precision, branch conventions, tolerances, and reproducible commands. Verify symbolic output by substitution, differentiation, limiting cases, or an independent implementation.
