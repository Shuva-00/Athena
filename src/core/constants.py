"""
Project : Athena
Module  : Core Constants

Purpose
-------
Defines project-wide immutable constants shared across Athena.

Guidelines
----------
- Store ONLY immutable, project-wide constants.
- Do NOT store configurable values here.
  Those belong in configs/config.yaml.
- Do NOT store enums or state values here.
  Those belong in enums.py.
"""

from __future__ import annotations

###############################################################################
# PROJECT INFORMATION
###############################################################################

PROJECT_NAME: str = "Athena"

PROJECT_VERSION: str = "1.0.0"

ARCHITECTURE_VERSION: str = "1.0"

###############################################################################
# PIPELINE LIMITS
###############################################################################

FINAL_RANK_SIZE: int = 100

INITIAL_RETRIEVAL_SIZE: int = 2000



###############################################################################
# RANDOMNESS
###############################################################################

DEFAULT_RANDOM_SEED: int = 42

###############################################################################
# SCORE LIMITS
###############################################################################

MIN_SCORE: float = 0.0

MAX_SCORE: float = 1.0

###############################################################################
# CONFIDENCE LIMITS
###############################################################################

MIN_CONFIDENCE: float = 0.0

MAX_CONFIDENCE: float = 1.0

###############################################################################
# FILES
###############################################################################

DEFAULT_CONFIG_FILE: str = "configs/config.yaml"

###############################################################################
# LOGGING
###############################################################################

LOGGER_NAME: str = "athena"

###############################################################################
# NUMERICAL TOLERANCE
###############################################################################
REQUIRED_CANDIDATE_FIELDS = (
    "candidate_id",
    "profile",
    "education",
    "career_history",
    "skills",
    "certifications",
    "languages",
    "redrob_signals",
)

EPSILON: float = 1e-9

###############################################################################
# END OF FILE
###############################################################################