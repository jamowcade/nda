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


@login_required(login_url='login')
def filter_data(request):
    try:
        
        search = request.GET.get('search', None)
        
        search_list = []
        singleHost = []
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
        
            if host_date == filter_date:
                if search is None or search == '':
                    ports = host.ports.all()
                   
                    new_search_ports = host.ports.filter(state=search).all()
                    for result in new_search_ports:
                        search_list.append({
                                'state':result.state,
                                'port':result.port,
                                'host':host.hostname,
                                'company':host.network.compony_info.owner

                        })
                    filtered_hosts.append({
                    'company': host.network.compony_info.owner,
                    'hostname': host.hostname,
                    'status': host.status,
                    "scanDate":filter_date,
                    'hostDate': host.host_date,
                    'ports': ports,
                    'service':[port.service for port in ports],
                    "network": host.network.network,
                    "totalports": host.ports.all().count(),
                    'openPort': host.ports.filter(state='open').count(),
                    'closePort': host.ports.filter(state='closed').count(),
                    'filteredPort': host.ports.filter(state='filtered').count(),


                    })
                   
                else:
                      ports = host.ports.all()

                      if "ip" in search:
                           ip = search.split(":")

                           if ip[1] in host.hostname:
                                
                                filtered_hosts.append({
                                'hostname': host.hostname,
                                'company': host.network.compony_info.owner,
                                "scanDate":filter_date,
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
                                
                      elif "state" in search.lower():
                           
                            state = search.split(":")
                            if host.ports.filter(state=state[1]).count() > 0 :
                                get_state = host.ports.filter(state=state[1]).all()
                                filtered_hosts.append({
                                        'hostname': host.hostname,
                                        'company': host.network.compony_info.owner,
                                        "scanDate":filter_date,
                                        'status': host.status,
                                        "scanDate":filter_date,
                                        'hostDate': host.host_date,
                                        'ports': get_state,
                                        "network": host.network.network,
                                        "totalports": host.ports.all().count(),
                                        'openPort': host.ports.filter(state='open').count(),
                                        'closePort': host.ports.filter(state='closed').count(),
                                        'filteredPort': host.ports.filter(state='filtered').count(),

                                    })
                           
                      elif "port" in search.lower():
                           port = search.split(":")
                           if host.ports.filter(port=port[1]).count() > 0 :
                            get_port = host.ports.filter(port=port[1]).all()
                            filtered_hosts.append({
                                    'hostname': host.hostname,
                                    'company': host.network.compony_info.owner,
                                    "scanDate":filter_date,
                                    'status': host.status,
                                    "scanDate":filter_date,
                                    'hostDate': host.host_date,
                                    'ports': get_port,
                                    "network": host.network.network,
                                    "totalports": host.ports.all().count(),
                                    'openPort': host.ports.filter(state='open').count(),
                                    'closePort': host.ports.filter(state='closed').count(),
                                    'filteredPort': host.ports.filter(state='filtered').count(),

                                })

                     
       
        paginator = Paginator(filtered_hosts, 50)
        # print("------>>",search_list)
        pagePaginator= paginator.get_page(page)
        data = {'records': pagePaginator, "network": host.network, 'dataCompany':Listcompany, "scan_date": filter_date,"search":search}
        # print(data)
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
    
   


def scan_case_report(request):
    # try:
        scan_case_id = request.GET.get('scan_case')
        page = request.GET.get('page')
        search = request.GET.get('search', '')
        scan_case = ScanCase.objects.get(id=scan_case_id)
        print("search:", search)
        print("page:", page)
        scan_case_hosts = ""
        print("scan case:", scan_case_id)
        if search is None or search == '':
            scan_case_hosts = scan_case.hosts.all()
            hosts = paginateHosts(scan_case_hosts, page)
            total_hosts = len( scan_case_hosts)
            if total_hosts > 0:
                    data = {'hosts': hosts,"scan_case": scan_case.id, "search":search, "total_hosts":total_hosts}
                    html = render(request, 'pages/report_hosts.html',data)
                    return JsonResponse({"success":True, "message":f"data found matching {scan_case.name }", "html":str(html.content, encoding='utf8')}, safe=False)
            else:
                return JsonResponse({"success":False, "message":f"No data found matching {ip[1]}"}, safe=False)

        else:
              
              if "ip" in search and ":" in search:
                        ip = search.split(":")
                        scan_case_hosts = scan_case.hosts.filter(hostname = ip[1]).all()
                        host = paginateHosts(scan_case_hosts, page)
                        total_hosts = len(scan_case_hosts)
                        if total_hosts > 0:
                            data = {'hosts': host,"scan_case": scan_case.id, "search":search, "total_hosts":total_hosts}
                            html = render(request, 'pages/report_hosts.html',data)
                            return JsonResponse({"success":True, "message":f"data found matching  {ip[1] }", "html":str(html.content, encoding='utf8')}, safe=False)
                        else:
                            return JsonResponse({"success":False, "message":f"No data found matching ip: {ip[1]}"}, safe=False)
              elif "state" in search.lower() and ":" in search:
                        state = search.split(":")
                        ports = Port.objects.filter(state=state[1] ).all()
                        scan_case_hosts= scan_case.hosts.filter(ports__state  = state[1]).all().distinct()
                        hosts = paginateHosts(scan_case_hosts, page)
                        total_hosts = len(scan_case_hosts)
                        if total_hosts > 0:
                            data = {'hosts': hosts,"scan_case": scan_case.id, "search":search, "total_hosts":total_hosts}
                            html = render(request, 'pages/report_hosts.html',data)
                            return JsonResponse({"success":True, "message":f"data found matching  {state[1] }", "html":str(html.content, encoding='utf8')}, safe=False)
                        else:
                            return JsonResponse({"success":False, "message":f"No data found matching state: {state[1]}! stats can be,(open, closed, filtered)"}, safe=False)
              elif "port" in search.lower() and ":" in search:
                        port = search.split(":")
                        scan_case_hosts = scan_case.hosts.filter(ports__port  = port[1]).all().distinct()
                        hosts = paginateHosts(scan_case_hosts, page)
                        total_hosts = len(scan_case_hosts)
                        if total_hosts > 0:
                            data = {'hosts': hosts,"scan_case": scan_case.id, "search":search, "total_hosts":total_hosts}
                            html = render(request, 'pages/report_hosts.html',data)
                            return JsonResponse({"success":True, "message":f"data found matching  {port[1] }", "html":str(html.content, encoding='utf8')}, safe=False)
                        else:
                            return JsonResponse({"success":False, "message":f" No data found matching Port: {port[1]}! Enter valid port number"}, safe=False)
              else:
                  return JsonResponse({"invalid":False, "message":f"Ivalid search query! please use keywords (ip, state, port and separate with colon) e.g: ip:67.33.8.9, port:90, state:open"}, safe=False)

        paginator = Paginator(scan_case_hosts, 50)

        pagePaginator= paginator.get_page(page)
        total_hosts = len(scan_case_hosts)
        data = {'hosts': pagePaginator,"scan_case": scan_case.id, "search":search, "total_hosts":total_hosts}
            # print(data)
        if len(scan_case_hosts) > 0:
                return render(request, 'pages/report_hosts.html',data)
        else:
            return JsonResponse("NO Data found", safe=False)
    # except Exception as e:
    #                 ErrorLog.objects.create(
    #                 user=request.user,
    #                 message=f"An error occurred: {e}"
    #                 )
    #                 return JsonResponse({'success': False, 'error': f'and error occured'})


def paginateHosts(hosts, page):
        paginator = Paginator(hosts, 50)
        pagePaginator= paginator.get_page(page)
        return pagePaginator
        
