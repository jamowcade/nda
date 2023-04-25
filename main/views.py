from django.shortcuts import render
from main.models import Campany,Network

# Create your views here.

def index(request):
    totalCompany = Campany.objects.count()
    totalNetwork = Network.objects.count()
    context = {
        'company':totalCompany,
        'network':totalNetwork
        }    
    return render(request, 'index.html',context)



