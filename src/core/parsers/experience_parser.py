"""
Project : Athena
Module  : Experience Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Experience


class ExperienceParser:
    """
    Parses candidate experience records.
    """

    def parse(
        self,
        experience_data: list[dict[str, Any]],
    ) -> list[Experience]:

        if not experience_data:
            return []

        return [
            Experience.model_validate(record)
            for record in experience_data
        ]


###############################################################################
# END OF FILE
###############################################################################