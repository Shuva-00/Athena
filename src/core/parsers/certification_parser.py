"""
Project : Athena
Module  : Certification Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Certification
from datetime import date

class CertificationParser:
    """
    Parses candidate certifications.
    """

    def parse(
        self,
        certification_data: list[dict[str, Any]],
    ) -> list[Certification]:

        certifications: list[Certification] = []

        for record in certification_data:

        ############################################################
        # Convert year -> issue_date
        ############################################################

            issue_date = None

            if record.get("year") is not None:

                issue_date = date(
                    record["year"],
                    1,
                    1,
                )

            certification = Certification(

            ########################################################
            # Official Redrob fields
            ########################################################

                name=record.get(
                    "name",
                    "",
                ),

                issuer=record.get(
                    "issuer",
                ),

                issue_date=issue_date,

            ########################################################
            # Athena-only fields
            ########################################################

                expiry_date=None,

                credential_id=None,

                credential_url=None,

                 verified=False,

                skills=[],

                level=None,

                keywords=[],
            )

            certifications.append(
                certification
            )

        return certifications

###############################################################################
# END OF FILE
###############################################################################