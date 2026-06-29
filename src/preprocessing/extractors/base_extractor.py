"""
Project : Athena
Module  : Base Extractor

Purpose
-------
Defines the common interface for all evidence extractors.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from src.core.candidate.entity import Candidate
from src.core.job.job_description import JobDescription


class BaseExtractor(ABC):
    """
    Base class for all evidence extractors.
    """

    @abstractmethod
    def extract(
        self,
        candidate: Candidate,
        job: JobDescription,
    ):
        """
        Extract raw evidence from a candidate.
        """
        raise NotImplementedError