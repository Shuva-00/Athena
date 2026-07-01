"""
Project : Athena
Module  : Evaluation Metrics

Purpose
-------
Provides standard information retrieval evaluation metrics.

Guidelines
----------
- Pure mathematical functions.
- No file I/O.
- No logging.
- No printing.
"""

from __future__ import annotations

import math


def precision_at_k(
    relevant: set[str],
    predicted: list[str],
    k: int,
) -> float:
    """
    Compute Precision@K.
    """

    if k <= 0:
        raise ValueError("k must be positive.")

    predicted = predicted[:k]

    if not predicted:
        return 0.0

    hits = sum(
        candidate in relevant
        for candidate in predicted
    )

    return hits / len(predicted)


def recall_at_k(
    relevant: set[str],
    predicted: list[str],
    k: int,
) -> float:
    """
    Compute Recall@K.
    """

    if not relevant:
        return 0.0

    predicted = predicted[:k]

    hits = sum(
        candidate in relevant
        for candidate in predicted
    )

    return hits / len(relevant)


def hit_rate(
    relevant: set[str],
    predicted: list[str],
    k: int,
) -> float:
    """
    Compute Hit Rate@K.
    """

    predicted = predicted[:k]

    return float(
        any(
            candidate in relevant
            for candidate in predicted
        )
    )


def mean_reciprocal_rank(
    relevant: set[str],
    predicted: list[str],
) -> float:
    """
    Compute Mean Reciprocal Rank (MRR).
    """

    for rank, candidate in enumerate(
        predicted,
        start=1,
    ):

        if candidate in relevant:
            return 1.0 / rank

    return 0.0


def mean_average_precision(
    relevant: set[str],
    predicted: list[str],
) -> float:
    """
    Compute Mean Average Precision (MAP).
    """

    if not relevant:
        return 0.0

    hits = 0
    precision_sum = 0.0

    for rank, candidate in enumerate(
        predicted,
        start=1,
    ):

        if candidate in relevant:

            hits += 1

            precision_sum += hits / rank

    return precision_sum / len(relevant)

def ndcg_at_k(
    relevant: set[str],
    predicted: list[str],
    k: int,
) -> float:
    """
    Compute Normalized Discounted Cumulative Gain.
    """

    predicted = predicted[:k]

    dcg = 0.0

    for rank, candidate in enumerate(
        predicted,
        start=1,
    ):

        if candidate in relevant:
            dcg += 1.0 / math.log2(rank + 1)

    ideal_hits = min(
        len(relevant),
        k,
    )

    idcg = sum(
        1.0 / math.log2(rank + 1)
        for rank in range(
            1,
            ideal_hits + 1,
        )
    )

    if idcg == 0:
        return 0.0

    return dcg / idcg


###############################################################################
# END OF FILE
###############################################################################