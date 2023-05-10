from django.shortcuts import render, HttpResponse
import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Campany, Host, Network, Port

# Create your views here.
def host(request,id):
    
   
    hosts = Host.objects.filter(network = id).all()

    context = {
        "hosts": hosts,
        "network_id":id
    }

    return render(request,'pages/host.html', context)

# def uploadHosts(request):
#     if request.method == 'POST':
#         data = request.POST.get('data')
#         jsondata = json.loads(data)
#         print("total host:",len(jsondata))
#         print(jsondata)
#         for host in jsondata:
#             print(host)


#     # data = json.loads('data')
    

#     return HttpResponse("success! file received")


@csrf_exempt
def addHosts(request):
    if request.method == 'POST':
        file_data = request.FILES['file'].read().decode('utf-8') # read the uploaded file data
        get_date = request.POST.get('scan_date')

        date_obj = datetime.strptime(get_date, "%B %d, %Y")
        scan_date = date_obj.strftime("%Y-%m-%d")

        data = json.loads(file_data) # parse the JSON data
        file_network = data[0]['network'] #get the network in json file
        # check if network not registed before uploading hosts
        try:
            host_network = Network.objects.get(network=file_network) 
        except Network.DoesNotExist:
            return JsonResponse({'success': False, 'error': f'network {file_network} is not registered now!'})
        
        # retrieve data from json file and save to model
        for host in range(len(data)-1):
            hostname = data[host]['ip']
            status =   data[host]['state']
            network = host_network
            
            is_host = Host.objects.filter(hostname=hostname, host_date=scan_date).all() # check if host exists with the given hostname and scan date.
            
            # check if host already registered in the current scan case
            if is_host:
                return JsonResponse({'success': False, 'error': 
                f'This file already uploaded for network - ({file_network}) at {scan_date}. Please upload another file'})
                continue
            else:
                new_host = Host(hostname=hostname, status = status, network=network, host_date=scan_date)
                new_host.save()
                for port in range(len(data[host]['ports'])):
                    portid= data[host]['ports'][port]['portid']
                    protocol = data[host]['ports'][port]['protocol']
                    state = data[host]['ports'][port]['state']
                    service_name =  data[host]['ports'][port]['service']['name']
                    service_method =  data[host]['ports'][port]['service']['method']
                    service_conf =  data[host]['ports'][port]['service']['conf']
                    service = f"name: {service_name} method: {service_method} conf: {service_conf}"
                    # for service in range(1):
                    #     service_name
                    reason = data[host]['ports'][port]['state']
                    port = Port(port=portid, state = state, protocol=protocol, host=new_host, service=service, reason=reason)
                    port.save()
                    print(portid, "saved now")
            
        return JsonResponse({'success': True, "message": f"All hosts Uploaded to network {network.compony_info.owner} - {file_network}", })
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})