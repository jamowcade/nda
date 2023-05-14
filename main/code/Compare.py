import json
from django.shortcuts import render
from django.http import JsonResponse
from main.models import Campany, Host, ScanCase, Network
from django.utils import timezone
from datetime import datetime

# Create your views here.


def compare(request):
    name = request.GET.get('name')
    network = Network.objects.filter(compony_info= name).values('network').all()
    scan_cases = ScanCase.objects.all()
    companies = Campany.objects.all()
    context = {
        "scan_cases":scan_cases,
        "companies":companies,
        'network':network
    }
    return render(request,'pages/compare.html', context)

def get_campany_name(request):
    name = request.GET.get('name')
    network = Network.objects.filter(compony_info= name).values().all()
    data = {'network': network}

    print(network)
   
    return JsonResponse(list(network), safe=False)

def compare_by_date(request):
    compare_date = request.GET.get('FILTERED_DATE')
    network = request.GET.get('network')
    company = request.GET.get('company')
    network_id  = Network.objects.get(id=network)
    date_object = datetime.strptime(compare_date, "%Y-%m-%d").date()
    all_host = Host.objects.filter(host_date=date_object,network= network_id).all().count()
    all_network = Host.objects.filter(host_date=date_object,network= network_id).values('network').all().distinct().count()
    all_ports = Host.objects.filter(host_date=date_object,network= network_id).values('ports').all().distinct().count()
    data = {
        "all_hosts":all_host,
        "all_networks":all_network,
        "all_ports":all_ports
    }
    print(type(date_object), date_object, "Total hosts", all_host, "total networks", all_network, "allports", all_ports)
    return JsonResponse(data, safe=False)

def compare2_by_date(request):
    compare_date = request.GET.get('FILTERED_DATE')
    network = request.GET.get('network')
    company = request.GET.get('company')
    network_id  = Network.objects.get(id=network)
    date_object = datetime.strptime(compare_date, "%Y-%m-%d").date()
    all_host = Host.objects.filter(host_date=date_object,network= network_id).all().count()
    all_network = Host.objects.filter(host_date=date_object,network= network_id).values('network').all().distinct().count()
    all_ports = Host.objects.filter(host_date=date_object,network= network_id).values('ports').all().distinct().count()
    data = {
        "all_hosts":all_host,
        "all_networks":all_network,
        "all_ports":all_ports
    }
    print(type(date_object), date_object, "Total hosts", all_host, "total networks", all_network, "allports", all_ports)
    return JsonResponse(data, safe=False)

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
                "company": host.network.compony_info.owner,


            })
           
            data = {'records': filtered_hosts, "network": host.network, 'dataCompany':Listcompany}
     
        # print(filtered_hosts)
    # return JsonResponse(data)
    return render(request, 'pages/display.html',data)

