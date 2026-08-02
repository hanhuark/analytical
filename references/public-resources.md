# Public Resources for Theory and Existing Models

Use this atlas as a verified starting set, not an exhaustive or permanently current bibliography. Recheck access, version, licensing, and the actual supporting passage when a resource is used. Last curated: 2026-08-02.

For automated identity and staleness checks, use the companion [public-resource-registry.json](public-resource-registry.json). Copy only selected, problem-relevant entries into the analysis package and recheck their supporting content; the registry is discovery infrastructure, not frozen evidence.

## Evidence and access classes

Record one access state for every source:

- `open-full-text`: complete document can be read without institutional credentials;
- `open-data`: data files and metadata are downloadable or queryable;
- `open-code`: source and license are public;
- `metadata-only`: citation record is public but supporting content was not checked;
- `registration`: free account, token, or agreement is required;
- `restricted`: subscription, membership, benchmark agreement, or license is required;
- `unverified`: access or identity has not been checked.

Do not equate public access with peer review, correctness, applicability, or permission to redistribute.

## Search the progress of a theory

1. Search the exact phenomenon, governing competition, equation, dimensionless group, closure, and proposed cross-domain analogy.
2. Find the earliest formulation and the most recent review or assessment.
3. Follow references backward and citations forward.
4. Search for negative results, counterexamples, alternative mechanisms, errata, and validation failures.
5. Inspect existing code implementations to expose hidden closures and default coefficients.
6. Verify material claims in the primary paper, report, manual, source code, or dataset documentation.
7. Record query, date, version, DOI/report number, access state, regime, and the exact claim supported.

Metadata services are discovery aids. A DOI record or search result does not verify an equation or conclusion.

## Open technical repositories

| Resource | Best use | Evidence/access caution |
|---|---|---|
| [DOE OSTI.GOV](https://www.osti.gov/search-tools) | DOE reports, accepted manuscripts, datasets, code, and historical energy research | Check whether each record includes full text or only metadata |
| [NASA Technical Reports Server](https://ntrs.nasa.gov/) | Aerodynamics, heat transfer, fluids, space thermal systems, reports and data | Public and registered holdings differ |
| [U.S. NRC ADAMS](https://www.nrc.gov/reading-rm/adams) | Reactor thermal-hydraulic manuals, assessments, experiments, and regulatory records | Record accession number; some program material has access conditions |
| [IAEA INIS](https://nucleus.iaea.org/Pages/inis.aspx) | Nuclear science and engineering reports, proceedings, theses, and bibliographic records | Full text is available for a subset of records |
| [arXiv](https://arxiv.org/) | Rapid discovery of preprints and author manuscripts | Preprint status is not peer-review status; verify versions and final publication |
| [Crossref Metadata Search](https://search.crossref.org/) | DOI and bibliographic identity verification | Metadata does not verify article content |
| [OpenAlex](https://openalex.org/) | Open citation graph and forward/backward discovery | Aggregated metadata may contain errors; verify at the source |

## Open fundamentals

- [NASA Navier-Stokes equations](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/navier-strokes-equation/) provides an accessible mass-momentum-energy equation overview.
- [MIT OCW Continuum Electromechanics](https://ocw.mit.edu/courses/res-6-001-continuum-electromechanics-spring-2009/pages/open-textbook/) includes open chapters on continuum conservation, interfaces, constitutive laws, and coupled fields.
- [MIT OCW Advanced Fluid Mechanics](https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/) provides derivations of continuum fluid balances.
- [MIT OCW Introduction to Heat Transfer](https://ocw.mit.edu/courses/2-051-introduction-to-heat-transfer-fall-2015/) provides public heat-transfer fundamentals and modeling exercises.
- [NIST DLMF](https://dlmf.nist.gov/) provides an authoritative public mathematical-function reference.

Use these for definitions and derivation support. Use original papers and current primary literature for novelty or state-of-the-art claims.

## Open implementations and model documentation

| Resource | Model content | Use in an analytical audit |
|---|---|---|
| [OpenFOAM wall-boiling documentation](https://doc.openfoam.com/2606/tools/processing/boundary-conditions/rtm/derived/multiphase/alphatWallBoilingWallFunction/) | RPI-style heat-flux partitioning and selectable nucleation, departure, CHF, transition, and film-boiling submodels | Enumerate closures, coefficients, regime switches, and implementation assumptions |
| [MOOSE Navier-Stokes module](https://mooseframework.inl.gov/moose/modules/navier_stokes/intro/index.html) | Compressible, incompressible, porous, flow, and energy equations in an open multiphysics framework | Compare strong/weak forms, variables, closures, and boundary conditions |
| [NETL MFiX](https://mfix.netl.doe.gov/products/mfix/) | Open multiphase-flow models with theory guides, conservation equations, and constitutive relations | Audit averaging assumptions, interphase closures, and model hierarchy |
| [Turbulence Modeling Resource](https://tmbwg.github.io/turbmodels/) | Public turbulence-model definitions and numerical-verification/experimental-validation cases | The resource moved from NASA Langley hosting to the TMBWG GitHub site in 2026; verify exact model equations, page version, and case provenance |
| [CoolProp](https://coolprop.org/) | Open thermophysical-property library based on documented formulations | Reproduce property evaluation while retaining source, state, and version |
| [NRC NUREG collections](https://www.nrc.gov/reading-rm/doc-collections/nuregs/pubs/index) | Public code manuals, assessments, and safety research | Locate TRACE/RELAP and experiment assessments; verify exact report and version |

An implemented model is evidence of use, not proof of physical validity. Cite both the implementation/version and the primary model source.

## Resource-register requirements

For every material source record:

- persistent identifier or stable URL;
- title, authoring organization, year, and version;
- source type and peer-review status;
- access state and date checked;
- exact equation, mechanism, dataset, or claim supported;
- physical regime and property convention;
- limitations, conflicts, and known corrections;
- license or reuse constraints when code/data will be redistributed.

Never copy confidential, licensed, sponsor-restricted, or controlled material into an open package. Link to restricted resources only when their existence or access limitation is itself relevant.
