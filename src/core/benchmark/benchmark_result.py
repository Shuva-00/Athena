"""
Project : Athena
Module  : Benchmark Result

Purpose
-------
Stores runtime performance statistics of the Athena pipeline.

Guidelines
----------
- Pure domain model.
- No timing logic.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class BenchmarkResult(AthenaModel):
    """
    Stores pipeline benchmark statistics.
    """
    preprocessing_time: float = Field(
    default=0.0,
    ge=0.0,
    description="Preprocessing execution time.",
    )
    
    retrieval_time: float = Field(
        default=0.0,
        ge=0.0,
        description="Time spent during retrieval (seconds).",
    )

    ranking_time: float = Field(
        default=0.0,
        ge=0.0,
        description="Time spent during ranking (seconds).",
    )

    reasoning_time: float = Field(
        default=0.0,
        ge=0.0,
        description="Time spent during reasoning (seconds).",
    )

    total_time: float = Field(
        default=0.0,
        ge=0.0,
        description="Total pipeline execution time (seconds).",
    )