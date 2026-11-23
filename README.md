# Digital Transformation Operationalized Maturity Model

An evidence-based maturity model for assessing how an enterprise transforms its business and operating model into a digital business. It considers customer and ecosystem value, strategy, platforms, operations, organizational capabilities, and the intelligence required to adapt. Digital technology is treated as an enabler of business and operating-model change, not as the sole subject of transformation.

The model contains **6 dimensions, 23 subdimensions, 70 criteria and 350 evidence-anchored criterion-level statements**. Each criterion has five cumulative progression anchors. A full assessment requires evidence against the criteria and application of the model's advancement gates.

## Model identity and status

| Property | Value |
|---|---|
| Model | Digital Transformation Operationalized Maturity & Assessment Model |
| Canonical identifier | `dea:maturity-digital-transformation-operationalized` |
| Repository release | `2.0.1` |
| Model type | Maturity model |
| Assessment structure | 6 dimensions · 23 subdimensions · 70 criteria · 350 anchors |
| Capability scale | L-1 to L-5, with L-0 Not Assessed sentinel |
| Scoring scheme | `dea:maturity-bands-v2` v1.0.0 |

## What the model assesses

The model examines digital transformation as an enterprise-wide change in the way value is conceived, created, delivered and improved. It spans customer and ecosystem outcomes, strategic direction, digital platforms, operating practices, organizational readiness and decision intelligence. Its transversal levers include agentic AI, autonomy, digital twins and simulation, human-agent teaming, ecosystem platforms, trust and security, sustainability, composability, business value, innovation, governance and data intelligence.

The model is designed to assess the operationalization of digital business, rather than the presence of technology in isolation. Its criteria are organized into six weighted dimensions:

| Dimension | Weight |
|---|---:|
| Customer & Ecosystem Value | 20% |
| Digital Strategy & Business Model | 20% |
| Platforms & Architecture | 20% |
| Operations & Delivery | 15% |
| Organization & Culture | 10% |
| Data & Intelligence | 15% |

## Maturity scale and score bands

The model uses five maturity levels correlated to canonical capability levels L-1 through L-5. L-0 Not Assessed is an assessment sentinel, not a maturity level. The canonical v2 score bands are authoritative for active score resolution.

| Canonical level | Model state | Score range | Effort multiplier |
|---|---|---:|---:|
| L-1 | Emergent | 0–20 | 1.0× |
| L-2 | Structured | 21–45 | 1.5× |
| L-3 | Systematic | 46–70 | 2.5× |
| L-4 | Adaptive | 71–88 | 4.0× |
| L-5 | Self-Optimising | 89–100 | 6.0× |

The historical v1-alpha ranges (0–25, 26–50, 51–75, 76–90 and 91–100) remain in the model correlation metadata for lineage and compatibility. They are not used for current scoring or level resolution.

## Scoring method

Each criterion is rated from 1 to 5 against its evidence-anchored progression statements. The criterion score is mapped to a 0–100 value:

`criterion score = (rating - 1) / 4 × 100`

Scores are aggregated in three stages:

1. **Subdimension** — arithmetic mean of its criterion scores.
2. **Dimension** — arithmetic mean of its subdimension scores (equal weighting within the dimension).
3. **Overall** — weighted mean of the six dimension scores using the weights above.

The unrounded overall score is resolved against the canonical v2 bands. Rounding is for display only and must not change band resolution.

### Effort-adjusted value

The effort-adjusted value (EAV) is a supplementary index that makes the increasing effort associated with higher maturity bands explicit. It is not the 0–100 maturity score and does not determine the maturity level.

`EAV(S) = Σ [Pₖ(S) / Mₖ]`

Where `S` is the unrounded overall score, `Pₖ(S)` is the number of marginal score points allocated to band `k`, and `Mₖ` is that band's effort multiplier. Points are allocated progressively across the bands and counted exactly once:

| Band | Marginal score interval | Multiplier |
|---|---:|---:|
| Emergent | 0–20 | 1.0× |
| Structured | above 20–45 | 1.5× |
| Systematic | above 45–70 | 2.5× |
| Adaptive | above 70–88 | 4.0× |
| Self-Optimising | above 88–100 | 6.0× |

For example, an overall score of 73.8 allocates 20 points to Emergent, 25 to Structured, 25 to Systematic and 3.8 to Adaptive:

`EAV(73.8) = 20/1.0 + 25/1.5 + 25/2.5 + 3.8/4.0 = 47.62`

The theoretical maximum is approximately 53.17. EAV is reported to two decimal places; full precision is retained during calculation.

## Advancement and maturity determination

A score-band lookup is not, by itself, a complete maturity determination. The model also applies cumulative evidence and advancement controls:

- **Cumulative progression:** evidence for a claimed criterion level must also substantiate all lower anchors; levels cannot be skipped.
- **Mandatory-criterion gate:** a dimension's resolved level cannot exceed its lowest mandatory criterion level.
- **Enterprise weakest-link gate:** the overall level cannot exceed the lowest resolved dimension among d1–d4 (customer, strategy, platforms and operations).
- **Exit criteria:** the applicable model-level exit criteria must be met and evidenced.
- **Highest conformant level:** the final maturity level is the highest level for which the score band, mandatory criteria, dimension limits and exit criteria all conform.

The rapid self-assessment path uses one five-point question per subdimension and is indicative only. A full assessment requires criterion-level evidence and evaluation of all applicable gates.

## Auditable worked example

[`examples/digital-transformation-operationalized-2026.yaml`](examples/digital-transformation-operationalized-2026.yaml) provides a reproducible aggregation and band-resolution trace. It calculates an unrounded aggregate of **73.8**, resolves the score to the **Adaptive (L-4)** band, and calculates EAV as **47.62**.

The example deliberately identifies itself as a partial scoring demonstration. It uses dimension scores to demonstrate the arithmetic; it does not claim to represent a complete 70-criterion assessment and does not evaluate mandatory-criterion, cumulative-evidence, weakest-link or exit-criteria gates. Its band result must therefore not be interpreted as a final organizational maturity rating.

## Repository structure

```text
maturity-model-digital-transformation-operationalized/
├── model.yaml
├── standard.yaml
├── VERSION
├── README.md
├── CHANGELOG.md
├── maturity/
│   ├── scale.yaml
│   └── model/digital-transformation-operationalized.yaml
├── examples/
│   └── digital-transformation-operationalized-2026.yaml
├── scripts/
│   └── local_validate.py
└── .github/workflows/
    ├── local-model-ci.yml
    ├── contract-conformance.yml
    └── repository-standard.yml
```

## Validation sequence

The repository uses layered validation:

1. **Level 1 — local model validation:** run `python scripts/local_validate.py`. This checks the manifest and contract handshake, six-entry scale, model references, canonical v2 band resolution, dimension aggregation, marginal-band EAV arithmetic, boundary behavior and the worked-example trace.
2. **Level 2 — contract conformance:** `.github/workflows/contract-conformance.yml` checks the manifest handshake against the pinned Assessment-Models contract suite.
3. **Repository-standard conformance:** `.github/workflows/repository-standard.yml` checks the repository's declared structural conformance to [AM-MODEL-REPOSITORY-STANDARD](https://github.com/Assessment-Models/maturity-model-standard).
4. **Level 3 — ecosystem validation:** the model's registration is checked through the Assessment-Models registry workflow when registry changes are proposed.

A passing Level 1 result does not imply Level 2 or ecosystem conformance. Each gate reports its own outcome.

## Governance and provenance

This repository is the independently versioned home of the `dea:maturity-digital-transformation-operationalized` model within the [Assessment-Models](https://github.com/Assessment-Models) organization. Model identity, versioning, releases and assessment content are maintained here; shared assessment contracts and repository standards are maintained in their respective canonical repositories.

The model's criteria lineage is the committed Digital Transformation Operationalized register in the former `dea-catalog-maturity-models` source. The 6-dimension, 23-subdimension, 70-criterion and 350-anchor structure is retained. The historical score ranges remain documented for lineage only; active scoring uses the canonical v2 bands.

## License

MIT — see [LICENSE](LICENSE).
