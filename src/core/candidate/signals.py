"""
Project : Athena
Module  : Candidate Signals

Purpose
-------
Defines the structured Redrob behavioural signals associated
with a candidate.

Guidelines
----------
- Mirrors the Redrob dataset exactly.
- Pure domain model.
- No scoring logic.
"""

from __future__ import annotations

from datetime import date
from src.core.enums import WorkMode
from pydantic import Field
from src.core.model import AthenaModel


class SalaryRange(AthenaModel):
    """
    Expected salary range in Lakhs Per Annum (LPA).
    """

    minimum: float = Field(
        ...,
        ge=0,
        description="Minimum expected salary (LPA).",
    )

    maximum: float = Field(
        ...,
        ge=0,
        description="Maximum expected salary (LPA).",
    )


class CandidateSignals(AthenaModel):
    """
    Behavioural signals from the Redrob platform.
    """

    profile_completeness_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Profile completeness score.",
    )

    signup_date: date = Field(
        ...,
        description="Candidate signup date.",
    )

    last_active_date: date = Field(
        ...,
        description="Last activity date.",
    )

    open_to_work_flag: bool = Field(
        ...,
        description="Whether the candidate is open to work.",
    )

    profile_views_received_30d: int = Field(
        ...,
        ge=0,
        description="Profile views received in the last 30 days.",
    )

    applications_submitted_30d: int = Field(
        ...,
        ge=0,
        description="Applications submitted in the last 30 days.",
    )

    recruiter_response_rate: float = Field(
        ...,
        ge=0,
        le=1,
        description="Recruiter response rate.",
    )

    avg_response_time_hours: float = Field(
        ...,
        ge=0,
        description="Average recruiter response time.",
    )

    skill_assessment_scores: dict[str, float] = Field(
        default_factory=dict,
        description="Per-skill assessment scores.",
    )

    connection_count: int = Field(
        ...,
        ge=0,
        description="Number of Redrob connections.",
    )

    endorsements_received: int = Field(
        ...,
        ge=0,
        description="Total endorsements received.",
    )
    
    notice_period_days: int = Field(
        ...,
        ge=0,
        le=180,
        description="Notice period in days.",
    )

    expected_salary_range_inr_lpa: SalaryRange = Field(
        ...,
        description="Expected salary range.",
    )

    preferred_work_mode: WorkMode = Field(
        ...,
        description="Preferred work mode.",
    )

    willing_to_relocate: bool = Field(
        ...,
        description="Whether willing to relocate.",
    )

    github_activity_score: float = Field(
        ...,
        ge=-1,
        le=100,
        description="GitHub activity score.",
    )

    search_appearance_30d: int = Field(
        ...,
        ge=0,
        description="Recruiter search appearances.",
    )

    saved_by_recruiters_30d: int = Field(
        ...,
        ge=0,
        description="Saved by recruiters in last 30 days.",
    )

    interview_completion_rate: float = Field(
        ...,
        ge=0,
        le=1,
        description="Interview completion rate.",
    )

    offer_acceptance_rate: float = Field(
        ...,
        ge=-1,
        le=1,
        description="Offer acceptance rate.",
    )

    verified_email: bool = Field(
        ...,
        description="Email verification status.",
    )

    verified_phone: bool = Field(
        ...,
        description="Phone verification status.",
    )

    linkedin_connected: bool = Field(
        ...,
        description="LinkedIn connection status.",
    )
    

###############################################################################
# END OF FILE
###############################################################################