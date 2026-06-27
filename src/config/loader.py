"""
Project : Athena
Module  : Configuration Loader

Purpose
-------
Loads and validates Athena configuration from YAML files.

Guidelines
----------
- No business logic.
- No global state.
- Returns immutable AthenaSettings.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from src.config.schema import AthenaSettings

###############################################################################
# Configuration Loader
###############################################################################


class ConfigLoader:
    """
    Loads Athena configuration from YAML files.
    """

    def __init__(
        self,
        config_path: str | Path = "configs/config.yaml",
    ) -> None:

        self.config_path = Path(config_path)

    def load(
        self,
    ) -> AthenaSettings:
        """
        Load all Athena configuration.
        """

        master_config = self._load_yaml(
            self.config_path
        )

        configuration = master_config["configuration"]

        merged = {
            "project": master_config["project"],
            "environment": master_config["environment"],
            "pipeline": master_config["pipeline"],
            "evaluation": master_config["evaluation"],

           "models": self._load_yaml(
                Path(configuration["models"])
            ),

            "retrieval": self._load_yaml(
                Path(configuration["retrieval"])
            ),

            "ranking": self._load_yaml(
                Path(configuration["ranking"])
            ),

            "weights": self._load_yaml(
                Path(configuration["weights"])
            ),

            "features": self._load_yaml(
                Path(configuration["features"])
             )["features"],

            "paths": self._load_yaml(
                Path(configuration["paths"])
            ),

            "logging": self._load_yaml(
                Path(configuration["logging"])
            ),

           
        }

        return AthenaSettings(
            **merged
    )
    ###############################################################################
# Private Helpers
###############################################################################

    def _load_yaml(
        self,
        path: Path,
    ) -> dict:
        """
        Load one YAML file.
        """

        if not path.exists():

            raise FileNotFoundError(
                f"Configuration file not found: {path}"
            )

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = yaml.safe_load(file)

        if data is None:

            return {}

        return data