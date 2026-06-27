"""
Project : Athena
Module  : Settings

Purpose
-------
Creates the global immutable configuration object.
"""

from __future__ import annotations

from src.config.loader import ConfigLoader

###############################################################################
# Global Settings
###############################################################################

settings = ConfigLoader().load()

###############################################################################
# END OF FILE
###############################################################################