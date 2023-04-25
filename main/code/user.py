from django.shortcuts import render
from main.models import Campany

# Create your views here.



def login(request):
    return render(request, 'accounts/login2.html')

def register(request):
    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forget.html')

def staffs(request):
    return render(request,'accounts/staffs.html')