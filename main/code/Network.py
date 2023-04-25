from django.shortcuts import render
from main.models import Campany

# Create your views here.

def network(request):

    return render(request,'pages/network.html')