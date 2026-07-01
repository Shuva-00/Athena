"""
Project : Athena
Module  : Skill Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Skill


class SkillParser:
    """
    Parses candidate skills.
    """

    def parse(
        self,
        skill_data: list[dict[str, Any]],
    ) -> list[Skill]:

        if not skill_data:
            return []

        skills: list[Skill] = []

        for record in skill_data:

            skill = Skill(

                name=record.get(
            "name",
            "",
        ),

                proficiency=record.get(
            "proficiency",
        ),

                endorsements=record.get(
            "endorsements",
            0,
        ),

                duration_months=record.get(
            "duration_months",
        ),

        ####################################################
        # Athena-only fields
        ####################################################

                category=None,

                confidence=1.0,
    )

            skills.append(
          skill
    )

        return skills


###############################################################################
# END OF FILE
###############################################################################