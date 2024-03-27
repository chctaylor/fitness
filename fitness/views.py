from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    #return HttpResponse("This is the home page of my future fitness web app")
    return render(request, "fitness/home.html")