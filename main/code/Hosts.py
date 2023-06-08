import traceback,json
from django.shortcuts import render, HttpResponse
from user_agents import parse
from datetime import datetime
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from main.models import Campany, ErrorLog, Host, Network, Port, UserLog, ScanCase,Service
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
@login_required(login_url='login')
@permission_required('main.view_host', raise_exception=True,login_url='login')
def host(request,id):
    device_info = hanldeLog(request)
    try:
        network = Network.objects.get(id=id)
        hosts = Host.objects.filter(network = id).all()
        context = {
            "hosts": hosts,
            "network_id":id
        }
        msg=f"You Visited Host Detail of Network {network}"
        UserLog.objects.create(
                        user=request.user,device=device_info,
                        message=msg,
                         )

        return render(request,'pages/host.html', context)
    except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
                # return info

@login_required(login_url='login')
@permission_required('main.view_host', raise_exception=True, login_url=None)
def all_host(request,page):
    device_info = hanldeLog(request)
    try:
        hosts = Host.objects.all()
        paginator = Paginator(hosts, 50)
        pagePaginator= paginator.get_page(page)

        context = {
            "hosts": pagePaginator,
        }
        msg=f"You Visited All Hosts Page"
        UserLog.objects.create(user=request.user,device=device_info,message=msg)
        return render(request,'pages/all_host.html', context)
    except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

@login_required(login_url='login')
def search(request):
    id = request.GET.get('id')
    port = Port.objects.get(id=id)

    data = {"port_service": port.service}
    return JsonResponse(data)
    


    
@csrf_exempt
@login_required(login_url='login')
@permission_required('main.add_host', raise_exception=True,login_url='login')
def addHosts(request):
    device_info = hanldeLog(request)
    try:
        serviceList = []
        if request.method == 'POST':
            file_data = request.FILES['file'].read().decode('utf-8') # read the uploaded file data
            scan_case_id = request.POST.get('scan_case')
            scan_case = ScanCase.objects.get(id=scan_case_id)
            # date_obj = datetime.strptime(get_date, "%B %d, %Y")
            # scan_date = date_obj.strftime("%Y-%m-%d")
            data = json.loads(file_data) # parse the JSON data
            # check if network not registed before uploading hosts
            #check if the is empty
            if 'network' not in data[0]:
                print("fle is ")
                return JsonResponse({'success': False, 'error': " Empty File Not Uploaded !"})
            file_network = data[0]['network'] #get the network in json file
            try:
                host_network = Network.objects.get(network=file_network) 
            except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
                return JsonResponse({'success': False, 'error': f'network {file_network} is not registered now!'})
            # retrieve data from json file and save to model
            for host in range(len(data)-1):
                hostname = data[host]['ip']
                status =   data[host]['state']
                network = host_network
                is_host = Host.objects.filter(hostname=hostname, scan_case_id=scan_case_id, network=network).all() # check if host exists with the given hostname and scan date.
                # check if host already registered in the current scan case
                if is_host:
                    info = f'sorry! this file already uploaded for network - ({file_network}) at {scan_case.name}. Please upload another file or change'
                    msg = 'Duplicate File Not Allowed! Please upload New File'
                    ErrorLog.objects.create(user=request.user,device=device_info, message=msg,info=info)
                    return JsonResponse({'success': False, 'error':info})
                    continue
                else:
                    new_host = Host(hostname=hostname, status = status, network=network, host_date=scan_case.scan_date, scan_case=scan_case)
                    new_host.save()
                    for port in range(len(data[host]['ports'])):
                        all_services =  data[host]['ports'][port]['service']
                        # print(all_services)
                        portid= data[host]['ports'][port]['portid']
                        protocol = data[host]['ports'][port]['protocol']
                        state = data[host]['ports'][port]['state']
                        reason = data[host]['ports'][port]['reason']
                        new_port = Port(port=portid, state = state, protocol=protocol, host=new_host, reason=reason)
                        new_port.save()
                        for key,value in all_services.items():
                             new_key = key
                             new_value = value
                             service = Service(key=new_key, value=new_value, port=new_port)
                             service.save()
            UserLog.objects.create(
                    user=request.user,device=device_info,
                    message = f'You Successfuly  uploaded ({file_network}) file for scan case ({scan_case.scan_date})'
                    )
            return JsonResponse({'success': True, "message": f"All hosts Uploaded to network {network.compony_info.owner} - {file_network}", })
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})
    except Exception as e:
                   info = traceback.format_exc()   
                   ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
                   return JsonResponse({'success': False, 'error': f'Erro Uploading the file {e}'})
    

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
 