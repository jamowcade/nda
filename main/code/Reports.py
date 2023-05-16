from django.shortcuts import render
from main.models import Campany, Host, Network, Port, ScanCase
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def Reports(request):

    return render(request,'pages/Reports.html')


@permission_required('main.view_report', raise_exception=True, login_url=None)
def scan_cases_report(request):
    scan_cases = ScanCase.objects.all()
    context = {
        "scan_cases":scan_cases
    }
    return render(request,'pages/scan_case_report.html', context)

@permission_required('main.view_report', raise_exception=True, login_url=None)
def filter_by_date(request):
    filter_date = request.GET.get('filter_date')
    hosts = Host.objects.all()
    Listcompany = Campany.objects.all()
    # print(filter_date)
    filtered_hosts = []
    data = {
        "records": []
    }
    for host in hosts:
        host_date = host.host_date
        # print(host_date)

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
     
    return render(request, 'pages/display.html',data)
