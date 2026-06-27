"""
Project : Athena
Module  : Candidate Scores

Purpose
-------
Defines the normalized scores assigned to a candidate throughout
the Athena ranking pipeline.

Guidelines
----------
- Every score is normalized to [0.0, 1.0].
- No business logic belongs here.
- This is a pure domain model.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class CandidateScores(AthenaModel):
    """
    Stores all normalized scores generated during retrieval,
    ranking, and evaluation.
    """

    ###########################################################################
    # Retrieval Scores
    ###########################################################################

    bm25_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Normalized BM25 retrieval score.",
    )

    dense_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Dense retrieval similarity score.",
    )

    retrieval_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Combined retrieval score after Reciprocal Rank Fusion (RRF).",
    )

    ###########################################################################
    # Semantic Ranking Score
    ###########################################################################

    semantic_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Cross-encoder semantic relevance score.",
    )

    ###########################################################################
    # Feature Scores
    ###########################################################################

    skill_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Skill matching score.",
    )

    experience_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Experience relevance score.",
    )

    project_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Project relevance score.",
    )

    education_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Education relevance score.",
    )

    certification_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Certification relevance score.",
    )

    behavior_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Behavioral signal score.",
    )

    consistency_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Career consistency score.",
    )

    feature_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Combined engineered feature score.",
    )

    ###########################################################################
    # Final Scores
    ###########################################################################

    confidence_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Overall confidence in the ranking result.",
    )

    final_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Final ranking score.",
    )

    ###########################################################################
    # Ranking Information
    ###########################################################################

    rank: int | None = Field(
        default=None,
        ge=1,
        description="Final candidate rank.",
    )

    percentile: float | None = Field(
        default=None,
        ge=0.0,
        le=100.0,
        description="Candidate percentile among all candidates.",
    )


###############################################################################
# END OF FILE
###############################################################################