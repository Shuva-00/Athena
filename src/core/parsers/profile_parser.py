"""
Project : Athena
Module  : Profile Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import CandidateProfile


class ProfileParser:
    """
    Parses candidate profile information.
    """

    def parse(
        self,
        profile_data: dict[str, Any],
    ) -> CandidateProfile:

        return CandidateProfile(

            full_name=profile_data.get(
                "anonymized_name"
            ),

            headline=profile_data.get(
                "headline"
            ),

            summary=profile_data.get(
                "summary"
            ),

            location=profile_data.get(
                "location"
            ),

            ####################################################
            # Athena-only fields
            ####################################################

            email=None,

            phone=None,

            linkedin_url=None,

            github_url=None,

            portfolio_url=None,

            credential_url=None,

            total_experience_months=int(
                profile_data.get(
                    "years_of_experience",
                    0,
                ) * 12
            ),

            primary_skills=[],

            secondary_skills=[],

            languages=[],

            certifications=[],

            keywords=[],
        )


###############################################################################
# END OF FILE
###############################################################################