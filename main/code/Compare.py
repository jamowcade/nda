import json
from django.shortcuts import render
from django.http import JsonResponse
from main.models import Campany, Host, ScanCase, Network,Port
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required

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
<<<<<<< HEAD
@permission_required('main.compare_scancase', raise_exception=True, login_url=None)
=======

def get_campany_name(request):
    name = request.GET.get('name')
    network = Network.objects.filter(compony_info= name).values().all()
    data = {'network': network}
    return JsonResponse(list(network), safe=False)

>>>>>>> 75cdd065af5f79a8a20cb2db6ae045f6366f3b90
def compare_by_date(request):
    compare_date = request.GET.get('FILTERED_DATE')
    compare_date2 = request.GET.get('FILTERED_DATE2')

    if compare_date is not None : 
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
        global all_host1 
        all_host1 = Host.objects.filter(host_date=date_object,network= network_id).all()
        return JsonResponse(data, safe=False)
    else:
  
        network = request.GET.get('network')   
        company = request.GET.get('company')
        network_id  = Network.objects.get(id=network)
        date_object = datetime.strptime(compare_date2, "%Y-%m-%d").date()
        all_host = Host.objects.filter(host_date=date_object,network= network_id).all().count()
        all_network = Host.objects.filter(host_date=date_object,network= network_id).values('network').all().distinct().count()
        all_ports = Host.objects.filter(host_date=date_object,network= network_id).values('ports').all().distinct().count()
        global all_host2 
        all_host2 = Host.objects.filter(host_date=date_object,network= network_id).all()

        all_h2 =[]
        all_h1 =[]
        
        for all_hst2 in all_host2:
            all_h2.append(all_hst2.hostname)
        for all_hst1 in all_host1:
            all_h1.append(all_hst1.hostname)
        # dff = set(all_host1) - set(all_host2)

        print(f"host 2 ==> {all_h2}\n")
        print(f"host 1 ==> {all_h1}\n")


        dff = set(all_h1) - set(all_h2)
        dff1 = set(all_h2) - set(all_h1)
        all_dff = dff.union(dff1)
        print(f"\n\ndifference host ==> {all_dff}\n")
            
        data = {
            "all_hosts2":all_host,
            "all_networks2":all_network,
            "all_ports2":all_ports,
            "dff":list(all_dff),
        }
        return render(request, 'pages/show_cmpr.html',data)
    
    

<<<<<<< HEAD
    print("hello world")

    return render(request, 'pages/display.html',data)
@permission_required('main.compare_scancase', raise_exception=True, login_url=None)
=======
>>>>>>> 75cdd065af5f79a8a20cb2db6ae045f6366f3b90
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
<<<<<<< HEAD
                "company": host.network.compony_info.owner


            })
          
=======
                "company": host.network.compony_info.owner,
            })
           
>>>>>>> 75cdd065af5f79a8a20cb2db6ae045f6366f3b90
            data = {'records': filtered_hosts, "network": host.network, 'dataCompany':Listcompany}
     
        # print(filtered_hosts)
    # return JsonResponse(data)
    return render(request, 'pages/display.html',data)



def get_Hosts(request):
    host = request.GET.get('host')
    get_host_id = Host.objects.filter(hostname=host).all()
    for id in get_host_id:
        host_id = id.id
        ports = Port.objects.filter(host=host_id).all()

        data = {'ports': list(ports.values())}
        
        # return render(request, 'pages/show_port_Reuslt.html',data)
        return JsonResponse(data)

