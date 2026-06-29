"""
Athena Domain Sanity Test

Purpose
-------
Verifies that the core domain architecture is correctly wired before
moving to feature extraction and scoring.
"""

from src.core.candidate.entity import Candidate
from src.core.candidate.profile import CandidateProfile

from src.core.candidate.evidence import EvidenceCollection
from src.core.candidate.skill_evidence import SkillEvidence
from src.core.candidate.experience_evidence import ExperienceEvidence
from src.core.candidate.education_evidence import EducationEvidence
from src.core.candidate.certification_evidence import CertificationEvidence
from src.core.candidate.signal_evidence import SignalEvidence
from src.core.candidate.integrity_evidence import IntegrityEvidence
from pydantic import ValidationError
from src.core.candidate.features import CandidateFeatures
from src.core.candidate.scores import CandidateScores


print("=" * 70)
print("ATHENA DOMAIN SANITY TEST")
print("=" * 70)

###############################################################################
# Candidate Construction
###############################################################################

candidate = Candidate(
    candidate_id="candidate_001",
    profile=CandidateProfile(),
)

print("\n[PASS] Candidate instantiated")

###############################################################################
# Evidence Collection
###############################################################################

assert isinstance(candidate.evidence, EvidenceCollection)

print("[PASS] EvidenceCollection exists")

###############################################################################
# Evidence Models
###############################################################################

assert isinstance(candidate.evidence.skill, SkillEvidence)
assert isinstance(candidate.evidence.experience, ExperienceEvidence)
assert isinstance(candidate.evidence.education, EducationEvidence)
assert isinstance(candidate.evidence.certification, CertificationEvidence)
assert isinstance(candidate.evidence.signal, SignalEvidence)
assert isinstance(candidate.evidence.integrity, IntegrityEvidence)

print("[PASS] All evidence models initialized")

###############################################################################
# Feature Model
###############################################################################

assert isinstance(candidate.features, CandidateFeatures)

print("[PASS] CandidateFeatures initialized")

###############################################################################
# Score Model
###############################################################################

assert isinstance(candidate.scores, CandidateScores)

print("[PASS] CandidateScores initialized")

###############################################################################
# Default Mutable Objects
###############################################################################

candidate.evidence.skill.matched_skills.append("Python")

candidate2 = Candidate(
    candidate_id="candidate_002",
    profile=CandidateProfile(),
)

assert candidate2.evidence.skill.matched_skills == []

print("[PASS] Default factories are independent")

###############################################################################
# Nested Assignment
###############################################################################

candidate.evidence.skill.exact_matches = 7

assert candidate.evidence.skill.exact_matches == 7

print("[PASS] Nested models are mutable")

###############################################################################
# Feature Assignment
###############################################################################

candidate.features.skill_score = 0.82

assert candidate.features.skill_score == 0.82

print("[PASS] Feature model assignment works")

###############################################################################
# Score Assignment
###############################################################################

candidate.scores.final_score = 0.915
try:
    candidate.scores.final_score = 1.5
    raise AssertionError("Validation failed.")
except Exception:
    print("[PASS] Score validation works")
    
assert candidate.scores.final_score == 0.915

print("[PASS] Score model assignment works")

###############################################################################
# Serialization
###############################################################################

data = candidate.model_dump()

assert isinstance(data, dict)

print("[PASS] model_dump() successful")

###############################################################################
# JSON Serialization
###############################################################################

json_data = candidate.model_dump_json()

assert isinstance(json_data, str)

print("[PASS] JSON serialization successful")

###############################################################################
# Deep Copy
###############################################################################

copy_candidate = candidate.model_copy(deep=True)

copy_candidate.evidence.skill.exact_matches = 999

assert candidate.evidence.skill.exact_matches == 7

print("[PASS] Deep copy isolation verified")

###############################################################################
# Summary
###############################################################################

print("\n" + "=" * 70)
print("ALL DOMAIN TESTS PASSED")
print("=" * 70)


try:
    Candidate(candidate_id="1")
    raise AssertionError("Profile should be required.")
except ValidationError:
    print("[PASS] Required field validation works")