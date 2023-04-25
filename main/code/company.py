from django.shortcuts import render
from main.models import Campany

# Create your views here.

def company(request):   
    listCompany = Campany.objects.all()
    context = {'company': listCompany}
    
    return render(request,'pages/company.html',context)