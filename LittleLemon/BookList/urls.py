"""
URL configuration for BookList project.

The `urlpatterns` list routes URLs to views. This module acts as the root URL configuration,
dispatching requests to the admin site and the LittleLemonDRF application.

For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('LittleLemonDRF.urls')),
]
