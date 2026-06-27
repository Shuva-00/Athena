"""
Project : Athena
Module  : Settings

Purpose
-------
Central configuration for the Athena project.

Guidelines
----------
- Stores configurable values only.
- No business logic.
- No functions.
"""

from __future__ import annotations


###############################################################################
# EMBEDDING MODELS
###############################################################################

EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
CROSS_ENCODER_MODEL = "BAAI/bge-reranker-large"

FINAL_TOP_K = 100

###############################################################################
# RETRIEVAL
###############################################################################

BM25_TOP_K = 1000

DENSE_TOP_K = 1000

FINAL_RETRIEVAL_TOP_K = 2000
RERANK_INPUT_SIZE = 300
RRF_K = 60

SKILL_MATCH_WEIGHT = 5.0

EXPERIENCE_WEIGHT = 1.0

PROJECT_WEIGHT = 2.0

CERTIFICATION_WEIGHT = 1.5

TECHNOLOGY_WEIGHT = 1.0
###############################################################################
# FAISS
###############################################################################

FAISS_METRIC = "cosine"

NORMALIZE_EMBEDDINGS = True

CROSS_ENCODER_WEIGHT = 0.80

FEATURE_WEIGHT = 0.20
###############################################################################
# TEXT PROCESSING
###############################################################################

MIN_PROJECT_SENTENCE_LENGTH = 20

MAX_PROJECTS_PER_EXPERIENCE = 5

###############################################################################
# REASONING
###############################################################################

MIN_STRONG_SKILL_MATCH = 5

MIN_STRONG_TECH_MATCH = 3

###############################################################################
# RANDOMNESS
###############################################################################

RANDOM_SEED = 42


###############################################################################
# END OF FILE
###############################################################################