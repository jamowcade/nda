from django.shortcuts import render
from main.models import Campany

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'accounts/login2.html')

def register(request):
    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forgot.html')


def staffs(request):
    return render(request,'accounts/staffs.html')


def company(request):   
    listCompany = Campany.objects.all()
    counts = Campany.objects.count()
    context = {'company': listCompany}
    print(counts)  
    return render(request,'pages/company.html',context)


def network(request):

    return render(request,'pages/network.html')

def host(request):

    return render(request,'pages/host.html')




def ports(request):
    return render(request,'pages/port.html')

def compare(request):
    return render(request,'pages/compare.html')



def scan_case(request):
    return render(request,'pages/scan_case.html')


def Reports2(request):
    return render(request,'pages/Reports2.html')




