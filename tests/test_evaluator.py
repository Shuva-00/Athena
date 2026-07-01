"""
ATHENA EVALUATOR TEST
"""

from __future__ import annotations

from src.evaluation import Evaluator

print("=" * 70)
print("ATHENA EVALUATOR TEST")
print("=" * 70)

###############################################################################
# Ground Truth
###############################################################################

relevant = {
    "candidate_1",
    "candidate_3",
    "candidate_5",
}

predicted = [
    "candidate_1",
    "candidate_2",
    "candidate_3",
    "candidate_4",
    "candidate_5",
]

###############################################################################
# Evaluation
###############################################################################

result = Evaluator().evaluate(
    relevant=relevant,
    predicted=predicted,
    k=5,
)

###############################################################################
# Validation
###############################################################################

assert 0.0 <= result.precision_at_k <= 1.0
assert 0.0 <= result.recall_at_k <= 1.0
assert 0.0 <= result.hit_rate <= 1.0
assert 0.0 <= result.mean_reciprocal_rank <= 1.0
assert 0.0 <= result.mean_average_precision <= 1.0
assert 0.0 <= result.ndcg_at_k <= 1.0

print(f"[PASS] Precision@5 : {result.precision_at_k:.4f}")
print(f"[PASS] Recall@5    : {result.recall_at_k:.4f}")
print(f"[PASS] Hit Rate    : {result.hit_rate:.4f}")
print(f"[PASS] MRR         : {result.mean_reciprocal_rank:.4f}")
print(f"[PASS] MAP         : {result.mean_average_precision:.4f}")
print(f"[PASS] NDCG@5      : {result.ndcg_at_k:.4f}")

print("=" * 70)
print("ALL EVALUATOR TESTS PASSED")
print("=" * 70)