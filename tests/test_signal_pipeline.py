"""
ATHENA SIGNAL PIPELINE TEST
"""

from __future__ import annotations

from datetime import date

from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile
from src.core.candidate.signals import (
    CandidateSignals,
    SalaryRange,
)

from src.core.enums import WorkMode

from src.core.job.job_description import JobDescription

from src.preprocessing.extractors.signal_extractor import (
    SignalExtractor,
)

from src.ranking.scorers.signal_scorer import (
    SignalScorer,
)

from src.ranking.feature_scorer import (
    FeatureScorer,
)

print("=" * 70)
print("ATHENA SIGNAL PIPELINE TEST")
print("=" * 70)

###############################################################################
# Candidate
###############################################################################

candidate = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(),
)

candidate.signals = CandidateSignals(

    profile_completeness_score=95,

    signup_date=date(2024, 1, 1),

    last_active_date=date.today(),

    open_to_work_flag=True,

    profile_views_received_30d=80,

    applications_submitted_30d=20,

    recruiter_response_rate=0.90,

    avg_response_time_hours=8,

    skill_assessment_scores={
        "Python": 90,
        "Machine Learning": 85,
    },

    connection_count=150,

    endorsements_received=20,

    notice_period_days=30,

    expected_salary_range_inr_lpa=SalaryRange(
        minimum=10,
        maximum=15,
    ),

    preferred_work_mode=WorkMode.HYBRID,

    willing_to_relocate=True,

    github_activity_score=85,

    search_appearance_30d=70,

    saved_by_recruiters_30d=12,

    interview_completion_rate=0.90,

    offer_acceptance_rate=0.80,

    verified_email=True,

    verified_phone=True,

    linkedin_connected=True,
)

###############################################################################
# Job
###############################################################################

job = JobDescription(
    title="Machine Learning Engineer",
)

###############################################################################
# Extraction
###############################################################################

evidence = SignalExtractor().extract(
    candidate,
    job,
)

print("[PASS] Signal extraction completed")

###############################################################################
# Evidence
###############################################################################

assert evidence.responsiveness_score > 0.0

print("[PASS] Responsiveness verified")

assert evidence.engagement_score > 0.0

print("[PASS] Engagement verified")

assert evidence.assessment_score > 0.0

print("[PASS] Assessment verified")

assert evidence.profile_completeness > 0.0

print("[PASS] Profile completeness verified")

assert evidence.github_activity > 0.0

print("[PASS] GitHub activity verified")

###############################################################################
# Scoring
###############################################################################

score = SignalScorer().score(
    evidence,
)

print(f"[PASS] Signal score = {score:.4f}")

###############################################################################
# Feature Scorer
###############################################################################

FeatureScorer().score(
    candidate,
)

assert (
    candidate.features.signal_score > 0.0
)

print("[PASS] Feature scorer verified")

print("=" * 70)
print("ALL SIGNAL PIPELINE TESTS PASSED")
print("=" * 70)