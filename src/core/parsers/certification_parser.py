"""
Project : Athena
Module  : Certification Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Certification


class CertificationParser:
    """
    Parses candidate certifications.
    """

    def parse(
        self,
        certification_data: list[dict[str, Any]],
    ) -> list[Certification]:

        if not certification_data:
            return []

        return [
            Certification.model_validate(record)
            for record in certification_data
        ]


###############################################################################
# END OF FILE
###############################################################################