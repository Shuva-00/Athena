"""
Project : Athena
Module  : Education Parser

Purpose
-------
Converts raw Redrob education records into Athena Education models.
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Education
from src.core.enums import DegreeLevel
from src.core.enums import (
    DegreeLevel,
    InstitutionTier,
)

class EducationParser:
    """
    Parses candidate education records.
    """

    ###########################################################################
    # Degree Level Inference
    ###########################################################################

    def _infer_degree_level(
        self,
        degree: str,
    ) -> DegreeLevel:
        """
        Infer normalized degree level from the raw degree text.
        """

        degree = degree.lower().strip()

        #######################################################################
        # Bachelor
        #######################################################################

        if any(
            keyword in degree
            for keyword in [
                "b.tech",
                "btech",
                "b.e",
                "be",
                "b.sc",
                "bsc",
                "bca",
                "b.com",
                "bcom",
                "ba",
                "b.a",
                "llb",
                "mbbs",
            ]
        ):
            return DegreeLevel.BACHELOR

        #######################################################################
        # Master
        #######################################################################

        if any(
            keyword in degree
            for keyword in [
                "m.tech",
                "mtech",
                "m.e",
                "me",
                "m.sc",
                "msc",
                "mba",
                "mca",
                "m.com",
                "mcom",
                "ma",
                "m.a",
                "llm",
                "md",
                "ms",
            ]
        ):
            return DegreeLevel.MASTER

        #######################################################################
        # Doctorate
        #######################################################################

        if any(
            keyword in degree
            for keyword in [
                "phd",
                "ph.d",
                "doctor",
                "doctorate",
                "d.phil",
            ]
        ):
            return DegreeLevel.DOCTORATE

        #######################################################################
        # Diploma
        #######################################################################

        if any(
            keyword in degree
            for keyword in [
                "diploma",
                "polytechnic",
            ]
        ):
            return DegreeLevel.DIPLOMA

        #######################################################################
        # Default
        #######################################################################

        return DegreeLevel.OTHER
    
    def _infer_institution_tier(
        self,
        tier: str | None,
    ) -> InstitutionTier:
        """
       Normalize Redrob institution tier values.
        """

        if tier is None:
            return InstitutionTier.UNKNOWN

        tier = tier.strip().upper()

        mapping = {
            "TIER_1": InstitutionTier.TIER_1,
            "TIER_2": InstitutionTier.TIER_2,
            "TIER_3": InstitutionTier.TIER_3,
        }

        return mapping.get(
            tier,
            InstitutionTier.UNKNOWN,
        )

    ###########################################################################
    # Parser
    ###########################################################################
     
    def parse(
        self,
        education_data: list[dict[str, Any]],
    ) -> list[Education]:

        educations: list[Education] = []

        for record in education_data:

            education = Education(

                ################################################################
                # Core
                ################################################################

                institution=record.get(
                    "institution",
                    "",
                ),

                degree=record.get(
                    "degree",
                    "",
                ),

                field_of_study=record.get(
                    "field_of_study",
                    "",
                ),

                ################################################################
                # Timeline
                ################################################################

                start_year=record.get(
                    "start_year",
                ),

                end_year=record.get(
                    "end_year",
                ),

                ################################################################
                # Academic Performance
                ################################################################

                grade=record.get(
                    "grade",
                ),

                tier=self._infer_institution_tier(
                     record.get(
                        "tier",
                    )
                ),

                ################################################################
                # Athena Normalization
                ################################################################

                degree_level=self._infer_degree_level(
                    record.get(
                        "degree",
                        "",
                    )
                ),

                ################################################################
                # Athena-only fields
                ################################################################

                cgpa=None,

                relevant_courses=[],

                research_projects=[],

                publications=[],
            )

            educations.append(
                education
            )

        return educations


###############################################################################
# END OF FILE
###############################################################################