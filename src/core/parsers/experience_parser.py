"""
Project : Athena
Module  : Experience Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Experience


class ExperienceParser:
    """
    Converts raw Redrob experience records into Athena Experience models.
    """

    def parse(
        self,
        experience_data: list[dict[str, Any]],
    ) -> list[Experience]:

        experiences: list[Experience] = []

        for record in experience_data:

            experience = Experience(

                ################################################################
                # Core
                ################################################################

                company=record.get(
                    "company",
                    "",
                ),

                job_title=record.get(
                    "title",
                    "",
                ),

                ################################################################
                # Employment
                ################################################################

                employment_type=record.get(
                    "employment_type",
                ),

                location=record.get(
                    "location",
                ),

                start_date=record.get(
                    "start_date",
                ),

                end_date=record.get(
                    "end_date",
                ),

                is_current=record.get(
                    "is_current",
                    False,
                ),

                ################################################################
                # Metadata
                ################################################################

                industry=record.get(
                    "industry",
                ),

                company_size=record.get(
                    "company_size",
                ),

                duration_months=record.get(
                    "duration_months",
                ),

                ################################################################
                # Description
                ################################################################

                responsibilities=[
                    record["description"]
                ]
                if record.get("description")
                else [],

                achievements=[],

                technologies=[],

                skills=[],

                keywords=[],

                impact_metrics={},
            )

            experiences.append(
                experience
            )

        return experiences


###############################################################################
# END OF FILE
###############################################################################