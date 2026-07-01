"""
ATHENA BENCHMARK TEST
"""

from __future__ import annotations

import time

from src.evaluation import Benchmark

print("=" * 70)
print("ATHENA BENCHMARK TEST")
print("=" * 70)

benchmark = Benchmark()

benchmark.start_pipeline()

benchmark.start_preprocessing()
time.sleep(0.01)
benchmark.stop_preprocessing()

benchmark.start_retrieval()
time.sleep(0.01)
benchmark.stop_retrieval()

benchmark.start_ranking()
time.sleep(0.01)
benchmark.stop_ranking()

benchmark.start_reasoning()
time.sleep(0.01)
benchmark.stop_reasoning()

result = benchmark.stop_pipeline()

assert result.preprocessing_time >= 0
assert result.retrieval_time >= 0
assert result.ranking_time >= 0
assert result.reasoning_time >= 0
assert result.total_time >= 0

print("[PASS] Benchmark timings verified")

print("=" * 70)
print("ALL BENCHMARK TESTS PASSED")
print("=" * 70)