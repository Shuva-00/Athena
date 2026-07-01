"""
ATHENA END-TO-END PIPELINE TEST
"""

from __future__ import annotations

from pathlib import Path

from src.pipeline import Pipeline

print("=" * 70)
print("ATHENA END-TO-END PIPELINE TEST")
print("=" * 70)

###############################################################################
# Paths
###############################################################################

candidate_file = Path(
    "data/raw/sample_candidates.json"
)

job_file = Path(
    "data/raw/job_description.docx"
)

output_directory = Path(
    "outputs"
)

###############################################################################
# Execute Pipeline
###############################################################################

pipeline = Pipeline(
    candidate_file=candidate_file,
    job_file=job_file,
    output_directory=output_directory,
)

pipeline.run()

from src.debug.debug_report import DebugReport
from src.debug.score_audit_report import ScoreAuditReport
candidate = pipeline.candidates[0]
c2=pipeline.candidates[0]
r= ScoreAuditReport()
report = DebugReport()
print(r.generate(candidate))
print(report.generate(candidate))

###############################################################################
# Load Validation
###############################################################################

assert pipeline.job is not None
print("[PASS] Job description loaded")

assert len(pipeline.raw_candidates) > 0
print(f"[PASS] Loaded {len(pipeline.raw_candidates)} raw candidates")

###############################################################################
# Preprocessing Validation
###############################################################################

assert len(pipeline.candidates) > 0
print(f"[PASS] Parsed {len(pipeline.candidates)} candidates")

###############################################################################
# Retrieval Validation
###############################################################################

for candidate in pipeline.candidates:

    assert candidate.scores.retrieval_score >= 0.0

print("[PASS] Retrieval completed")

###############################################################################
# Ranking Validation
###############################################################################

for candidate in pipeline.candidates:

    assert candidate.scores.semantic_score >= 0.0

    assert candidate.features.feature_score >= 0.0

    assert candidate.scores.final_score >= 0.0

    assert candidate.scores.rank is not None

print("[PASS] Ranking completed")

###############################################################################
# Reasoning Validation
###############################################################################

for candidate in pipeline.candidates:

    assert candidate.reason is not None

print("[PASS] Reasoning completed")

###############################################################################
# Submission Validation
###############################################################################

submission = output_directory / "submission.csv"

assert submission.exists()

print("[PASS] Submission generated")

###############################################################################
# Benchmark Validation
###############################################################################

assert pipeline.benchmark_result is not None

assert pipeline.benchmark_result.total_time >= 0.0

print("[PASS] Benchmark recorded")

###############################################################################
# Success
###############################################################################

print("=" * 70)
print("ATHENA V1 END-TO-END PIPELINE PASSED")
print("=" * 70)