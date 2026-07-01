"""
ATHENA SUBMISSION GENERATOR TEST
"""

from __future__ import annotations

from pathlib import Path

from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile
from src.submission.submission_generator import SubmissionGenerator

print("=" * 70)
print("ATHENA SUBMISSION GENERATOR TEST")
print("=" * 70)

###############################################################################
# Candidate
###############################################################################

candidate = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(),
)

candidate.scores.rank = 1
candidate.scores.final_score = 0.913

candidate.reason = (
    "Excellent skill match."
)

###############################################################################
# Generate
###############################################################################

output = SubmissionGenerator().generate(
    [candidate],
    Path("outputs/test_submission.csv"),
)

###############################################################################
# Validation
###############################################################################

assert output.exists()

print(output)

print("[PASS] Submission generated successfully")

print("=" * 70)
print("ALL SUBMISSION TESTS PASSED")
print("=" * 70)