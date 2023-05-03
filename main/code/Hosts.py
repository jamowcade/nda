from django.shortcuts import render, HttpResponse
import json
from main.models import Campany, Host

# Create your views here.
def host(request,id):
    
   
    hosts = Host.objects.filter(network = id).all()

    context = {
        "hosts": hosts
    }

    return render(request,'pages/host.html')

def uploadHosts(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        jsondata = json.loads(data)
        print("total host:",len(jsondata))
        print(jsondata)
        for host in jsondata:
            print(host)


    # data = json.loads('data')
    

    return HttpResponse("success! file received")