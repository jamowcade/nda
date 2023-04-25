from django.shortcuts import render
from main.models import Campany,Network

# Create your views here.

def network(request,id):

    companyList = Campany.objects.all()
    networkList = Network.objects.all()
    singleNetwork = Network.objects.filter(compony_info = id).all()
    context = {
        'companyData': companyList,
        'networkData': networkList,
        'singleNetwork': singleNetwork
    }

    # for n in networkList:
    #     print(n.compony_info)
    # print(singleNetwork)

    return render(request,'pages/network.html',context)