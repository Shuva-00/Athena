"""
Project : Athena
Module  : Core Exceptions

Purpose
-------
Defines all project-specific exception classes used throughout Athena.

Guidelines
----------
- Never raise generic Exception.
- Always raise a specific Athena exception.
- Keep exceptions lightweight.
"""

from __future__ import annotations


class AthenaError(Exception):
    """
    Base exception for all Athena-specific errors.
    """

    pass


###############################################################################
# Configuration Errors
###############################################################################


class ConfigurationError(AthenaError):
    """Raised when configuration files are missing or invalid."""

    pass


###############################################################################
# Data Errors
###############################################################################


class DataError(AthenaError):
    """Base class for dataset-related errors."""

    pass


class DataValidationError(DataError):
    """Raised when dataset validation fails."""

    pass


class MissingFieldError(DataError):
    """Raised when a required dataset field is missing."""

    pass


class InvalidCandidateError(DataError):
    """Raised when a candidate profile is malformed."""

    pass


###############################################################################
# Retrieval Errors
###############################################################################


class RetrievalError(AthenaError):
    """Raised when candidate retrieval fails."""

    pass


class EmbeddingError(RetrievalError):
    """Raised when embedding generation fails."""

    pass


class IndexErrorAthena(RetrievalError):
    """Raised when FAISS index operations fail."""

    pass


###############################################################################
# Ranking Errors
###############################################################################


class RankingError(AthenaError):
    """Raised when ranking cannot be completed."""

    pass


###############################################################################
# Evidence Errors
###############################################################################


class EvidenceError(AthenaError):
    """Raised when evidence extraction fails."""

    pass


###############################################################################
# Validation Errors
###############################################################################


class SubmissionValidationError(AthenaError):
    """Raised when the final submission is invalid."""

    pass


###############################################################################
# Runtime Errors
###############################################################################


class PipelineStateError(AthenaError):
    """
    Raised when pipeline execution violates state transitions.
    """

    pass


###############################################################################
# End of File
###############################################################################