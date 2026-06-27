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

        return [
            Skill.model_validate(record)
            for record in skill_data
        ]


###############################################################################
# END OF FILE
###############################################################################