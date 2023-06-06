from django.shortcuts import render
from main.models import Port, Host
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url='login')
@permission_required('main.view_port', login_url='login', raise_exception=False)
def ports(request):
    host_id = request.GET.get('host_id')
    
    ports = Port.objects.filter(host=host_id).all()

    host_ports = []
    for port in ports:
        host_ports.append({
            "port": port.port,
            "protocol":port.protocol,
            "state": port.state,
            "service": port.service
        })
  
    
    return JsonResponse(host_ports, safe=False)