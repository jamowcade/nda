from django.shortcuts import render
from main.models import Campany

# Create your views here.
def host(request):

    return render(request,'pages/host.html')
