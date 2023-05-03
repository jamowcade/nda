from django.shortcuts import render, HttpResponse
import json
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
        data = json.loads(file_data) # parse the JSON data
        # create a new object of MyModel and save it to the database
        "41.78.72.0-24/24"
        
        network = data[0]['network']
        
        # network_id = request.POST['network_id']
        host_network = Network.objects.get(network=network)
        print(host_network.network, host_network.state)
       
        # service =  data[0]['ports'][0]['service']['name']

        # print(service)
        for host in range(len(data)-1):
            hostname = data[host]['ip']
            status =   data[host]['state']
            network = host_network
            new_host = Host(hostname=hostname, status = status, network=network)
            new_host.save()
            for port in range(len(data[host]['ports'])):
                portid= data[host]['ports'][port]['portid']
                protocol = data[host]['ports'][port]['protocol']
                state = data[host]['ports'][port]['state']
                service =  data[host]['ports'][port]['service']
                # for service in range(1):
                #     service_name
                reason = data[host]['ports'][port]['state']
                port = Port(port=portid, state = state, protocol=protocol, host=new_host)
                port.save()
                print(portid, "saved now")
            
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})