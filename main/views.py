from django.shortcuts import render
from main.models import Campany,Network,Host,Port,ScanCase,UserLog
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count

# Create your views here.
@login_required(login_url='login')
def index(request):
    eachPort = []

    # Count Each Table Of Database
    totalCompany = Campany.objects.count()
    totalNetwork = Network.objects.count()
    totalHost = Host.objects.count()
    totalPorts = Port.objects.count()
    
    # ppp = Port.objects.annotate(count=Count('port')).order_by('-count')[:5]
    # for p in ppp:
    #     print(p.port)

    each_port_value = Port.objects.values('port').annotate(count=Count('port')).order_by('-count')[:5][::1]

    # Geting Ports State By Filtering "Open","Closed" & "Filtered"

    openPorts = Port.objects.filter(state="open").count()
    closePorts = Port.objects.filter(state="closed").count()
    filterPorts = Port.objects.filter(state="filtered").count()
    

    openstate = getOpenPorts(totalPorts,openPorts)
    closestate = getClosedPort(totalPorts,closePorts)
    filterstate = getfilterPorts(totalPorts,filterPorts)


    # Get Last Top 5 Activity Scan Cases
    top_scan = ScanCase.objects.all().order_by('-id')[:5][::-1]
    user_logs = UserLog.objects.all().order_by('created_at')[:5][::-1]


    
  
    for each in each_port_value:
         each['percentage'] = round(each['count'] / totalPorts * 100, 2)

         eachPort.append({
              'ports':each['port'],
              'count':each['count'],
              'percentage':each['percentage'],
         })
    print(eachPort)
   
    context = {
        'company':totalCompany,
        'network':totalNetwork,
        'host':totalHost,
        'ports':totalPorts,
        'each_port_value': eachPort,
        'openstate':openstate,
        'openport':openPorts,
        'closestate':closestate,
        'closeport':closePorts,
        'filterstate':filterstate,
        'filterport':filterPorts,
        'top_scan':top_scan,
        'user_logs':user_logs,
        }    
    return render(request, 'index.html',context)


def getOpenPorts(totalPorts,openPorts):
    if totalPorts > 0:
        openPercentage = round(openPorts / totalPorts * 100, 2)
        return openPercentage
    else:
        openPercentage = 0
        return openPercentage

def getClosedPort(totalPorts,closedPorts):
    if totalPorts > 0:
        openPercentage = round(closedPorts / totalPorts * 100, 2)
        return openPercentage
    else:
        openPercentage = 0
        return openPercentage

def getfilterPorts(totalPorts,filteredPorts):
    if totalPorts > 0:
        openPercentage = round(filteredPorts / totalPorts * 100, 2)
        return openPercentage
    else:
        openPercentage = 0
        return openPercentage
