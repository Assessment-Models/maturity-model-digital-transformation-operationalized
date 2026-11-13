# Changelog — maturity-model-digital-transformation-operationalized

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
