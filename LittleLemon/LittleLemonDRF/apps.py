"""
This module contains the application configuration for LittleLemonDRF.
"""
from django.apps import AppConfig


class LittlelemondrfConfig(AppConfig):
    """
    Configuration for the LittleLemonDRF application.

    This class sets the default auto field type and the application name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LittleLemonDRF'
