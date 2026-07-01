"""
Project : Athena
Module  : Dataset Cleaner

Purpose
-------
Cleans raw candidate records before parsing.

Guidelines
----------
- Removes formatting inconsistencies.
- Does not change semantic meaning.
- Operates recursively.
"""

from __future__ import annotations

import unicodedata
from typing import Any


class Cleaner:
    """
    Cleans raw dataset records.
    """

    def clean(
        self,
        records: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """
        Clean every candidate record.
        """

        return [
            self._clean_value(record)
            for record in records
        ]

    def _clean_value(
        self,
        value: Any,
    ) -> Any:
        """
        Recursively clean any supported value.
        """

        if isinstance(value, dict):
            return {
                key: self._clean_value(val)
                for key, val in value.items()
            }

        if isinstance(value, list):
            return [
                self._clean_value(item)
                for item in value
            ]

        if isinstance(value, str):

            text = unicodedata.normalize(
                "NFKC",
                value,
            )

            text = " ".join(text.split())

            if text == "":
                return None

            return text

        return value


###############################################################################
# END OF FILE
###############################################################################