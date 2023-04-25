from django.shortcuts import render
from main.models import Campany

# Create your views here.

def ports(request):
    return render(request,'pages/port.html')