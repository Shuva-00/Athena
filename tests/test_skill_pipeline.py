"""
Athena Skill Pipeline Integration Test

Verifies the complete pipeline:

Candidate
    ↓
SkillExtractor
    ↓
SkillEvidence
    ↓
SkillScorer
    ↓
FeatureScorer
"""

from datetime import date

from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile
from src.core.candidate.skills import Skill
from src.core.candidate.experiences import Experience
from src.core.job.job_description import JobDescription
from src.core.enums import EmploymentType

from src.preprocessing.extractors.skill_extractor import SkillExtractor
from src.ranking.scorers.skill_scorer import SkillScorer
from src.ranking.feature_scorer import FeatureScorer


print("=" * 70)
print("ATHENA SKILL PIPELINE TEST")
print("=" * 70)


###############################################################################
# Candidate
###############################################################################

candidate = Candidate(

    candidate_id="C001",

    profile=CandidateProfile(
        full_name="John Doe",
    ),

    skills=[
        Skill(name="Python"),
        Skill(name="SQL"),
        Skill(name="Docker"),
    ],

    experiences=[

        Experience(

            company="ABC",

            job_title="Software Engineer",

            employment_type=EmploymentType.FULL_TIME,

            start_date=date(2022, 1, 1),

            end_date=date(2024, 1, 1),

            duration_months=24,

            skills=[
                "Python",
                "SQL",
            ],
        )
    ],
)

###############################################################################
# Job
###############################################################################

job = JobDescription(

    title="Backend Engineer",

    required_skills=[
        "Python",
        "SQL",
        "AWS",
    ],
)

###############################################################################
# Skill Extraction
###############################################################################

extractor = SkillExtractor()

evidence = extractor.extract(
    candidate,
    job,
)

print("[PASS] Skill extraction completed")

###############################################################################
# Verify Evidence
###############################################################################

assert evidence.candidate_total == 3
assert evidence.required_total == 3

assert evidence.exact_matches == 2

assert sorted(evidence.matched_skills) == [
    "python",
    "sql",
]

assert evidence.missing_required == [
    "aws",
]

assert evidence.additional_skills == [
    "docker",
]

print("[PASS] Skill evidence verified")

###############################################################################
# Duration
###############################################################################

assert evidence.total_duration_months == 48

assert evidence.average_duration_months == 24

assert evidence.maximum_duration_months == 24

print("[PASS] Duration extraction verified")

###############################################################################
# Confidence
###############################################################################

assert evidence.confidence == 1.0

print("[PASS] Confidence extraction verified")

###############################################################################
# Skill Scorer
###############################################################################

score = SkillScorer().score(
    evidence,
)

assert 0.0 <= score <= 1.0

print(f"[PASS] Skill score = {score:.4f}")

###############################################################################
# Feature Scorer
###############################################################################

FeatureScorer().score(candidate)

assert candidate.features.skill_score == score

print("[PASS] Feature scorer verified")

###############################################################################
# Final
###############################################################################

print("=" * 70)
print("ALL SKILL PIPELINE TESTS PASSED")
print("=" * 70)