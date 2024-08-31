from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    if request.htmx:
        print(request.htmx) # only exist if the wiew is called from htmx anchors/buttons)

    else:
        print("No htmx")
    return HttpResponse("success")