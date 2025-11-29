"""
ASGI config for BookList project.

It exposes the ASGI callable as a module-level variable named ``application``.

This configuration allows the Django application to run in an ASGI (Asynchronous
Server Gateway Interface) environment, which is required for asynchronous features.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookList.settings')

application = get_asgi_application()
