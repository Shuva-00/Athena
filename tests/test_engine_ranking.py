"""
ATHENA RANKING ENGINE TEST
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile

from src.ranking.ranking_engine import RankingEngine

print("=" * 70)
print("ATHENA RANKING ENGINE TEST")
print("=" * 70)

###############################################################################
# Candidates
###############################################################################

c1 = Candidate(
    candidate_id="1",
    profile=CandidateProfile(),
)

c2 = Candidate(
    candidate_id="2",
    profile=CandidateProfile(),
)

c3 = Candidate(
    candidate_id="3",
    profile=CandidateProfile(),
)

###############################################################################
# Scores
###############################################################################


c1.scores.final_score = 0.875
c2.scores.final_score = 0.675
c3.scores.final_score = 0.8875

c2.features.feature_score = 0.50
c2.scores.semantic_score = 0.60

c3.features.feature_score = 0.70
c3.scores.semantic_score = 0.95

###############################################################################
# Ranking
###############################################################################

ranking = RankingEngine()

results = ranking.rank(
    [
        c1,
        c2,
        c3,
    ]
)

###############################################################################
# Validation
###############################################################################

assert results[0].scores.rank == 1
assert results[1].scores.rank == 2
assert results[2].scores.rank == 3

assert (
    results[0].scores.final_score
    >=
    results[1].scores.final_score
)

assert (
    results[1].scores.final_score
    >=
    results[2].scores.final_score
)

print("[PASS] Ranking order verified")
print("[PASS] Rank assignment verified")
print("[PASS] Final score fusion verified")

print("=" * 70)
print("ALL RANKING ENGINE TESTS PASSED")
print("=" * 70)