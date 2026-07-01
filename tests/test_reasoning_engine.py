"""
ATHENA REASONING ENGINE TEST
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile

from src.core.candidate.skill_evidence import SkillEvidence
from src.core.candidate.experience_evidence import ExperienceEvidence
from src.core.candidate.education_evidence import EducationEvidence
from src.core.candidate.certification_evidence import CertificationEvidence
from src.core.candidate.signal_evidence import SignalEvidence
from src.core.candidate.integrity_evidence import IntegrityEvidence

from src.reasoning.reasoning_engine import ReasoningEngine

print("=" * 70)
print("ATHENA REASONING ENGINE TEST")
print("=" * 70)

###############################################################################
# Candidate
###############################################################################

candidate = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(),
)

###############################################################################
# Skill Evidence
###############################################################################

candidate.evidence.skill = SkillEvidence(
    exact_matches=8,
    missing_required=["Kubernetes"],
)

###############################################################################
# Experience Evidence
###############################################################################

candidate.evidence.experience = ExperienceEvidence(
    relevant_experience_months=72,
    employment_gap_months=0,
)

###############################################################################
# Education Evidence
###############################################################################

candidate.evidence.education = EducationEvidence(
    minimum_degree_met=True,
)

###############################################################################
# Certification Evidence
###############################################################################

candidate.evidence.certification = CertificationEvidence(
    matched_total=2,
    missing_certifications=["Azure Administrator"],
)

###############################################################################
# Signal Evidence
###############################################################################

candidate.evidence.signal = SignalEvidence(
    profile_completeness=0.95,
    github_activity=0.82,
)

###############################################################################
# Integrity Evidence
###############################################################################

candidate.evidence.integrity = IntegrityEvidence()

###############################################################################
# Final Score
###############################################################################

candidate.scores.final_score = 0.913

###############################################################################
# Generate Reasoning
###############################################################################

engine = ReasoningEngine()

reason = engine.generate(candidate)

###############################################################################
# Validation
###############################################################################

assert candidate.reason == reason

assert "Matched 8 required skill" in reason

assert "6.0 years relevant experience" in reason

assert "Required education satisfied" in reason

assert "2 relevant certification" in reason

assert "Highly complete professional profile" in reason

assert "Resume integrity verified" in reason

assert "Kubernetes" in reason

assert "Azure Administrator" in reason

assert "Final Score" in reason

print(reason)

print("[PASS] Reason generated successfully")

print("=" * 70)
print("ALL REASONING ENGINE TESTS PASSED")
print("=" * 70)