"""
ATHENA REPORT TEST
"""

from __future__ import annotations

from src.core import EvaluationResult
from src.core import BenchmarkResult

from src.evaluation import Report

print("=" * 70)
print("ATHENA REPORT TEST")
print("=" * 70)

evaluation = EvaluationResult(

    precision_at_k=0.80,
    recall_at_k=0.75,
    hit_rate=1.00,
    mean_reciprocal_rank=0.90,
    mean_average_precision=0.82,
    ndcg_at_k=0.88,
)

benchmark = BenchmarkResult(

    preprocessing_time=0.25,
    retrieval_time=0.11,
    ranking_time=0.05,
    reasoning_time=0.03,
    total_time=0.44,
)

report = Report().generate(
    evaluation,
    benchmark,
)

assert "Precision@K" in report
assert "Recall@K" in report
assert "Total Time" in report
assert "ATHENA EVALUATION REPORT" in report

print(report)

print("[PASS] Report generated successfully")

print("=" * 70)
print("ALL REPORT TESTS PASSED")
print("=" * 70)