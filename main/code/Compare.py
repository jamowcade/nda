import json
from django.shortcuts import render
from django.http import JsonResponse
from main.models import Campany, Host, ScanCase
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@permission_required('main.compare_scancase', raise_exception=True, login_url=None)
def compare(request):
    scan_cases = ScanCase.objects.all()
    companies = Campany.objects.all()
    context = {
        "scan_cases":scan_cases,
        "companies":companies
    }
    return render(request,'pages/compare.html', context)
@permission_required('main.compare_scancase', raise_exception=True, login_url=None)
def compare_by_date(request):
    compare_date = request.GET.get('FILTERED_DATE')
    hosts = Host.objects.all()
    Listcompany = Campany.objects.all()
    filtered_hosts = []
    for host in hosts:
        host_date = str(host.host_date)
        if host_date == compare_date:
            ports = host.ports.all()
            
            filtered_hosts.append({
                "host":host.hostname,
                "ports": ports,
                "totalports": host.ports.all().count(),
                "network": host.network.network,
                "company": host.network.compony_info.owner,


            })
    data = {'records': filtered_hosts, "network": host.network, 'dataCompany':Listcompany}
    

    print("hello world")

    return render(request, 'pages/display.html',data)
@permission_required('main.compare_scancase', raise_exception=True, login_url=None)
def filter_by_date(request):
    filter_date = request.GET.get('filter_date')
    hosts = Host.objects.all()
    Listcompany = Campany.objects.all()

    filtered_hosts = []
    data = {
        "records": []
    }
    for host in hosts:
        host_date = str(host.host_date)
     
        # data_string = host_date.strftime('%Y-%m-%d')
        
        # print(type(host_date), type(filter_date))
        if host_date == filter_date:
            ports = host.ports.all()
            
            filtered_hosts.append({
                "host":host.hostname,
                "ports": ports,
                "totalports": host.ports.all().count(),
                "network": host.network.network,
                "company": host.network.compony_info.owner


            })
          
            data = {'records': filtered_hosts, "network": host.network, 'dataCompany':Listcompany}
     
        # print(filtered_hosts)
    # return JsonResponse(data)
    return render(request, 'pages/display.html',data)

