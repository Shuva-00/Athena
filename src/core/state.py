"""
Project : Athena
Module  : Pipeline State Machine

Purpose
-------
Manages the execution state of the Athena pipeline.

Responsibilities
----------------
- Track current pipeline state.
- Validate state transitions.
- Prevent invalid execution order.
- Allow deterministic execution.
"""

from __future__ import annotations

from src.core.enums import PipelineState
from src.core.exceptions import PipelineStateError


class PipelineStateMachine:
    """
    Controls the execution lifecycle of the Athena pipeline.
    """

    _TRANSITIONS = {
        PipelineState.INITIALIZED: PipelineState.DATA_READY,
        PipelineState.DATA_READY: PipelineState.PREPROCESSING_READY,
        PipelineState.PREPROCESSING_READY: PipelineState.INTENT_READY,
        PipelineState.INTENT_READY: PipelineState.RETRIEVAL_READY,
        PipelineState.RETRIEVAL_READY: PipelineState.RERANK_READY,
        PipelineState.RERANK_READY: PipelineState.EVIDENCE_READY,
        PipelineState.EVIDENCE_READY: PipelineState.SCORING_READY,
        PipelineState.SCORING_READY:
        PipelineState.EVALUATION_READY,

PipelineState.EVALUATION_READY:
PipelineState.VALIDATION_READY,
    }

    def __init__(self) -> None:
        self._state = PipelineState.INITIALIZED

    @property
    def current_state(self) -> PipelineState:
        """
        Return the current pipeline state.
        """
        return self._state

    def can_transition(self, next_state: PipelineState) -> bool:
        """
        Check whether the requested transition is valid.
        """
        return self._TRANSITIONS.get(self._state) == next_state

    def transition(self, next_state: PipelineState) -> None:
        """
        Move the pipeline to the next valid state.
        """
        if not self.can_transition(next_state):
            raise PipelineStateError(
                f"Invalid transition: {self._state.value} -> {next_state.value}"
            )

        self._state = next_state

    def reset(self) -> None:
        """
        Reset pipeline execution.
        """
        self._state = PipelineState.INITIALIZED

    def is_completed(self) -> bool:
        """
        Check whether pipeline reached the final state.
        """
        return self._state == PipelineState.SUBMISSION_READY


###############################################################################
# END OF FILE
###############################################################################