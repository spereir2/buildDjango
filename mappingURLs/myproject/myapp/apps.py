"""
This module contains the application configuration for myapp.
"""
from django.apps import AppConfig


class MyappConfig(AppConfig):
    """
    Configuration for the myapp application.

    This class sets the default auto field type and the application name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
