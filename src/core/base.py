"""
Project : Athena
Module  : Base Component

Purpose
-------
Provides the common implementation shared by all executable
components in Athena.

Guidelines
----------
- Inherit from AthenaComponent.
- Contains shared functionality only.
- Do NOT implement business logic here.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any

from src.core.interfaces import AthenaComponent


class BaseComponent(AthenaComponent):
    """
    Base implementation for all Athena components.

    Provides common functionality such as component naming,
    initialization state, and lifecycle helpers.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the component.

        Parameters
        ----------
        name : str
            Human-readable component name.
        """
        self._name = name
        self._initialized = False

    @property
    def name(self) -> str:
        """
        Return the component name.
        """
        return self._name

    @property
    def initialized(self) -> bool:
        """
        Return whether the component has been initialized.
        """
        return self._initialized

    def initialize(self) -> None:
        """
        Mark the component as initialized.
        """
        self._initialized = True

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the component.

        Must be implemented by subclasses.
        """
        raise NotImplementedError

    @abstractmethod
    def validate(self) -> bool:
        """
        Validate the component output.

        Must be implemented by subclasses.
        """
        raise NotImplementedError

    def cleanup(self) -> None:
        """
        Release resources held by the component.
        """
        self._initialized = False


###############################################################################
# END OF FILE
###############################################################################