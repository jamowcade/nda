from django.shortcuts import render
from main.models import Campany,Network
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    totalCompany = Campany.objects.count()
    totalNetwork = Network.objects.count()
    context = {
        'company':totalCompany,
        'network':totalNetwork
        }    
    return render(request, 'index.html',context)



