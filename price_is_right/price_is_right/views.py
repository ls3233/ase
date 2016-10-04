from django.http import HttpResponse


def index(Request):
    return HttpResponse("Welcome to the price is right.")

