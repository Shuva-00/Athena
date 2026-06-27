"""
Project : Athena
Module  : Submission Packager

Purpose
-------
Packages submission artifacts into a ZIP archive.

Guidelines
----------
- No validation.
- No formatting.
- No ranking.
- Packages existing files only.
"""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile


class Packager:
    """
    Packages submission artifacts.
    """

    def package(
        self,
        files: list[str | Path],
        output_zip: str | Path,
    ) -> None:
        """
        Package files into a ZIP archive.
        """

        output_zip = Path(output_zip)

        output_zip.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with ZipFile(
            output_zip,
            mode="w",
            compression=ZIP_DEFLATED,
        ) as archive:

            for file in files:

                file = Path(file)

                if not file.exists():
                    raise FileNotFoundError(
                        f"File not found: {file}"
                    )

                archive.write(
                    filename=file,
                    arcname=file.name,
                )


###############################################################################
# END OF FILE
###############################################################################