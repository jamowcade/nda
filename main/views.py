from django.shortcuts import render
from main.models import Campany

# Create your views here.

def index(request):
    totalCompany = Campany.objects.count()
    context = {
        'company':totalCompany
        }
    
    return render(request, 'index.html',context)





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




