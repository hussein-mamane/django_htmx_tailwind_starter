from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

def tlwnd(request):
    if request.htmx:
        print(request.htmx)

    else:
        print("No htmx")
    return render(request,'base.html',{"data":request.htmx})