"""
Project : Athena
Module  : Signal Evidence

Purpose
-------
Stores derived behavioural evidence extracted from candidate signals.

Guidelines
----------
- Pure domain model.
- No business logic.
- No scoring logic.
- No inference logic.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class SignalEvidence(AthenaModel):
    """
    Stores normalized behavioural evidence derived from CandidateSignals.
    """

    ###########################################################################
    # Behaviour Scores
    ###########################################################################

    responsiveness_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Normalized responsiveness score.",
    )

    engagement_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Normalized engagement score.",
    )

    assessment_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Normalized assessment score.",
    )

    ###########################################################################
    # Supporting Statistics
    ###########################################################################

    profile_completeness: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Normalized profile completeness.",
    )

    github_activity: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Normalized GitHub activity.",
    )

    ###########################################################################
    # Confidence
    ###########################################################################

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence in extracted signal evidence.",
    )

    ###########################################################################
    # Explainability
    ###########################################################################

    strengths: list[str] = Field(
        default_factory=list,
        description="Behavioural strengths supporting ranking.",
    )

    concerns: list[str] = Field(
        default_factory=list,
        description="Behavioural concerns affecting ranking.",
    )

    ###########################################################################
# Availability
###########################################################################

    open_to_work: bool = False

    notice_period_days: int = 0

        ###########################################################################
        # Work Preferences
        ###########################################################################

    preferred_work_mode: str = ""

    willing_to_relocate: bool = False

        ###########################################################################
        # Salary
        ###########################################################################

    salary_expectation_min: float = 0

    salary_expectation_max: float = 0

        ###########################################################################
        # Verification
        ###########################################################################

    verified_email: bool = False

    verified_phone: bool = False

    linkedin_connected: bool = False

        ###########################################################################
        # Recruiter Interest
        ###########################################################################

    profile_views: int = 0

    search_appearances: int = 0

    saved_by_recruiters: int = 0

        ###########################################################################
        # Platform Activity
        ###########################################################################

    applications_last_30d: int = 0

    connections: int = 0

    endorsements: int = 0

        ###########################################################################
        # Interview
        ###########################################################################

    interview_completion_rate: float = 0.0

    offer_acceptance_rate: float = 0.0


###############################################################################
# END OF FILE
###############################################################################