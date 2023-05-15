from django.shortcuts import render, redirect, HttpResponse
from main.models import Campany,Network, UserLog
from django.contrib.auth.decorators import login_required, permission_required


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

def addNetwork(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        network = request.POST.get('network')
        state = request.POST.get('state')
        description = request.POST.get('description')
        company_id = Campany.objects.get(id=company)
  
        new_network = Network(network=network, state=state, description=description,compony_info=company_id)
        new_network.save()
        
        success = 'data successfully saved'
        UserLog.objects.create(
            user=request.user,
            message=f"{request.user}  added new network ({new_network.network}) for ({company_id.owner})",
        )
    return HttpResponse(success)

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