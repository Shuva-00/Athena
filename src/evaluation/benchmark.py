"""
Project : Athena
Module  : Benchmark

Purpose
-------
Measures execution time of Athena pipeline stages.

Guidelines
----------
- Measures elapsed time only.
- No evaluation metrics.
- No printing.
"""

from __future__ import annotations

import time

from src.core import BenchmarkResult


class Benchmark:
    """
    Measures execution time of pipeline stages.
    """

    def __init__(self) -> None:

        self._retrieval_start = 0.0
        self._ranking_start = 0.0
        self._reasoning_start = 0.0
        self._preprocessing_start = 0.0
        self._retrieval_time = 0.0
        self._ranking_time = 0.0
        self._reasoning_time = 0.0
        self._preprocessing_time = 0.0

        self._pipeline_start = 0.0

    ###########################################################################
    # Pipeline
    ###########################################################################

    def start_pipeline(self) -> None:

        self._pipeline_start = time.perf_counter()

    def stop_pipeline(self) -> BenchmarkResult:

        total_time = (
            time.perf_counter()
            - self._pipeline_start
        )

        return BenchmarkResult(

    preprocessing_time=self._preprocessing_time,

    retrieval_time=self._retrieval_time,

    ranking_time=self._ranking_time,

    reasoning_time=self._reasoning_time,

    total_time=total_time,
    )
    ###########################################################################
# Preprocessing
###########################################################################

    def start_preprocessing(self) -> None:

        self._preprocessing_start = (
            time.perf_counter()
        )

    def stop_preprocessing(self) -> None:

        self._preprocessing_time = (
            time.perf_counter()
            - self._preprocessing_start
        )
    ###########################################################################
    # Retrieval
    ###########################################################################

    def start_retrieval(self) -> None:

        self._retrieval_start = time.perf_counter()

    def stop_retrieval(self) -> None:

        self._retrieval_time = (
            time.perf_counter()
            - self._retrieval_start
        )
    
    ###########################################################################
    # Ranking
    ###########################################################################

    def start_ranking(self) -> None:

        self._ranking_start = time.perf_counter()

    def stop_ranking(self) -> None:

        self._ranking_time = (
            time.perf_counter()
            - self._ranking_start
        )

    ###########################################################################
    # Reasoning
    ###########################################################################

    def start_reasoning(self) -> None:

        self._reasoning_start = time.perf_counter()

    def stop_reasoning(self) -> None:

        self._reasoning_time = (
            time.perf_counter()
            - self._reasoning_start
        )


###############################################################################
# END OF FILE
###############################################################################