"""
This module defines the views for the myapp application.
"""
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    """
    Handles the request for the home page.

    Args:
        request (HttpRequest): The request object used to generate this response.

    Returns:
        HttpResponse: An HTTP response containing the welcome message "Welcome to Little Lemon!".
    """
    return HttpResponse("<h1> Welcome to Little Lemon! </h1>")
