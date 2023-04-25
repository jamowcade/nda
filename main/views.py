from django.shortcuts import render
from main.models import Campany

# Create your views here.

def index(request):
    totalCompany = Campany.objects.count()
    context = {
        'company':totalCompany
        }    
    return render(request, 'index.html',context)



