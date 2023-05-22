from django.shortcuts import render
from main.models import Campany, ErrorLog, Host, Network, Port, ScanCase
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.
def scan_cases_report(request):
    scan_cases = ScanCase.objects.all()
    context = {
        "scan_cases":scan_cases
    }
    return render(request,'pages/scan_case_report.html', context)



def filter_data(request):
    try:
        filter_date = request.GET.get('filter_date')
        page = request.GET.get('page')
        hosts = Host.objects.all()
        Listcompany = Campany.objects.all()
        # print(filter_date)
        filtered_hosts = []
        data = {
            "records": []
        }
        for host in hosts:
            host_date = str(host.host_date)
            # print(host_date)

            # data_string = host_date.strftime('%Y-%m-%d')
            
            # print(type(host_date), type(filter_date))
            if host_date == filter_date:
                ports = host.ports.all()
                
                filtered_hosts.append({
                'company': host.network.compony_info.owner,
                'hostname': host.hostname,
                'status': host.status,
                "scanDate":filter_date,
                'hostDate': host.host_date,
                'ports': ports,
                "network": host.network.network,
                "totalports": host.ports.all().count(),
                'openPort': host.ports.filter(state='open').count(),
                'closePort': host.ports.filter(state='closed').count(),
                'filteredPort': host.ports.filter(state='filtered').count(),


                })
        paginator = Paginator(filtered_hosts, 50)
    
        pagePaginator= paginator.get_page(page)
        data = {'records': pagePaginator, "network": host.network, 'dataCompany':Listcompany, "scan_date": filter_date}
        if len(filtered_hosts) > 0:
            return render(request, 'pages/report_hosts.html',data)
        else:
            return JsonResponse("NO Data found", safe=False)
    except Exception as e:
                    ErrorLog.objects.create(
                    user=request.user,
                    message=f"An error occurred: {e}"
                    )
                    return JsonResponse({'success': False, 'error': f'and error occured'})
    


