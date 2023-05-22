import traceback
from django.shortcuts import render, HttpResponse
import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Campany, ErrorLog, Host, Network, Port, UserLog, ScanCase
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
@login_required(login_url='login')
@permission_required('main.view_host', raise_exception=True, login_url=None)
def host(request,id):
    hosts = Host.objects.filter(network = id).all()

    context = {
        "hosts": hosts,
        "network_id":id
    }

    return render(request,'pages/host.html', context)

@login_required(login_url='login')
def search(request):
    id = request.GET.get('id')
    port = Port.objects.get(id=id)

    data = {"port_service": port.service}
    return JsonResponse(data)
    


    
@csrf_exempt
@login_required(login_url='login')
@permission_required('main.add_host', raise_exception=True, login_url=None)
def addHosts(request):
    try:
        if request.method == 'POST':
            file_data = request.FILES['file'].read().decode('utf-8') # read the uploaded file data
            get_date = request.POST.get('scan_date')
            
            print(get_date)

            date_obj = datetime.strptime(get_date, "%B %d, %Y")
            scan_date = date_obj.strftime("%Y-%m-%d")
            scan_case = ScanCase.objects.get(scan_date=scan_date)

            data = json.loads(file_data) # parse the JSON data
            file_network = data[0]['network'] #get the network in json file
            # check if network not registed before uploading hosts
            try:
                host_network = Network.objects.get(network=file_network) 
            except Exception as e:
                    ErrorLog.objects.create(
                    user=request.user,
                    message=f"An error occurred: f'network {file_network} is not registered now!'"
                    )
                    return JsonResponse({'success': False, 'error': f'network {file_network} is not registered now!'})
            
            # retrieve data from json file and save to model
            for host in range(len(data)-1):
                hostname = data[host]['ip']
                status =   data[host]['state']
                network = host_network
                
                is_host = Host.objects.filter(hostname=hostname, host_date=scan_date).all() # check if host exists with the given hostname and scan date.
                
                # check if host already registered in the current scan case
                if is_host:
                    ErrorLog.objects.create(
                    user=request.user,
                    message=f'This file already uploaded for network - ({file_network}) at {scan_date}. Please upload another file'
                    )
                    return JsonResponse({'success': False, 'error': 
                    f'sorry! this file already uploaded for network - ({file_network}) at {scan_date}. Please upload another file or change'})
                    continue
                else:
                    new_host = Host(hostname=hostname, status = status, network=network, host_date=scan_date)
                   
                    for port in range(len(data[host]['ports'])):
                        all_services =  data[host]['ports'][port]['service']
                        print(all_services)
                        portid= data[host]['ports'][port]['portid']
                        protocol = data[host]['ports'][port]['protocol']
                        state = data[host]['ports'][port]['state']

                        try:
                            for key,value in data[host]['ports'][port]['service'].items():
                                print(key,value)

                        except:
                            return JsonResponse("error getttin services", safe=False)
                        service = all_services
                        # for service in range(1):
                        #     service_name
                        reason = data[host]['ports'][port]['state']
                        port = Port(port=portid, state = state, protocol=protocol, host=new_host, service=service, reason=reason)
                        new_host.save()
                        port.save()
                 
         
            return JsonResponse({'success': True, "message": f"All hosts Uploaded to network {network.compony_info.owner} - {file_network}", })
            UserLog.objects.create(
                    user=request.user,
                    message = f'{request.user} uploaded ({file_network}) file for scan case ({scan_date})'
                    )
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})
  
    except Exception as e:
                    tb = traceback.format_exc()
                    message = f"An error occurred: while uploading file {e}"
                    ErrorLog.objects.create(
                    user=request.user,
                    message= message
                    )
                    return JsonResponse({'success': False, 'error': f'Erro Uploading the file {e}'})