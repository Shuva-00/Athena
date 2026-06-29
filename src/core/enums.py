"""
Project : Athena
Module  : Core Enumerations

Purpose
-------
Defines all enumerations used throughout Athena.

Notes
-----
- Enumerations provide type safety.
- Prevent string literals from being scattered
  throughout the project.
"""

from __future__ import annotations
from enum import Enum


###############################################################################
# PIPELINE
###############################################################################


class PipelineState(str, Enum):
    INITIALIZED = "INITIALIZED"
    DATA_READY = "DATA_READY"
    PREPROCESSING_READY = "PREPROCESSING_READY"
    INTENT_READY = "INTENT_READY"
    RETRIEVAL_READY = "RETRIEVAL_READY"
    RERANK_READY = "RERANK_READY"
    EVIDENCE_READY = "EVIDENCE_READY"
    SCORING_READY = "SCORING_READY"
    EVALUATION_READY = "EVALUATION_READY"
    VALIDATION_READY = "VALIDATION_READY"
    SUBMISSION_READY = "SUBMISSION_READY"


###############################################################################
# REQUIREMENTS
###############################################################################
class WorkMode(str, Enum):
    ONSITE = "onsite"
    HYBRID = "hybrid"
    REMOTE = "remote"
    FLEXIBLE = "flexible"
    
class EvidenceSource(str, Enum):
    RESUME = "RESUME"
    EXPERIENCE = "EXPERIENCE"
    PROJECT = "PROJECT"
    EDUCATION = "EDUCATION"
    CERTIFICATION = "CERTIFICATION"
    GITHUB = "GITHUB"
    PORTFOLIO = "PORTFOLIO"
    INFERENCE = "INFERENCE"

class RequirementType(str, Enum):
    MANDATORY = "MANDATORY"
    PREFERRED = "PREFERRED"
    OPTIONAL = "OPTIONAL"
    NEGATIVE = "NEGATIVE"


###############################################################################
# EVIDENCE
###############################################################################

class EmploymentType(str, Enum):
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    INTERNSHIP = "INTERNSHIP"
    CONTRACT = "CONTRACT"
    FREELANCE = "FREELANCE"
    TEMPORARY = "TEMPORARY"
    APPRENTICESHIP = "APPRENTICESHIP"
    SELF_EMPLOYED = "SELF_EMPLOYED"
    OTHER = "OTHER"

class DegreeLevel(str, Enum):
    HIGH_SCHOOL = "HIGH_SCHOOL"
    DIPLOMA = "DIPLOMA"
    BACHELOR = "BACHELOR"
    MASTER = "MASTER"
    DOCTORATE = "DOCTORATE"
    CERTIFICATE = "CERTIFICATE"
    OTHER = "OTHER"

class InstitutionTier(str, Enum):
    """
    Relative reputation tier of an educational institution.

    Used only as one signal among many during education scoring.
    """

    TIER_1 = "TIER_1"
    TIER_2 = "TIER_2"
    TIER_3 = "TIER_3"
    UNKNOWN = "UNKNOWN"
###############################################################################
# SCORE
###############################################################################


class ScoreType(str, Enum):
    RETRIEVAL = "RETRIEVAL"
    SEMANTIC = "SEMANTIC"
    EXPERIENCE = "EXPERIENCE"
    SKILL = "SKILL"
    BEHAVIOUR = "BEHAVIOUR"
    CONFIDENCE = "CONFIDENCE"
    FINAL = "FINAL"


###############################################################################
# CANDIDATE
###############################################################################


class CandidateStatus(str, Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    DUPLICATE = "DUPLICATE"
    FILTERED = "FILTERED"


###############################################################################
# LOGGING
###############################################################################


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


###############################################################################
# END OF FILE
###############################################################################