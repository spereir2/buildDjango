from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def drinks(request, drink_name):
    drink_dict = {"mocha" : "type of coffee",
                  "tea" : "type of beverage",
                  "lemonade" : "type of refreshment"}

    choice_of_drink = drink_dict.get(drink_name, "unknown drink")

    return HttpResponse(f"<h2> {drink_name} </h2> is a {choice_of_drink}.")
