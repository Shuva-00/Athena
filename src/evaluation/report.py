"""
Project : Athena
Module  : Evaluation Report

Purpose
-------
Generates a human-readable evaluation report.

Guidelines
----------
- No printing.
- No logging.
- No file writing.
- Formats results only.
"""

from __future__ import annotations

from src.core import BenchmarkResult
from src.core import EvaluationResult


class Report:
    """
    Generates evaluation reports.
    """

    def generate(
        self,
        evaluation: EvaluationResult,
        benchmark: BenchmarkResult,
    ) -> str:
        """
        Generate a formatted evaluation report.
        """

        report = [
            "=" * 70,
            "ATHENA EVALUATION REPORT",
            "=" * 70,
            "",
            "Ranking Metrics",
            "-" * 70,
            f"Precision@K           : {evaluation.precision_at_k:.4f}",
            f"Recall@K              : {evaluation.recall_at_k:.4f}",
            f"Hit Rate              : {evaluation.hit_rate:.4f}",
            f"Mean Reciprocal Rank  : {evaluation.mean_reciprocal_rank:.4f}",
            f"Mean Average Precision: {evaluation.mean_average_precision:.4f}",
            f"NDCG@K                : {evaluation.ndcg_at_k:.4f}",
            "",
            "Performance",
            "-" * 70,
            f"Preprocessing Time (s): {benchmark.preprocessing_time:.4f}",
            f"Retrieval Time (s)    : {benchmark.retrieval_time:.4f}",
            f"Ranking Time (s)      : {benchmark.ranking_time:.4f}",
            f"Reasoning Time (s)    : {benchmark.reasoning_time:.4f}",
            f"Total Time (s)        : {benchmark.total_time:.4f}",
            "",
            "=" * 70,
        ]

        return "\n".join(report)


###############################################################################
# END OF FILE
###############################################################################