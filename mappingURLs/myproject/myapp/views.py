"""
This module defines the views for the myapp application.
"""
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def drinks(request, drink_name):
    """
    Handles requests for drink information.

    Args:
        request (HttpRequest): The request object used to generate this response.
        drink_name (str): The name of the drink to retrieve information about.

    Returns:
        HttpResponse: An HTTP response containing a description of the drink.
    """
    drink_dict = {"mocha" : "type of coffee",
                  "tea" : "type of beverage",
                  "lemonade" : "type of refreshment"}

    choice_of_drink = drink_dict.get(drink_name, "unknown drink")

    return HttpResponse(f"<h2> {drink_name} </h2> is a {choice_of_drink}.")
