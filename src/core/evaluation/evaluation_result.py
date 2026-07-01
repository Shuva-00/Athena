"""
Project : Athena
Module  : Evaluation Result

Purpose
-------
Represents the results of evaluating a ranking pipeline.

Guidelines
----------
- Pure domain model.
- No business logic.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class EvaluationResult(AthenaModel):
    """
    Stores evaluation metrics.
    """

    precision_at_k: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    recall_at_k: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    hit_rate: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    mean_reciprocal_rank: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    ndcg_at_k: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )
    mean_average_precision: float = Field(
    default=0.0,
    ge=0.0,
    le=1.0,
    description="Mean Average Precision (MAP).",
)