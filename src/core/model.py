"""
Project : Athena
Module  : Base Domain Model

Purpose
-------
Defines the common base model inherited by every domain model
within Athena.

Guidelines
----------
- All domain models inherit from AthenaModel.
- Provides consistent validation and serialization.
- No business logic belongs here.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class AthenaModel(BaseModel):
    """
    Base model for all Athena domain objects.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        populate_by_name=True,
        arbitrary_types_allowed=False,
        frozen=False,
    )

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the model to a Python dictionary.

        Returns
        -------
        dict[str, Any]
            Dictionary representation of the model.
        """
        return self.model_dump()

    def to_json(self) -> str:
        """
        Convert the model to a JSON string.

        Returns
        -------
        str
            JSON representation of the model.
        """
        return self.model_dump_json(indent=4)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "AthenaModel":
        """
        Create an instance from a dictionary.

        Parameters
        ----------
        data : dict[str, Any]
            Input dictionary.

        Returns
        -------
        AthenaModel
            Parsed model instance.
        """
        return cls.model_validate(data)


###############################################################################
# END OF FILE
###############################################################################