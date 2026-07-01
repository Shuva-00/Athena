"""
Athena Experience Pipeline Test

Verifies the complete experience pipeline:

Candidate
    ↓
ExperienceExtractor
    ↓
ExperienceEvidence
    ↓
ExperienceScorer
    ↓
FeatureScorer
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.core.candidate.experiences import Experience
from src.core.candidate.skills import Skill
from src.core.job.job_description import JobDescription
from src.core.candidate.profile import CandidateProfile
from src.preprocessing.extractors.experience_extractor import (
    ExperienceExtractor,
)

from src.ranking.scorers.experience_scorer import (
    ExperienceScorer,
)

from src.ranking.feature_scorer import FeatureScorer


###############################################################################
# Build Candidate
###############################################################################

candidate = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(),
)

candidate.skills = [
    Skill(name="Python"),
    Skill(name="SQL"),
    Skill(name="Machine Learning"),
]

candidate.experiences = [

    Experience(
        company="ABC Technologies",
        job_title="Software Engineer",
        duration_months=24,
        is_current=False,
        skills=[
            "Python",
            "SQL",
        ],
    ),

    Experience(
        company="XYZ AI",
        job_title="Machine Learning Engineer",
        duration_months=18,
        is_current=True,
        skills=[
            "Python",
            "Machine Learning",
        ],
    ),
]

###############################################################################
# Build Job
###############################################################################

job = JobDescription()

job.required_skills = [
    "Python",
    "Machine Learning",
]

###############################################################################
# Execute Pipeline
###############################################################################

print("=" * 70)
print("ATHENA EXPERIENCE PIPELINE TEST")
print("=" * 70)

extractor = ExperienceExtractor()

evidence = extractor.extract(
    candidate,
    job,
)

print("[PASS] Experience extraction completed")

###############################################################################
# Verify Evidence
###############################################################################

assert evidence.total_roles == 2

assert evidence.total_experience_months == 42

assert evidence.current_role_months == 18

print("[PASS] Experience statistics verified")

###############################################################################
# Relevant Experience
###############################################################################

assert evidence.relevant_role_count == 2

assert evidence.relevant_experience_months == 42

print("[PASS] Relevant experience verified")

###############################################################################
# Tenure
###############################################################################

assert evidence.average_tenure_months == 21

assert evidence.longest_tenure_months == 24

assert evidence.shortest_tenure_months == 18

print("[PASS] Tenure statistics verified")

###############################################################################
# Experience Scorer
###############################################################################

score = ExperienceScorer().score(
    evidence,
)

assert 0.0 <= score <= 1.0

print(f"[PASS] Experience score = {score:.4f}")

###############################################################################
# Feature Scorer
###############################################################################

FeatureScorer().score(
    candidate,
)

assert (
    0.0
    <= candidate.features.experience_score
    <= 1.0
)

print("[PASS] Feature scorer verified")

###############################################################################
# Finished
###############################################################################

print("=" * 70)
print("ALL EXPERIENCE PIPELINE TESTS PASSED")
print("=" * 70)