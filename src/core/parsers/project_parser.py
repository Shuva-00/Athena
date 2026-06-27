"""
Project : Athena
Module  : Project Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Project


class ProjectParser:
    """
    Parses candidate projects.
    """

    def parse(
        self,
        project_data: list[dict[str, Any]],
    ) -> list[Project]:

        if not project_data:
            return []

        return [
            Project.model_validate(record)
            for record in project_data
        ]


###############################################################################
# END OF FILE
###############################################################################