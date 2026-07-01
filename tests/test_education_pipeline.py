"""
ATHENA EDUCATION PIPELINE TEST
"""

from __future__ import annotations

from src.core.candidate.education import Education
from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile

from src.core.enums import DegreeLevel
from src.core.enums import InstitutionTier

from src.core.job.job_description import JobDescription

from src.preprocessing.extractors.education_extractor import (
    EducationExtractor,
)

from src.ranking.scorers.education_scorer import (
    EducationScorer,
)

from src.ranking.feature_scorer import (
    FeatureScorer,
)

print("=" * 70)
print("ATHENA EDUCATION PIPELINE TEST")
print("=" * 70)

###############################################################################
# Candidate
###############################################################################

candidate = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(),
)

candidate.education.append(

    Education(

        institution="IIIT Sri City",

        degree="B.Tech",

        degree_level=DegreeLevel.BACHELOR,

        field_of_study="Electronics and Communication Engineering",

        start_year=2024,

        end_year=2028,

        grade="8.55",

        cgpa=8.55,

        tier=InstitutionTier.TIER_2,

        relevant_courses=[
            "Python",
            "Machine Learning",
        ],

        research_projects=[
            "Athena ATS",
        ],

        publications=[],
    )
)

###############################################################################
# Job
###############################################################################

job = JobDescription(

    title="Machine Learning Engineer",

    required_skills=[
        "Python",
        "Machine Learning",
    ],

    minimum_degree=["BACHELOR",
    ],
)

###############################################################################
# Extraction
###############################################################################

evidence = EducationExtractor().extract(
    candidate,
    job,
)

print("[PASS] Education extraction completed")

###############################################################################
# Evidence
###############################################################################

assert evidence.total_degrees == 1

assert evidence.minimum_degree_met

assert evidence.highest_degree == DegreeLevel.BACHELOR

print("[PASS] Degree evidence verified")

assert evidence.highest_cgpa == 8.55

assert evidence.average_cgpa == 8.55

print("[PASS] Academic evidence verified")

assert evidence.institution_tier == InstitutionTier.TIER_2

print("[PASS] Institution evidence verified")

assert evidence.research_project_count == 1

assert evidence.research_publication_count == 0

print("[PASS] Research evidence verified")

###############################################################################
# Scoring
###############################################################################

score = EducationScorer().score(
    evidence,
)

print(f"[PASS] Education score = {score:.4f}")

###############################################################################
# Feature Scorer
###############################################################################

FeatureScorer().score(
    candidate,
)

assert (
    candidate.features.education_score > 0.0
)

print("[PASS] Feature scorer verified")

print("=" * 70)
print("ALL EDUCATION PIPELINE TESTS PASSED")
print("=" * 70)