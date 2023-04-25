from django.shortcuts import render
from main.models import Campany

# Create your views here.

def Reports(request):
    return render(request,'pages/Reports.html')
