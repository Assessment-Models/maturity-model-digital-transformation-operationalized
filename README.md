# Digital Transformation Operationalized Maturity Model

Digital-business maturity and assessment model. Positions digital transformation as the reimagining of the organization's business and operating model as a digital business: grounded in advanced digital technology adoption (AI, agentic AI, autonomous systems, composable cloud-native platforms, digital twins), expressed through novel operating models across all operating concerns, steered by customer- and ecosystem-centric digital strategy, and run as a deliberate working model between humans and software agents. Technology is an enabler, not the subject. Every criterion is MECE-placed, carries five evidence-anchored progression levels correlated to the org's canonical L-1..L-5 capability scale (L-0 Not Assessed), and is independently assessable.

## Status

`2.0.0` · adoption pending [dea-metamodel #214] — canonical v2 bands, scale renumbering adopted

## Placement

This repository is the independent home of the `dea:maturity-digital-transformation-operationalized` maturity
model. Under the Assessment-Models organisation taxonomy (CR-AM-11 §8,
`.github/GOVERNANCE.md`) a maturity model is an independently versioned asset
with its own releases, issues, roadmap and contributors.

Assessment-Models is categorically the home of **capability** assessment
assets. The maturity model for *enterprise architecture practice itself* is
owned by the DEA federation (`technehub-labs`), not by this organisation.

## Scoring scheme

Canonical v2 bands — `dea:maturity-bands-v2` v1.0.0
(`technehub-labs/dea-metamodel`). Non-linear band widths 20/25/25/18/12 with
per-level effort multipliers 1.0 → 6.0:

| Band id | Name | Range | Width | Effort multiplier | Legacy (v1) name |
|---|---|---|---|---|---|
| `level-1-emergent` | Emergent | 0–20 | 21 | 1.0× | Ad Hoc |
| `level-2-structured` | Structured | 21–45 | 25 | 1.5× | Defined |
| `level-3-systematic` | Systematic | 46–70 | 25 | 2.5× | Managed |
| `level-4-adaptive` | Adaptive | 71–88 | 18 | 4.0× | Quantitatively Managed |
| `level-5-self-optimising` | Self-Optimising | 89–100 | 12 | 6.0× | Optimising |

## Layout

```
maturity-model-digital-transformation-operationalized/
├── model.yaml                       # CR-AM-11 §15 contract handshake
├── standard.yaml                    # repository-standard declaration (CR-AM-ORG-RES-000)
├── VERSION
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── maturity/
│   ├── scale.yaml                     # model-owned scale (level-0-not-assessed + level-1..level-5)
│   └── model/digital-transformation-operationalized.yaml
├── examples/
│   └── digital-transformation-operationalized-2026.yaml
├── scripts/
│   └── local_validate.py            # Level 1 validator
└── .github/workflows/
    ├── local-model-ci.yml           # Level 1
    ├── contract-conformance.yml     # Level 2 (reusable from assessment-ci)
    └── repository-standard.yml      # repository-standard conformance (reusable)
```

## CI levels

1. **Level 1 — local model CI** (`.github/workflows/local-model-ci.yml`):
   runs `scripts/local_validate.py` — manifest contract, handshake shape,
   scale integrity, register-to-scale resolution, worked-example scoring math
   against the canonical v2 bands.
2. **Level 2 — contract conformance**
   (`.github/workflows/contract-conformance.yml`): reuses
   `Assessment-Models/assessment-ci/.github/workflows/contract-conformance.yml`
   to resolve the §15 handshake against the published contract suite at the
   pinned `dea-metamodel` release.
3. **Level 3 — ecosystem CI**: the registration record in
   `Assessment-Models/assessment-registry` is resolved by the ecosystem
   validator on every registry pull request.

The **repository-standard conformance workflow**
(`.github/workflows/repository-standard.yml`) runs alongside these levels as
an additive gate (CR-AM-ORG-RES-000).

## Repository standard

This repository declares adoption of
[AM-MODEL-REPOSITORY-STANDARD](https://github.com/Assessment-Models/maturity-model-standard)
v1.0.1 (CR-AM-ORG-RES-000) at conformance level **`structural`** via a root
`standard.yaml` declaration. `model.yaml` remains the authoritative identity
manifest; the standard workflow cross-checks `standard.yaml`, `model.yaml`,
`VERSION` and this README's Status line on every push and pull request. The
legacy self-named directory at the repository root is retained untouched
(migration matrix M4); deduplication is a separate owner decision.

## Provenance

`Assessment-Models/dea-catalog-maturity-models` — `maturity-models/v1-alpha/digital-transformation-operationalized.yaml` (the committed model, proposal 0003) plus `proposals/0003-…md` for the gap review. The criteria register (6 dimensions / 23 sub-dimensions / 70 criteria / 350 anchors) is carried verbatim.

Level semantics (characteristics, exit criteria, evidence) are carried
**verbatim** from the source; only the scoring fields differ between the
frozen v1-alpha lineage and the canonical v2 scheme.

## Licence

MIT — see `LICENSE`.
