#!/usr/bin/env python3
"""Level 1 validation for the Digital Transformation Operationalized model.

Validates the manifest handshake, canonical six-entry scale, register references,
canonical v2 band resolution, marginal-band effort-adjusted value and the
traceability of the partial worked scoring example.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def load(rel: str):
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"missing file: {rel}")
        return {}
    try:
        return yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{rel}: invalid YAML: {exc}")
        return {}


manifest = load("model.yaml")
scale = load("maturity/scale.yaml")
register = load("maturity/model/digital-transformation-operationalized.yaml")
example = load("examples/digital-transformation-operationalized-2026.yaml")

# 1. Manifest shape and contract handshake.
for key in ("id", "type", "name", "version", "conformance"):
    if key not in manifest:
        errors.append(f"model.yaml: missing required field {key}")
if manifest.get("type") not in ("maturity-model", "assessment-model", "assessment-tool"):
    errors.append(f"model.yaml: invalid type {manifest.get('type')!r}")
conf = manifest.get("conformance") or {}
contract = conf.get("contract") or {}
source = conf.get("source") or {}
if not contract.get("id"):
    errors.append("model.yaml: conformance.contract.id is required")
if not conf.get("version"):
    errors.append("model.yaml: conformance.version is required")
if not source.get("organization") or not source.get("repository"):
    errors.append("model.yaml: conformance.source organization+repository are required")

# 2. Canonical scale structure.
EXPECTED_LEVELS = [
    "level-0-not-assessed",
    "level-1-unrealized",
    "level-2-proven",
    "level-3-standardized",
    "level-4-compounding",
    "level-5-leading",
]
actual_levels = scale.get("levels") or []
if len(actual_levels) != len(EXPECTED_LEVELS):
    errors.append(f"scale: expected {len(EXPECTED_LEVELS)} levels, found {len(actual_levels)}")
for ordinal, level in enumerate(actual_levels):
    if level.get("ordinal") != ordinal:
        errors.append(f"scale: {level.get('id')} ordinal {level.get('ordinal')!r}; expected {ordinal}")
    if ordinal < len(EXPECTED_LEVELS) and level.get("id") != EXPECTED_LEVELS[ordinal]:
        errors.append(f"scale: ordinal {ordinal} must be {EXPECTED_LEVELS[ordinal]!r}")
    if not level.get("name") or not level.get("definition"):
        errors.append(f"scale: {level.get('id')} requires name and definition")
if actual_levels and actual_levels[0].get("name") != "Not Assessed":
    errors.append("scale: ordinal 0 must be the Not Assessed sentinel")
if scale.get("ordering") != "ascending":
    errors.append("scale: ordering must be ascending")
progression = scale.get("progression") or {}
if progression.get("topology") != "linear" or progression.get("function") != "exponential":
    errors.append("scale: expected linear topology and exponential progression")

# 3. Register identity and scale references.
if register.get("repo_id") != manifest.get("id"):
    errors.append("register.repo_id must match model.yaml id")
if not register.get("id"):
    errors.append("register: canonical model id is required")
scale_ids = {level.get("id") for level in actual_levels}
for level_id in register.get("scale_levels", []) or []:
    if level_id not in scale_ids:
        errors.append(f"register: scale level {level_id!r} does not resolve")
scoring = register.get("scoring") or {}
if scoring.get("band_resolution", "").lower().find("canonical") < 0:
    errors.append("register: band_resolution must identify canonical v2 as authoritative")
description = scoring.get("description", "")
if "catalog bands (0-25" in description or "0-25 / 26-50" in description:
    errors.append("register: legacy v1 ranges must not be used for active scoring")
if scoring.get("dimension_weights") != {"d1": 0.2, "d2": 0.2, "d3": 0.2, "d4": 0.15, "d5": 0.1, "d6": 0.15}:
    errors.append("register: dimension weights differ from the declared model weights")

# 4. Canonical v2 bands and effort multipliers.
BANDS = [
    ("level-1-emergent", 0.0, 20.0, 1.0),
    ("level-2-structured", 20.0, 45.0, 1.5),
    ("level-3-systematic", 45.0, 70.0, 2.5),
    ("level-4-adaptive", 70.0, 88.0, 4.0),
    ("level-5-self-optimising", 88.0, 100.0, 6.0),
]


def resolve_band(score: float) -> str | None:
    if not 0 <= score <= 100:
        return None
    for index, (band_id, lower, upper, _) in enumerate(BANDS):
        if (score <= upper if index == 0 else lower < score <= upper):
            return band_id
    return None


def marginal_points(score: float) -> list[float]:
    boundaries = (20.0, 45.0, 70.0, 88.0, 100.0)
    lower = 0.0
    points = []
    for upper in boundaries:
        points.append(max(0.0, min(score, upper) - lower))
        lower = upper
    return points


def effort_adjusted_value(score: float) -> float:
    return sum(points / band[3] for points, band in zip(marginal_points(score), BANDS))


# 5. Auditable partial worked example.
scope = example.get("assessment_scope") or {}
if scope.get("type") != "partial-scoring-demonstration":
    errors.append("example: assessment_scope.type must identify a partial scoring demonstration")
if scope.get("complete_assessment") is not False or scope.get("gates_evaluated") is not False:
    errors.append("example: must explicitly state that this is not a complete gated assessment")

dimensions = example.get("dimension_scores") or []
expected_weights = {"d1": 0.20, "d2": 0.20, "d3": 0.20, "d4": 0.15, "d5": 0.10, "d6": 0.15}
if {item.get("dimension") for item in dimensions} != set(expected_weights):
    errors.append("example: dimension_scores must include exactly d1 through d6")
weighted_total = 0.0
for item in dimensions:
    dimension = item.get("dimension")
    score = item.get("score")
    weight = item.get("weight")
    contribution = item.get("weighted_contribution")
    if not isinstance(score, (int, float)) or not 0 <= score <= 100:
        errors.append(f"example: invalid score for {dimension}")
        continue
    if not math.isclose(float(weight), expected_weights.get(dimension, -1), abs_tol=1e-9):
        errors.append(f"example: incorrect weight for {dimension}")
    expected_contribution = float(score) * expected_weights[dimension]
    if not isinstance(contribution, (int, float)) or not math.isclose(float(contribution), expected_contribution, abs_tol=1e-8):
        errors.append(f"example: incorrect weighted contribution for {dimension}")
    weighted_total += expected_contribution

declared_score = example.get("aggregated_score_unrounded")
if not isinstance(declared_score, (int, float)):
    errors.append("example: aggregated_score_unrounded must be numeric")
else:
    if not math.isclose(weighted_total, float(declared_score), abs_tol=1e-8):
        errors.append(f"example: dimension aggregation {weighted_total} != declared {declared_score}")
    expected_band = resolve_band(float(declared_score))
    if example.get("resolved_band") != expected_band:
        errors.append(f"example: resolved_band {example.get('resolved_band')!r} != canonical result {expected_band!r}")
    if not math.isclose(float(example.get("aggregated_score_display", -1)), round(float(declared_score), 2), abs_tol=1e-8):
        errors.append("example: displayed aggregate must be rounded to two decimal places")
    eav = example.get("effort_adjusted_value") or {}
    expected_eav = effort_adjusted_value(float(declared_score))
    if not math.isclose(float(eav.get("unrounded", -1)), expected_eav, abs_tol=1e-8):
        errors.append(f"example: EAV {eav.get('unrounded')} != marginal-band calculation {expected_eav}")
    if not math.isclose(float(eav.get("displayed", -1)), round(expected_eav, 2), abs_tol=1e-8):
        errors.append("example: displayed EAV must be rounded to two decimal places")
    contributions = eav.get("contributions") or []
    points = marginal_points(float(declared_score))
    if len(contributions) != len(BANDS):
        errors.append("example: EAV must show one contribution for each of the five bands")
    else:
        for item, band, expected_points in zip(contributions, BANDS, points):
            band_id, _, _, multiplier = band
            if item.get("band") != band_id:
                errors.append(f"example: EAV contribution order/id mismatch for {band_id}")
            if not math.isclose(float(item.get("marginal_points", -1)), expected_points, abs_tol=1e-8):
                errors.append(f"example: incorrect marginal points for {band_id}")
            if not math.isclose(float(item.get("multiplier", -1)), multiplier, abs_tol=1e-8):
                errors.append(f"example: incorrect multiplier for {band_id}")
            expected_part = expected_points / multiplier
            if not math.isclose(float(item.get("adjusted_contribution", -1)), expected_part, abs_tol=1e-8):
                errors.append(f"example: incorrect adjusted contribution for {band_id}")

# 6. Formula boundary and maximum checks, independent of the worked example.
if not math.isclose(effort_adjusted_value(100.0), 53.166666666666664, abs_tol=1e-9):
    errors.append("scoring: EAV theoretical maximum is incorrect")
for boundary, expected in ((20.0, "level-1-emergent"), (20.0001, "level-2-structured"),
                           (45.0, "level-2-structured"), (45.0001, "level-3-systematic"),
                           (70.0, "level-3-systematic"), (70.0001, "level-4-adaptive"),
                           (88.0, "level-4-adaptive"), (88.0001, "level-5-self-optimising")):
    if resolve_band(boundary) != expected:
        errors.append(f"scoring: canonical boundary resolution failed at {boundary}")

if errors:
    print(f"FAIL — {len(errors)} error(s):")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)
print(f"OK — manifest + canonical scale ({len(actual_levels)} entries) + register + v2 scoring + marginal EAV + auditable example")
