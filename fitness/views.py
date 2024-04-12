from django.http import HttpResponse
from django.shortcuts import render

from datetime import date
from dateutil.relativedelta import relativedelta

from .models import BodyComposition


def home_view(request):
    #return HttpResponse("This is the home page of my future fitness web app")

    # Get all Body Composition Data
    body_composition = BodyComposition.objects.all().order_by('date')

    # Get latest Body Composition Data
    latest_body_composition = BodyComposition.objects.latest('date')

    # Get a specific month's Body Composition Data
    jan_body_composition = BodyComposition.objects.filter(
        date__year = '2024',
        date__month = '01')
    
    # Get a specific month's Body Composition Reverse Data
    jan_reverse_body_composition = BodyComposition.objects.filter(
        date__year = '2024',
        date__month = '01').order_by('date')
    
    # Get a specific date range of Body Composition Data
    six_month_body_composition = BodyComposition.objects.filter(date__range=["2023-10-4", "2024-4-4"])

    # Testing DateTime
    today = date.today()

    six_months_ago = today - relativedelta(months=-6)

    context = {
        'body_composition':body_composition,
        'latest_body_composition':latest_body_composition,
        'jan_body_composition':jan_body_composition,
        'jan_reverse_body_composition': jan_reverse_body_composition,
        'six_month_body_composition':six_month_body_composition,
        'today':today,
        'six_months_ago':six_months_ago,
    }
    return render(request, "fitness/home.html", context)