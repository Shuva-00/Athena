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
from docx import Document

class Loader:
    """
    Loads Athena datasets.
    """

    def load_candidates(
        self,
        path: str | Path,
    ) -> list[dict[str, Any]]:
        """
        Load candidate records from either
        JSON or JSONL.
        """

        path = Path(path)

    #######################################################################
    # JSON
    #######################################################################

        if path.suffix.lower() == ".json":

            with path.open(
                "r",
                encoding="utf-8",
            ) as file:

                return json.load(file)

    #######################################################################
    # JSONL
    #######################################################################

        if path.suffix.lower() == ".jsonl":

            records: list[dict[str, Any]] = []

            with path.open(
                "r",
                encoding="utf-8",
            ) as file:

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    records.append(
                        json.loads(line)
                    )

            return records

    #######################################################################
    # Unsupported
    #######################################################################

        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    def load_job_description(
        self,
        path: str | Path,
    ) -> dict[str, Any]:
        """
       Load a job description from either JSON or DOCX.
        """

        path = Path(path)

    #######################################################################
    # JSON
    #######################################################################

        if path.suffix.lower() == ".json":

            with path.open(
                "r",
                encoding="utf-8",
            ) as file:

                return json.load(file)

    #######################################################################
    # DOCX
    #######################################################################

        if path.suffix.lower() == ".docx":

            document = Document(path)

            text = "\n".join(

                paragraph.text

                for paragraph in document.paragraphs

                if paragraph.text.strip()

            )

            return {
                "raw_text": text,
           }

    #######################################################################
    # Unsupported
    #######################################################################

        raise ValueError(
            f"Unsupported job description format: {path.suffix}"
        )


###############################################################################
# END OF FILE
###############################################################################