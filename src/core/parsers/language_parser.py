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

        languages: list[Language] = []

        for record in language_data:

            language = Language(

            ########################################################
            # Redrob -> Athena mapping
            ########################################################

                name=record.get(
                    "language",
                    "",
                ),

                proficiency=record.get(
                    "proficiency",
                ),
            )

            languages.append(
                language
            )

        return languages