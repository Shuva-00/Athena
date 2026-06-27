"""
Project : Athena
Module  : Component Registry

Purpose
-------
Central registry for executable Athena components.

Responsibilities
----------------
- Register components
- Retrieve components
- Prevent duplicate registration
- List registered components
- Clear registry (mainly for testing)

Notes
-----
This registry stores component instances, not classes.
"""

from __future__ import annotations

from src.core.base import BaseComponent
from src.core.exceptions import ConfigurationError


class ComponentRegistry:
    """
    Central registry for Athena components.
    """

    def __init__(self) -> None:
        self._components: dict[str, BaseComponent] = {}

    def register(self, component: BaseComponent) -> None:
        """
        Register a component.

        Raises
        ------
        ConfigurationError
            If a component with the same name is already registered.
        """
        if component.name in self._components:
            raise ConfigurationError(
                f"Component '{component.name}' is already registered."
            )

        self._components[component.name] = component

    def get(self, name: str) -> BaseComponent:
        """
        Retrieve a registered component.

        Raises
        ------
        ConfigurationError
            If the component does not exist.
        """
        if name not in self._components:
            raise ConfigurationError(
                f"Component '{name}' is not registered."
            )

        return self._components[name]

    def contains(self, name: str) -> bool:
        """
        Check whether a component is registered.
        """
        return name in self._components

    def remove(self, name: str) -> None:
        """
        Remove a registered component.

        Raises
        ------
        ConfigurationError
            If the component does not exist.
        """
        if name not in self._components:
            raise ConfigurationError(
                f"Component '{name}' is not registered."
            )

        del self._components[name]

    def list_components(self) -> list[str]:
        """
        Return a sorted list of registered component names.
        """
        return sorted(self._components.keys())

    def clear(self) -> None:
        """
        Remove all registered components.
        """
        self._components.clear()

    def __len__(self) -> int:
        """
        Return the number of registered components.
        """
        return len(self._components)


###############################################################################
# END OF FILE
###############################################################################