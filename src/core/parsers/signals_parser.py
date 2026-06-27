"""
Project : Athena
Module  : Signals Parser
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import CandidateSignals


class SignalsParser:
    """
    Parses candidate behavioural signals.
    """

    def parse(
        self,
        signals_data: dict[str, Any],
    ) -> CandidateSignals | None:

        if not signals_data:
            return None

        return CandidateSignals.model_validate(signals_data)


###############################################################################
# END OF FILE
###############################################################################