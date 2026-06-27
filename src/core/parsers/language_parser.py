"""
Project : Athena
Module  : Language Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Language


class LanguageParser:
    """
    Parses candidate languages.
    """

    def parse(
        self,
        language_data: list[dict[str, Any]],
    ) -> list[Language]:

        if not language_data:
            return []

        return [
            Language.model_validate(record)
            for record in language_data
        ]


###############################################################################
# END OF FILE
###############################################################################