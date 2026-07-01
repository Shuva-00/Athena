"""
ATHENA FINAL SCORE FUSION TEST
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile
from src.ranking.final_score_fusion import FinalScoreFusion

print("=" * 70)
print("ATHENA FINAL SCORE FUSION TEST")
print("=" * 70)

###############################################################################
# Candidate 1
###############################################################################

candidate1 = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(),
)

candidate1.scores.semantic_score = 0.90
candidate1.features.feature_score = 0.80

###############################################################################
# Candidate 2
###############################################################################

candidate2 = Candidate(
    candidate_id="candidate_002",
    profile=CandidateProfile(),
)

candidate2.scores.semantic_score = 0.60
candidate2.features.feature_score = 0.90

###############################################################################
# Fusion
###############################################################################

fusion = FinalScoreFusion()

fusion.score(candidate1)
fusion.score(candidate2)

###############################################################################
# Expected Values
###############################################################################

expected1 = (0.90 * 0.75) + (0.80 * 0.25)
expected2 = (0.60 * 0.75) + (0.90 * 0.25)

###############################################################################
# Validation
###############################################################################

assert abs(candidate1.scores.final_score - expected1) < 1e-6
assert abs(candidate2.scores.final_score - expected2) < 1e-6

print(f"[PASS] Candidate 1 = {candidate1.scores.final_score:.4f}")
print(f"[PASS] Candidate 2 = {candidate2.scores.final_score:.4f}")

assert candidate1.scores.final_score > candidate2.scores.final_score

print("[PASS] Score ordering verified")

print("=" * 70)
print("ALL FINAL SCORE FUSION TESTS PASSED")
print("=" * 70)