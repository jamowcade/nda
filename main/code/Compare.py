import json
from django.shortcuts import render
from django.http import JsonResponse
from main.models import Campany, Host, ScanCase, Network,Port
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
# Create your views here.


@permission_required('main.compare_scancase', raise_exception=True, login_url=None)
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

@login_required(login_url='login')
def get_campany_name(request):
    name = request.GET.get('name')
    network = Network.objects.filter(compony_info= name).values().all()
    data = {'network': network}
    return JsonResponse(list(network), safe=False)

@login_required(login_url='login')
def compare_by_date(request):
    compare_date = request.GET.get('FILTERED_DATE')
    compare_date1 = request.GET.get('FILTERED_DATE1')
    compare_date2 = request.GET.get('FILTERED_DATE2')
   
    compare_network = request.GET.get('network')


    scan_date_1 = datetime.strptime(compare_date1, "%Y-%m-%d").date()
    scan_date_2 = datetime.strptime(compare_date2, "%Y-%m-%d").date()

    network = request.GET.get('network')   
    company = request.GET.get('company')

    network_id  = Network.objects.get(id=network)
    date_object = datetime.strptime(compare_date1, "%Y-%m-%d").date()
    date_object2 = datetime.strptime(compare_date2, "%Y-%m-%d").date()
   
    all_host1 = Host.objects.filter(host_date=date_object,network= network_id).all()
    all_host2 = Host.objects.filter(host_date=date_object2,network= network_id).all()

    all_h2 =[]
    all_h1 =[]
    
    for all_hst1 in all_host1:
        all_h1.append(all_hst1.hostname)
    for all_hst2 in all_host2:
        all_h2.append(all_hst2.hostname)


    dff = set(all_h1) - set(all_h2)
    dff1 = set(all_h2) - set(all_h1)

    if len(dff) != 0:
       
        a =  getALl(dff)

        paginator = Paginator(a, 10)
        page_number = request.GET.get('page')
        pagePaginator= paginator.get_page(page_number)
        
        data = {
            'records':pagePaginator,
            'scan_date1':scan_date_1,
            'scan_date2':scan_date_2,
            'network':compare_network,
        }
    
        return render(request,'pages/show_cmpr.html',data)
    
    else:
       
        
        a =  getALl(dff1)

        paginator = Paginator(a, 10)
        page_number = request.GET.get('page')
        pagePaginator= paginator.get_page(page_number)        
        data = {
            'records':pagePaginator,
            'scan_date1':scan_date_1,
            'scan_date2':scan_date_2,
            'network':compare_network,
        }
    return render(request,'pages/show_cmpr.html',data)

    
@login_required(login_url='login')
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
     
        if host_date == filter_date:
            ports = host.ports.all()
            
            filtered_hosts.append({
                "host":host.hostname,
                "ports": ports,
                "totalports": host.ports.all().count(),
                "network": host.network.network,
                "company": host.network.compony_info.owner,
            })
           
            data = {'records': filtered_hosts, "network": host.network, 'dataCompany':Listcompany,}

    return JsonResponse(data)



def get_Hosts(request):
    host = request.GET.get('host')
    get_host_id = Host.objects.filter(hostname=host).all()
    for id in get_host_id:
        host_id = id.id
        ports = Port.objects.filter(host=host_id).all()

        data = {'ports': list(ports.values())}
        
       
        return JsonResponse(data)

def getALl(all_dff):
    port_with_host = []
    for host in all_dff:
       get_host_id = Host.objects.filter(hostname=host).all()
       for host_id in get_host_id:
        # print(f"id {host_id.id} Hostname = {host_id.hostname}")
        ports = host_id.ports.all()
           # print(f"port {port.host.id} Port = {port.port} State {port.state} Procol {port.protocol}\n")
        port_with_host.append({
            'host_id':host_id.id,
            'hostname': host_id.hostname,
            'port': ports,
            'company': host_id.network.compony_info.owner,
          
            'status': host_id.status,
            'hostDate': host_id.host_date,
            
           "network": host_id.network.network,
            "totalports": host_id.ports.all().count(),
            'openPort': host_id.ports.filter(state='open').count(),
            'closePort': host_id.ports.filter(state='closed').count(),
            'filteredPort': host_id.ports.filter(state='filtered').count(),
            
        })
        # print(host_id.host_date, host_id.scan_case.id)
    return port_with_host
       
        # for port in host_port_id:
        #     print(port.id)

    # return all_dff
@login_required(login_url='login')
@csrf_exempt
def showdetaile(request):
    id = request.POST.get('id')
    print(id)
    port = Port.objects.filter(host=id).all()
   
    # print(" =====> ",port)
    dataport ={"port": list(port.values())}
    return JsonResponse(dataport)