from django.shortcuts import render
from main.models import Campany

# Create your views here.

def index(request):
    totalCompany = Campany.objects.count()
    context = {
        'company':totalCompany
        }
    
    return render(request, 'index.html',context)

def login(request):
    return render(request, 'accounts/login2.html')

def register(request):
    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forget.html')