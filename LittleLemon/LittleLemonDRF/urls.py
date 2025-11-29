"""
This module defines the URL patterns for the LittleLemonDRF application.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('ratings', views.RatingsView.as_view()),
]
