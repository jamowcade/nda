from django.shortcuts import render
from main.models import Campany

# Create your views here.

def compare(request):
    return render(request,'pages/compare.html')
