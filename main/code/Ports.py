from django.shortcuts import render
from main.models import Port, Host
from django.http import JsonResponse

# Create your views here.

def ports(request):
    host_id = request.GET.get('host_id')
    
    ports = Port.objects.filter(host=host_id).all()

    host_ports = []
    for port in ports:
        host_ports.append({
            "port": port.port,
            "protocol":port.protocol,
            "state": port.state
        })
  
    print(host_ports)
    return JsonResponse(host_ports, safe=False)