from django.shortcuts import render, redirect, HttpResponse
from main.models import Campany,Network

# Create your views here.

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

    return render(request,'pages/networkDetails.html',context)

def all_networks(request):
    networks = Network.objects.all()
    companyList = Campany.objects.all()
    context = {
        'networks': networks,
        'companyData': companyList,
        'totalNetworks': networks.count()
    }
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
    return HttpResponse(success)


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
        else:
            messages = "Error  ..........."
            
    return HttpResponse(messages)