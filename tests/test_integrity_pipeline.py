"""
ATHENA INTEGRITY PIPELINE TEST
"""

from __future__ import annotations

from datetime import date

from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile
from src.core.candidate.skills import Skill
from src.core.candidate.certifications import Certification
from src.core.candidate.experiences import Experience

from src.core.enums import EmploymentType

from src.core.job.job_description import JobDescription

from src.preprocessing.extractors.integrity_extractor import (
    IntegrityExtractor,
)

from src.ranking.scorers.integrity_scorer import (
    IntegrityScorer,
)

from src.ranking.feature_scorer import (
    FeatureScorer,
)

print("=" * 70)
print("ATHENA INTEGRITY PIPELINE TEST")
print("=" * 70)

###############################################################################
# Candidate
###############################################################################

candidate = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(
        full_name="John Doe",
        email="john@example.com",
    ),
)

###############################################################################
# Skills (Duplicate)
###############################################################################

candidate.skills.extend(
    [
        Skill(name="Python"),
        Skill(name="python"),
    ]
)

###############################################################################
# Certifications (Duplicate)
###############################################################################

candidate.certifications.extend(
    [
        Certification(
            name="AWS CCP",
        ),
        Certification(
            name="aws ccp",
        ),
    ]
)

###############################################################################
# Experience (Timeline Issue)
###############################################################################

candidate.experiences.append(

    Experience(

        company="ABC",

        job_title="Software Engineer",

        employment_type=EmploymentType.FULL_TIME,

        start_date=date(2024, 6, 1),

        end_date=date(2023, 6, 1),

        is_current=False,

        duration_months=12,

    )

)

###############################################################################
# Job
###############################################################################

job = JobDescription(
    title="Software Engineer",
)

###############################################################################
# Extraction
###############################################################################

evidence = IntegrityExtractor().extract(
    candidate,
    job,
)

print("[PASS] Integrity extraction completed")

###############################################################################
# Evidence
###############################################################################

assert evidence.duplicate_skills == 1

print("[PASS] Duplicate skills verified")

assert evidence.duplicate_certifications == 1

print("[PASS] Duplicate certifications verified")

assert evidence.timeline_inconsistencies == 1

print("[PASS] Timeline consistency verified")

assert evidence.missing_required_fields == 0

print("[PASS] Missing field verification completed")

assert evidence.confidence > 0.0

print("[PASS] Confidence verified")

###############################################################################
# Scoring
###############################################################################

score = IntegrityScorer().score(
    evidence,
)

print(f"[PASS] Integrity score = {score:.4f}")

###############################################################################
# Feature Scorer
###############################################################################

FeatureScorer().score(
    candidate,
)

assert (
    candidate.features.integrity_score > 0.0
)

print("[PASS] Feature scorer verified")

print("=" * 70)
print("ALL INTEGRITY PIPELINE TESTS PASSED")
print("=" * 70)