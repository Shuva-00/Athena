"""
Project : Athena
Module  : Education Parser

Purpose
-------
Parses raw education data into Education domain objects.
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Education


class EducationParser:
    """
    Parses candidate education records.
    """

    def parse(
        self,
        education_data: list[dict[str, Any]],
    ) -> list[Education]:
        """
        Convert raw education records into Education objects.
        """

        if not education_data:
            return []

        return [
            Education.model_validate(record)
            for record in education_data
        ]


###############################################################################
# END OF FILE
###############################################################################