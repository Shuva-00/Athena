"""
Project : Athena
Module  : Signal Extractor

Purpose
-------
Extracts behavioural evidence from candidate signals.

Guidelines
----------
- No scoring.
- No ranking.
- No weighting.
- Populates SignalEvidence only.
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.core.candidate.signal_evidence import SignalEvidence
from src.core.job.job_description import JobDescription
from .base_extractor import BaseExtractor


class SignalExtractor(BaseExtractor):
    """
    Extracts behavioural evidence from CandidateSignals.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def extract(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> SignalEvidence:

        evidence = SignalEvidence()

        if candidate.signals is None:

            candidate.evidence.signal = evidence

            return evidence

        self._extract_responsiveness(
            candidate,
            evidence,
        )

        self._extract_engagement(
            candidate,
            evidence,
        )

        self._extract_assessment(
            candidate,
            evidence,
        )

        self._extract_profile(
            candidate,
            evidence,
        )

        self._extract_github(
            candidate,
            evidence,
        )

        self._extract_confidence(
            candidate,
            evidence,
        )

        candidate.evidence.signal = evidence

        return evidence

    ###########################################################################
    # Responsiveness
    ###########################################################################

    def _extract_responsiveness(
        self,
        candidate: Candidate,
        evidence: SignalEvidence,
    ) -> None:

        signals = candidate.signals

        response_rate = signals.recruiter_response_rate

        response_time = max(
            0.0,
            1.0 - min(
                signals.avg_response_time_hours / 72.0,
                1.0,
            ),
        )

        evidence.responsiveness_score = (
            response_rate + response_time
        ) / 2.0

    ###########################################################################
    # Engagement
    ###########################################################################

    def _extract_engagement(
        self,
        candidate: Candidate,
        evidence: SignalEvidence,
    ) -> None:

        signals = candidate.signals

        views = min(
            signals.profile_views_received_30d / 100.0,
            1.0,
        )

        searches = min(
            signals.search_appearance_30d / 100.0,
            1.0,
        )

        saved = min(
            signals.saved_by_recruiters_30d / 25.0,
            1.0,
        )

        evidence.engagement_score = (
            views +
            searches +
            saved
        ) / 3.0

    ###########################################################################
    # Assessment
    ###########################################################################

    def _extract_assessment(
        self,
        candidate: Candidate,
        evidence: SignalEvidence,
    ) -> None:

        signals = candidate.signals

        if signals.skill_assessment_scores:

            average = (
                sum(
                    signals.skill_assessment_scores.values()
                )
                /
                len(
                    signals.skill_assessment_scores
                )
            ) / 100.0

        else:

            average = 0.0

        evidence.assessment_score = (

            average +

            signals.interview_completion_rate

        ) / 2.0

    ###########################################################################
    # Profile
    ###########################################################################

    def _extract_profile(
        self,
        candidate: Candidate,
        evidence: SignalEvidence,
    ) -> None:

        evidence.profile_completeness = (

            candidate.signals.profile_completeness_score

            / 100.0

        )

    ###########################################################################
    # GitHub
    ###########################################################################

    def _extract_github(
        self,
        candidate: Candidate,
        evidence: SignalEvidence,
    ) -> None:

        evidence.github_activity = (

            candidate.signals.github_activity_score

            / 100.0

        )

    ###########################################################################
    # Confidence
    ###########################################################################

    def _extract_confidence(
        self,
        candidate: Candidate,
        evidence: SignalEvidence,
    ) -> None:

        evidence.confidence = 1.0