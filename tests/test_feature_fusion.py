"""
ATHENA FEATURE FUSION TEST
"""

from __future__ import annotations

from src.core.candidate.features import CandidateFeatures
from src.ranking.feature_fusion import FeatureFusion

print("=" * 70)
print("ATHENA FEATURE FUSION TEST")
print("=" * 70)

###############################################################################
# Features
###############################################################################

features = CandidateFeatures(

    skill_score=0.90,

    experience_score=0.80,

    education_score=0.70,

    certification_score=0.60,

    signal_score=0.50,

    integrity_score=1.00,

)

###############################################################################
# Fusion
###############################################################################

fusion = FeatureFusion()

score = fusion.score(
    features,
)

print(f"[PASS] Feature score = {score:.4f}")

###############################################################################
# Validation
###############################################################################

assert 0.0 <= score <= 1.0

print("[PASS] Score range verified")

###############################################################################
# Sensitivity Test
###############################################################################

original = score

features.skill_score = 0.20

updated = fusion.score(
    features,
)

assert original != updated

print("[PASS] Feature influence verified")

print("=" * 70)
print("ALL FEATURE FUSION TESTS PASSED")
print("=" * 70)