"""
Project : Athena
Module  : Dataset Validator

Purpose
-------
Validates the raw candidate dataset before parsing.

Guidelines
----------
- Validates dataset structure.
- Does not modify data.
- Raises descriptive exceptions.
"""

from __future__ import annotations

from typing import Any

from src.core.constants import REQUIRED_CANDIDATE_FIELDS


class Validator:
    """
    Validates raw candidate records.
    """

    REQUIRED_TOP_LEVEL_FIELDS = REQUIRED_CANDIDATE_FIELDS

    def validate(
        self,
        records: list[dict[str, Any]],
    ) -> None:
        """
        Validate all candidate records.
        """

        seen_ids: set[str] = set()

        for index, record in enumerate(records, start=1):
            self._validate_record(
                record,
                index,
                seen_ids,
            )

    def _validate_record(
        self,
        record: dict[str, Any],
        index: int,
        seen_ids: set[str],
    ) -> None:
        """
        Validate one candidate record.
        """

        for field in self.REQUIRED_TOP_LEVEL_FIELDS:
            if field not in record:
                raise ValueError(
                    f"Record {index}: Missing required field '{field}'."
                )

        candidate_id = record["candidate_id"]

        if not isinstance(candidate_id, str):
            raise TypeError(
                f"Record {index}: candidate_id must be a string."
            )

        if candidate_id in seen_ids:
            raise ValueError(
                f"Duplicate candidate_id: {candidate_id}"
            )

        seen_ids.add(candidate_id)

        self._validate_types(
            record,
            index,
        )

    def _validate_types(
        self,
        record: dict[str, Any],
        index: int,
    ) -> None:
        """
        Validate top-level field types.
        """

        if not isinstance(record["profile"], dict):
            raise TypeError(
                f"Record {index}: profile must be an object."
            )

        if not isinstance(record["education"], list):
            raise TypeError(
                f"Record {index}: education must be a list."
            )

        if not isinstance(record["career_history"], list):
            raise TypeError(
                f"Record {index}: career_history must be a list."
            )

        if not isinstance(record["skills"], list):
            raise TypeError(
                f"Record {index}: skills must be a list."
            )

        if not isinstance(record["certifications"], list):
            raise TypeError(
                f"Record {index}: certifications must be a list."
            )

        if not isinstance(record["languages"], list):
            raise TypeError(
                f"Record {index}: languages must be a list."
            )

        if not isinstance(record["redrob_signals"], dict):
            raise TypeError(
                f"Record {index}: redrob_signals must be an object."
            )


###############################################################################
# END OF FILE
###############################################################################