from django.shortcuts import render
from django.http import JsonResponse
from main.models import Campany, Host
from django.utils import timezone
from datetime import datetime

# Create your views here.


def compare(request):
    return render(request,'pages/compare.html')


def filter_by_date(request):
    filter_date = request.GET.get('filter_date')
    hosts = Host.objects.all()
    print(filter_date)
    filtered_hosts = []
    data = {
        "records": []
    }
    for host in hosts:
        host_date = str(host.get_date())
        # print(type(host_date), type(filter_date))
        if host_date == filter_date:
            ports = host.ports.all()
            print(ports.portid)
            filtered_hosts.append({
                "host":host.hostname,
                "ports": [{
                    "portid":[p.port for p in ports]
                }],
                "network": host.network.network,
                "company": host.network.compony_info.owner,


            })
           
            data = {'records': filtered_hosts}
        
        # print(filtered_hosts)
    return JsonResponse(data)

