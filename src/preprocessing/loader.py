"""
Project : Athena
Module  : Data Loader

Purpose
-------
Loads candidate and job description datasets.

Guidelines
----------
- Reads JSONL and JSON files.
- No parsing.
- No validation.
- No cleaning.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Loader:
    """
    Loads Athena datasets.
    """

    def load_candidates(
        self,
        path: str | Path,
    ) -> list[dict[str, Any]]:
        """
        Load candidate records from a JSONL file.
        """

        records: list[dict[str, Any]] = []

        with Path(path).open(
            "r",
            encoding="utf-8",
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                records.append(json.loads(line))

        return records

    def load_job_description(
        self,
        path: str | Path,
    ) -> dict[str, Any]:
        """
        Load a job description JSON file.
        """

        with Path(path).open(
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)


###############################################################################
# END OF FILE
###############################################################################