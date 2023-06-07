from main.models import Campany, Host, Network, Port, ScanCase
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from django.utils import timezone

@login_required(login_url='login')
@permission_required('main.view_scancase', raise_exception=False, login_url='login')
def scan_case(request):

    if request.method == 'POST':
        date = request.POST.get('date')
        name = f"scan case- {date}"
        is_exist = ScanCase.objects.filter(scan_date = date)
        date_is_less = compare_date(date)
        last_entry_date = ScanCase.objects.last().scan_date
        if date_is_less:
            return JsonResponse ({'success': False,"message":f"Scan case Date cannot be less than {last_entry_date} "})
        if is_exist:
            return JsonResponse ({'success': False,"message":"Scan case already Created"})
        scan_case = ScanCase(name=name, scan_date=date, description=name)
        scan_case.save()
        return JsonResponse ({'success': True,"message":"data saved"})
        print(name, date, description)

        
    else:
        scan_cases = ScanCase.objects.all()
   
        context = {
        "scan_cases":scan_cases,
        
        }
  
        return render(request, 'pages/scan_case.html', context)
    





@login_required(login_url='login')
def view_scan_case(request,scan_id):
    # try:
        # scan_id = request.GET.get('scan_case')
        page = request.GET.get('page')
        search = request.GET.get('search', '')
        page_number = request.GET.get('page_number',10)
        scan_case = ScanCase.objects.get(id=scan_id)
        print("search:", search)
        print("page:", page)
        print("number per page", page_number)
        print("scan case id:",scan_id)
        scan_case_hosts = ""
        print("scan case:", scan_id)
        if search is None or search == '':
            scan_case_hosts = scan_case.hosts.all()
            hosts = paginateHosts(scan_case_hosts, page,page_number)
            total_hosts = len( scan_case_hosts)
            returned_hosts = len(hosts)
            # if total_hosts > 0:
            data = {'hosts': hosts,"scan_case": scan_case.id, 'scan_date':scan_case.scan_date, "search":search, "returned_hosts":returned_hosts, "current_page":page, "page_number":page_number, "total_hosts":total_hosts}
            html = render(request, 'pages/scan_case_detail.html',data)
            return html
            # else:
                # data = {'hosts': hosts,"scan_case": scan_case.id, "search":search, "returned_hosts":returned_hosts, "current_page":page, "page_number":page_number, "total_hosts":total_hosts}
                # html = render(request, 'pages/report_hosts.html',data)
                # print('No Data')
                # return JsonResponse({"success":False, "message":f"No data found matching {scan_case.name}", "html":str(html.content, encoding='utf8')}, safe=False)
        else:
              
              if "ip" in search and ":" in search:
                        ip = search.split(":")
                        scan_case_hosts = scan_case.hosts.filter(hostname = ip[1]).all()
                        hosts = paginateHosts(scan_case_hosts, page, page_number)
                        total_hosts = len(scan_case_hosts)
                        returned_hosts = len(hosts)
                        if total_hosts > 0:
                            data = {'hosts': hosts,"scan_case": scan_case.id, "search":search, "returned_hosts":returned_hosts, "current_page":page, "page_number":page_number, "total_hosts":total_hosts}
                            # html = render(request, 'pages/report_hosts.html',data)
                            html = render(request, 'pages/scan_case_detail.html',data)
                            return JsonResponse({"success":True, "message":f"data found matching  {ip[1] }", "html":str(html.content, encoding='utf8')}, safe=False)
                            # return html
                        else:
                            return JsonResponse({"success":False, "message":f"No data found matching ip: {ip[1]}"}, safe=False)
              elif "state" in search.lower() and ":" in search:
                        state = search.split(":")
                        ports = Port.objects.filter(state=state[1] ).all()
                        scan_case_hosts= scan_case.hosts.filter(ports__state  = state[1]).all().distinct()
                        hosts = paginateHosts(scan_case_hosts, page, page_number)
                        total_hosts = len(scan_case_hosts)
                        returned_hosts = len(hosts)
                        if total_hosts > 0:
                            data = {'hosts': hosts,"scan_case": scan_case.id, "search":search, "returned_hosts":returned_hosts, "current_page":page, "page_number":page_number, "total_hosts":total_hosts}
                            # html = render(request, 'pages/report_hosts.html',data)
                            html = render(request, 'pages/scan_case_detail.html',data)
                            return JsonResponse({"success":True, "message":f"data found matching  {state[1] }", "html":str(html.content, encoding='utf8')}, safe=False)
                            # return html
                        else:
                            return JsonResponse({"success":False, "message":f"No data found matching state: {state[1]}! stats can be,(open, closed, filtered)"}, safe=False)
              elif "service" in search.lower() and ":" in search:
                        services = search.split(":")
                        get_ser = Port.objects.filter(Q(services__key__icontains=services[1]) | Q(services__value__icontains=services[1]))
                        scan_case_hosts = scan_case.hosts.filter(ports__in =get_ser).all().distinct()
                        hosts = paginateHosts(scan_case_hosts, page, page_number)
                        total_hosts = len(scan_case_hosts)
                        returned_hosts = len(hosts)
                        if total_hosts > 0:
                            data = {'hosts': hosts,"scan_case": scan_case.id, "search":search, "returned_hosts":returned_hosts, "current_page":page, "page_number":page_number, "total_hosts":total_hosts}
                            html = render(request, 'pages/scan_case_detail.html',data)
                            return JsonResponse({"success":True, "message":f"data found matching  {services[1] }", "html":str(html.content, encoding='utf8')}, safe=False)
                        else:
                            return JsonResponse({"success":False, "message":f"No data found matching Services: {services[1]}!"}, safe=False)
                        print(scan_case_hosts)
                        # for host in scan_case.hosts.all():
                        #       for port in host.ports.all():
                        #             for service in port.services.filter(key=services[1]).all():
                        #                   print(service.key,service.value,host.hostname,host.network.network,port.port)
              elif "port" in search.lower() and ":" in search:
                        port = search.split(":")
                        scan_case_hosts = scan_case.hosts.filter(ports__port  = port[1]).all().distinct()
                        hosts = paginateHosts(scan_case_hosts, page, page_number)
                        total_hosts = len(scan_case_hosts)
                        returned_hosts = len(hosts)
                        if total_hosts > 0:
                            data = {'hosts': hosts,"scan_case": scan_case.id, "search":search, "returned_hosts":returned_hosts, "current_page":page, "page_number":page_number, "total_hosts":total_hosts}
                            # html = render(request, 'pages/report_hosts.html',data)
                            html = render(request, 'pages/scan_case_detail.html',data)
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




def paginateHosts(hosts, page, page_number):
        paginator = Paginator(hosts, page_number)
        pagePaginator= paginator.get_page(page)
        return pagePaginator
        
def compare_date(date):
    given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    last_entry_date = ScanCase.objects.last().scan_date

    return given_date < last_entry_date



def delete_scan_case(request,scan_case_id):
    # Retrieve the scan case instance
   
    scan_case = ScanCase.objects.get(id=scan_case_id)
        # Delete all hosts related to the scan case and their related ports
    for host in Host.objects.filter(scan_case=scan_case):
        Port.objects.filter(host=host).delete()
    Host.objects.filter(scan_case=scan_case).delete()
    return JsonResponse({'message': 'Scan case and related hosts and ports have been deleted.'})
    return render('pages/scan_case.html')
