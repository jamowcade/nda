import traceback
from user_agents import parse
from main.models import Campany, Host, Network, Port, ScanCase,UserLog,ErrorLog
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

import datetime
from django.utils import timezone

@login_required(login_url='login')
@permission_required('main.view_scancase', raise_exception=False, login_url='login')
def scan_case(request):
    device_info=hanldeLog(request)
    try:

        if request.method == 'POST':
            date = request.POST.get('date')
            name = f"scan case- {date}"
            is_exist = ScanCase.objects.filter(scan_date = date)
            # date_is_less = compare_date(date)
            # last_entry_date = ScanCase.objects.last().scan_date
            # if date_is_less:
            #     return JsonResponse ({'success': False,"message":f"Scan case Date cannot be less than {last_entry_date} "})
            if is_exist:
                return JsonResponse ({'success': False,"message":"Scan case already Created"})
            else:
                scan_case = ScanCase(name=name, scan_date=date, description=name)
                scan_case.save()
                msg=f"You Successfuly Created New Scan Date ({date}) for ({name}))"
                UserLog.objects.create(
                            user=request.user,device=device_info,
                            message=msg,
                            )
                return JsonResponse ({'success': True,"message":msg})

            
        else:
            scan_cases = ScanCase.objects.all()
    
            context = {
            "scan_cases":scan_cases,
            
            }
            msg=f"You Successfuly Visited Scan Case Page"
            UserLog.objects.create(
                        user=request.user,device=device_info,
                        message=msg,
                         )
    
            return render(request, 'pages/scan_case.html', context)
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
        
    





@login_required(login_url='login')
def view_scan_case(request,scan_id):
    # try:
        # scan_id = request.GET.get('scan_case')
        page = request.GET.get('page')
        search = request.GET.get('search', '')
        page_number = request.GET.get('page_number',10)
        scan_case = ScanCase.objects.get(id=scan_id)
       
        scan_case_hosts = ""
        
        if search is None or search == '':
            scan_case_hosts = scan_case.hosts.all()
            hosts = paginateHosts(scan_case_hosts, page,page_number)
            total_hosts = len( scan_case_hosts)
            returned_hosts = len(hosts)
            # if total_hosts > 0:
            data = {'hosts': hosts,"scan_case": scan_case.id, 'scan_date':scan_case.scan_date, "search":search, "returned_hosts":returned_hosts, "current_page":page, "page_number":page_number, "total_hosts":total_hosts}
            html = render(request, 'pages/scan_case_detail.html',data)
            return html
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

      

def paginateHosts(hosts, page, page_number):
        paginator = Paginator(hosts, page_number)
        pagePaginator= paginator.get_page(page)
        return pagePaginator
        
def compare_date(date):
    given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    last_entry_date = ScanCase.objects.last().scan_date
    if last_entry_date is None:
        return given_date
    else:
        return given_date < last_entry_date

@login_required(login_url='login')
def delete_scan_case(request,scan_case_id):
    device_info = hanldeLog(request)
    try:
        if request.method == "POST":
            scan_case = get_object_or_404(ScanCase, id=scan_case_id)
            ischecked = request.POST.get('isChecked')
            # print('delte scan case:', ischecked)
            hosts = Host.objects.filter(scan_case=scan_case)
            total_hosts = hosts.count()
            if total_hosts > 0:
                for host in hosts:
                    Port.objects.filter(host=host).delete()
                hosts.delete()
                if ischecked:
                     scan_case.delete()

                     msg=f"You Successfully Deleted {scan_case.name}'s With it's Date {scan_case.scan_date}"
                     UserLog.objects.create(
                            user=request.user,device=device_info,
                            message=msg,
                            )

                     return JsonResponse({'message': f'{total_hosts} hosts and their ports related to {scan_case.name}  have been deleted.'})
                else:
                    msg=f"You Successfully Deleted {scan_case.name}'s Data"
                    UserLog.objects.create(
                            user=request.user,device=device_info,
                            message=msg,
                            )

                    return JsonResponse({'message': f'{total_hosts} hosts and their ports related to {scan_case.name}  have been deleted.'})
            else:
                if ischecked:
                    scan_case.delete()
                return JsonResponse({'message': f'No Data for {scan_case.name}'})

        scan_case = ScanCase.objects.get(id=scan_case_id)
        context = {
            "scan_case":scan_case
        }
        msg=f"You Tried to delete {scan_case.name}"
        UserLog.objects.create(
                        user=request.user,device=device_info,
                        message=msg,
                         )
        return render(request,'pages/delete_scan_case.html', context)
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)


def hanldeLog(request):
    user_agent_string = request.META.get('HTTP_USER_AGENT')
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = parse(user_agent_string)
    try:
        device_info = f"{ip_address} / {user_agent}"
        return device_info
    except Exception as e:
        device_info = f"{ip_address} / {user_agent}"
        info = traceback.format_exc()        
        ErrorLog.objects.create(user="AnonymousUser",device=device_info, message=str(e), info=info)