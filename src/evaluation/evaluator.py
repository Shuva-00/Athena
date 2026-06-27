"""
Project : Athena
Module  : Evaluator

Purpose
-------
Evaluates predicted rankings against ground truth.

Guidelines
----------
- Uses metrics from evaluation.metrics.
- No printing.
- No plotting.
"""

from __future__ import annotations

from src.core import EvaluationResult
from src.evaluation.metrics import (
    hit_rate,
    mean_average_precision,
    mean_reciprocal_rank,
    ndcg_at_k,
    precision_at_k,
    recall_at_k,
)


class Evaluator:
    """
    Evaluates ranking performance.
    """

    def evaluate(
        self,
        relevant: set[str],
        predicted: list[str],
        k: int,
    ) -> EvaluationResult:
        """
        Evaluate ranking metrics.
        """

        return EvaluationResult(
            precision_at_k=precision_at_k(
                relevant,
                predicted,
                k,
            ),
            recall_at_k=recall_at_k(
                relevant,
                predicted,
                k,
            ),
            hit_rate=hit_rate(
                relevant,
                predicted,
                k,
            ),
            mean_reciprocal_rank=mean_reciprocal_rank(
                relevant,
                predicted,
            ),
            ndcg_at_k=ndcg_at_k(
                relevant,
                predicted,
                k,
            ),
            mean_average_precision=mean_average_precision(
                relevant,
                predicted,
            ),
        )


###############################################################################
# END OF FILE
###############################################################################