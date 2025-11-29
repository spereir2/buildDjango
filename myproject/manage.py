#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This module is the entry point for running the Django application, executing
management commands, and performing other administrative tasks via the
command line.
"""
import os
import sys


def main():
    """
    Run administrative tasks.

    This function configures the Django environment and executes command-line
    utilities. It expects the DJANGO_SETTINGS_MODULE environment variable
    to be set, defaulting to 'myproject.settings'.

    Args:
        None

    Returns:
        None
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
