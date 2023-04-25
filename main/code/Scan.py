from django.shortcuts import render
from main.models import Campany

# Create your views here.

def scan_case(request):
    return render(request,'pages/scan_case.html')