from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from main.models import Campany, ErrorLog,Network, UserLog
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='login')
# Create your views here.
@permission_required('main.view_network', raise_exception=True, login_url=None)
def networkDetails(request,id):
    
    companyList = Campany.objects.all()
    company = Campany.objects.get(id=id)
    networkList = Network.objects.all()
    singleNetwork = Network.objects.filter(compony_info = id).all()
    context = {
        'companyData': companyList,
        'networkData': networkList,
        'singleNetwork': singleNetwork,
        'companyName': company.owner,
        'companyID': company.id,
        'total': singleNetwork.count()
        
    }
    # if request.method == 'POST':

    #     addNetwork(request)

    # for n in networkList:
    #     print(n.compony_info)
    # print(singleNetwork)
    UserLog.objects.create(
            user=request.user,
            message=f"user visisted network Details page",
        )
    return render(request,'pages/networkDetails.html',context)
@login_required(login_url='login')
@permission_required('main.view_network', raise_exception=True, login_url=None)
def all_networks(request):
    networks = Network.objects.all()
    companyList = Campany.objects.all()
    context = {
        'networks': networks,
        'companyData': companyList,
        'totalNetworks': networks.count()
    }
    # UserLog.objects.create(
    #         user=request.user,
    #         message=f"user visisted network listing page",
    #     )
    return render(request, 'pages/networks.html',context)
@login_required(login_url='login')
@permission_required('main.add_network', login_url='/login/', raise_exception=False)
def addNetwork(request):
    try:
        if request.method == 'POST':
            company = request.POST.get('company')
            network = request.POST.get('network')
            state = request.POST.get('state')
            description = request.POST.get('description')
            company_id = Campany.objects.get(id=company)
            is_network_exist = Network.objects.filter(network = network)
            if is_network_exist:
                message=f"Network  ({network})  Already Created for { company_id.owner} at ({company_id.timestamp}"
                return JsonResponse({'success': False, 'error':message})
            else:
                new_network = Network(network=network, state=state, description=description,compony_info=company_id)
                new_network.save()
                network_created = Network.objects.filter(network = network)
                if network_created:
                    success = True
                if success:
                  
                    UserLog.objects.create(
                        user=request.user,
                        message=f"{request.user}  added new network ({new_network.network}) for ({company_id.owner}))",
                         )
                    message=f"Network  ({network})  Created for { company_id.owner}"
                    return JsonResponse({'success': True, 'message':message})
    except Exception as e:
        ErrorLog.objects.create(
                user=request.user,
                message=f"An error occurred: {str(e)}",
            )
        return JsonResponse({'success': False, 'error': f"{str(e)}"})
    
@login_required(login_url='login')
@permission_required('main.change_network', raise_exception=True, login_url=None)
def updateNetwork(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        network = request.POST.get('network')
        state = request.POST.get('state')
        description = request.POST.get('description')

        network_update = Network.objects.get(id=id)

        network_update.network = network
        network_update.state = state
        network_update.description = description

        network_update.save()

        success = True
        if success:
            messages = 'Successfully Update'
            UserLog.objects.create(
            user=request.user,
            message=f"{request.user}  updated network ({network_update.network})",
        )
        else:
            messages = "Error  ..........."
        
    return HttpResponse(messages)



import ipaddress

def network_ip_is_valid(ip_address):
    try:
        ipaddress.IPv4Address(ip_address)
        return True
    except ipaddress.AddressValueError:
        return False