"""
This module defines the URL patterns for the myapp application.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
