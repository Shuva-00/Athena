"""
Project : Athena
Module  : Base Scorer

Purpose
-------
Defines the common interface for all feature scorers.

Guidelines
----------
- Abstract base class.
- Returns normalized score.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseScorer(ABC):
    """
    Base class for all feature scorers.
    """

    @abstractmethod
    def score(
        self,
        evidence,
    ) -> float:
        """
        Compute normalized score in [0,1].
        """
        raise NotImplementedError