# Changelog — maturity-model-digital-transformation-operationalized

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- CR-AM-06: make canonical v2 score bands authoritative for active score resolution; retain v1-alpha ranges only as lineage metadata.
- Define effort-adjusted value as the sum of marginal score points within each canonical band divided by that band's multiplier. EAV is supplementary and does not determine maturity level.
- Replace the previous whole-score-times-resolved-band calculation with auditable marginal-band contributions and boundary tests.
- Expand the worked example to show all six weighted dimension contributions, unrounded score resolution and EAV arithmetic; explicitly mark it as a partial scoring demonstration that does not evaluate assessment gates.
- Rewrite README as reader-facing model documentation, including scoring, advancement gates, worked-example scope and layered validation.


### Changed — BREAKING

- **Scale level renumbering adopted (dea-metamodel #214): `level-0-not-assessed` sentinel + capability levels `level-1..level-5` correlated to canonical L-1..L-5.** Release 2.0.0 — blocked on upstream ratification of dea-metamodel #214; do not merge before the renumbered canonical scale instance is released and CI pins are bumped.
  - Mapping: model level N maps to canonical L-N (the legacy offset convention — model N ↔ canonical N-1 — is retired); new `level-0-not-assessed` sentinel (0 points, not a capability level) added to scale.yaml, register `scale_levels` and the correlation mapping.
  - Unchanged: value-named level ids (`level-1-unrealized`…`level-5-leading`), level semantics, band instance `dea:maturity-bands-v2` v1.0.0 (ids, ranges, effort multipliers), 70 criteria and their numeric anchors 1..5, worked examples (band-keyed).
  - Comparability: historical index values and bands remain valid; only the canonical correlation labels shift (+1).
  - Lockstep consuming-side changes: VERSION/model.yaml/standard.yaml/assessment-manifest.json declare 2.0.0; scripts/local_validate.py validates the six-level scale with the Not-Assessed first-entry rule; README presents the aligned numbering.

## [1.0.1] - 2026-11-13

### Fixed

- Relationship edges in the model register now use only the upstream closed
  relationship-type vocabulary
  (`dea-metamodel/assessment-models/vocabulary/relationship-types.yaml`,
  CR-AM-11 section 17). The edge type `scored-by` was outside the vocabulary
  and is normalised to `scored-by-v2-bands`; the original value is preserved
  in `source_relationship_type`. No level, criterion, dimension or scoring
  content changed.


## [1.0.0] — 2026-11-13

### Added

- Initial release of the `dea:maturity-digital-transformation-operationalized` maturity model as an
  independently versioned asset, per the Assessment-Models organisation
  taxonomy (CR-AM-11 §8).
- Model-owned scale conforming to the published `maturity-scale.schema.json`:
  five levels, ordinals 0–4, `ordering: ascending`, linear topology with
  exponential progression, scored against the canonical v2 band instance
  (`dea:maturity-bands-v2` v1.0.0) — non-linear widths 20/25/25/18/12 and
  per-level effort multipliers 1.0 → 6.0.
- CR-AM-11 §15 contract handshake (`model.yaml`) declaring conformance to
  `maturity-scale-contract`, `maturity-model-contract` and
  `conformance-contract` against `technehub-labs/dea-metamodel`.
- Level 1 local model CI and Level 2 contract conformance workflows.
- Worked scoring example demonstrating canonical v2 band resolution and the
  effort-adjusted value.

### Notes

- Level semantics are carried verbatim from the authoritative source; only the
  scoring fields differ between the frozen v1-alpha lineage and the canonical
  v2 scheme.
