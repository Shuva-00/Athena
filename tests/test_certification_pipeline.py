"""
ATHENA CERTIFICATION PIPELINE TEST
"""

from __future__ import annotations

from datetime import date

from src.core.candidate.certifications import Certification
from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile

from src.core.job.job_description import JobDescription

from src.preprocessing.extractors.certification_extractor import (
    CertificationExtractor,
)

from src.ranking.feature_scorer import FeatureScorer
from src.ranking.scorers.certification_scorer import (
    CertificationScorer,
)

print("=" * 70)
print("ATHENA CERTIFICATION PIPELINE TEST")
print("=" * 70)

###############################################################################
# Candidate
###############################################################################

candidate = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(),
)

candidate.certifications.append(

    Certification(

        name="AWS Certified Cloud Practitioner",

        issuer="Amazon",

        issue_date=date(2024, 6, 1),

        verified=True,

        skills=[
            "AWS",
            "Cloud",
        ],
    )
)

###############################################################################
# Job
###############################################################################

job = JobDescription(

    title="Cloud Engineer",

    certifications=[
        "AWS Certified Cloud Practitioner",
    ],
)

###############################################################################
# Extraction
###############################################################################

evidence = CertificationExtractor().extract(
    candidate,
    job,
)

print("[PASS] Certification extraction completed")

###############################################################################
# Evidence
###############################################################################

assert evidence.total_certifications == 1

assert evidence.matched_total == 1

print("[PASS] Matching verified")

assert evidence.recent_certifications == 1

print("[PASS] Recency verified")

assert evidence.verified_count == 1

print("[PASS] Verification verified")

###############################################################################
# Scoring
###############################################################################

score = CertificationScorer().score(
    evidence,
)

print(f"[PASS] Certification score = {score:.4f}")

###############################################################################
# Feature Scorer
###############################################################################

FeatureScorer().score(
    candidate,
)

assert (
    candidate.features.certification_score > 0
)

print("[PASS] Feature scorer verified")

print("=" * 70)
print("ALL CERTIFICATION PIPELINE TESTS PASSED")
print("=" * 70)