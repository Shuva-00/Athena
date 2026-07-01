"""
Project : Athena
Module  : Signals Parser

Purpose
-------
Converts raw Redrob behavioural signals into Athena
CandidateSignals models.
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import (
    CandidateSignals,
    SalaryRange,
)
from src.core.enums import WorkMode


class SignalsParser:
    """
    Parses candidate behavioural signals.
    """

    def parse(
        self,
        signals_data: dict[str, Any],
    ) -> CandidateSignals | None:

        if not signals_data:
            return None

        #######################################################################
        # Salary Mapping
        #######################################################################

        salary_data = signals_data.get(
            "expected_salary_range_inr_lpa",
            {},
        )

        salary_range = SalaryRange(
            minimum=salary_data.get(
                "min",
                0.0,
            ),
            maximum=salary_data.get(
                "max",
                0.0,
            ),
        )

        #######################################################################
        # Candidate Signals
        #######################################################################

        return CandidateSignals(

            profile_completeness_score=signals_data.get(
                "profile_completeness_score",
                0.0,
            ),

            signup_date=signals_data.get(
                "signup_date",
            ),

            last_active_date=signals_data.get(
                "last_active_date",
            ),

            open_to_work_flag=signals_data.get(
                "open_to_work_flag",
                False,
            ),

            profile_views_received_30d=signals_data.get(
                "profile_views_received_30d",
                0,
            ),

            applications_submitted_30d=signals_data.get(
                "applications_submitted_30d",
                0,
            ),

            recruiter_response_rate=signals_data.get(
                "recruiter_response_rate",
                0.0,
            ),

            avg_response_time_hours=signals_data.get(
                "avg_response_time_hours",
                0.0,
            ),

            skill_assessment_scores=signals_data.get(
                "skill_assessment_scores",
                {},
            ),

            connection_count=signals_data.get(
                "connection_count",
                0,
            ),

            endorsements_received=signals_data.get(
                "endorsements_received",
                0,
            ),

            notice_period_days=signals_data.get(
                "notice_period_days",
                0,
            ),

            expected_salary_range_inr_lpa=salary_range,

            preferred_work_mode=WorkMode(
                signals_data.get(
                    "preferred_work_mode",
                    "remote",
                )
            ),

            willing_to_relocate=signals_data.get(
                "willing_to_relocate",
                False,
            ),

            github_activity_score=signals_data.get(
                "github_activity_score",
                -1,
            ),

            search_appearance_30d=signals_data.get(
                "search_appearance_30d",
                0,
            ),

            saved_by_recruiters_30d=signals_data.get(
                "saved_by_recruiters_30d",
                0,
            ),

            interview_completion_rate=signals_data.get(
                "interview_completion_rate",
                0.0,
            ),

            offer_acceptance_rate=signals_data.get(
                "offer_acceptance_rate",
                -1.0,
            ),

            verified_email=signals_data.get(
                "verified_email",
                False,
            ),

            verified_phone=signals_data.get(
                "verified_phone",
                False,
            ),

            linkedin_connected=signals_data.get(
                "linkedin_connected",
                False,
            ),
        )


###############################################################################
# END OF FILE
###############################################################################