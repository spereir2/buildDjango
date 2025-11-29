"""
WSGI config for BookList project.

It exposes the WSGI callable as a module-level variable named ``application``.

This configuration allows the Django application to run in a WSGI (Web Server
Gateway Interface) environment, which is the standard for Python web application
deployment.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookList.settings')

application = get_wsgi_application()
