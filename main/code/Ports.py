from django.shortcuts import render
from main.models import Port, Host,Service
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required(login_url='login')
@permission_required('main.view_port', login_url='/login/', raise_exception=False)
def all_ports(request, page):
    get_all_ports = Port.objects.all()
    paginator = Paginator(get_all_ports, 50)
    pagePaginator= paginator.get_page(page)
    context = {
        'ports':pagePaginator
    }

    return render(request,'pages/all_ports.html', context)







@login_required(login_url='login')
@permission_required('main.view_port', login_url='/login/', raise_exception=False)
def ports(request):
    host_id = request.GET.get('host_id')
    
    ports = Port.objects.filter(host=host_id).all()

    host_ports = []
    for port in ports:
        host_ports.append({
            "port": port.port,
            "protocol":port.protocol,
            "state": port.state,
            "reason": port.reason
        })
  
    
    return JsonResponse(host_ports, safe=False)




@login_required(login_url='login')
@permission_required('main.view_port', login_url='/login/', raise_exception=False)
def get_services(request):
    port_id = request.GET.get('port_id')
    
    service = Service.objects.filter(port=port_id).all()

    ServiceList = []
    for singleService in service:
        ServiceList.append({
            "key": singleService.key,
            "value":singleService.value
        })
    print(ServiceList)
  
    
    return JsonResponse(ServiceList, safe=False)