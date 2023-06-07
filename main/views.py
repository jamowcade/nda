import json
from django.shortcuts import render
from django.db.models.functions import ExtractMonth,TruncMonth,TruncYear,TruncDay
from main.models import Campany,Network,Host,Port,ScanCase,UserLog,UserLoggers
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from collections import defaultdict
# Create your views here.
@login_required(login_url='login')
def index(request):
    eachPort = []
    monthList = []
    topCompanyList = []
    topNetworkList = []
    topHost = []
    countListMonth = []
    countByYearName = []
    countByYearCount = []
    top5scanCases = []

    # Count Each Table Of Database
    totalCompany = Campany.objects.count()
    totalNetwork = Network.objects.count()
    totalHost = Host.objects.count()
    totalPorts = Port.objects.count()

    # Geting Hosts Added Each Month
    host_by_month = Host.objects.annotate(month=TruncMonth('host_date')).values('month').annotate(count=Count('id'))
    for dateHost in host_by_month:
        changeNameMonth = dateHost['month'].strftime('%B'),
       
        month = changeNameMonth[0]
        
        monthList.append({
            'month':month
        })
        countListMonth.append({
            'count':dateHost['count']
        })

    # Getiing Host added Each Year    
    host_by_year  = Host.objects.annotate(year=TruncYear('host_date')).values('year').annotate(count=Count('id'))
    for hostYear in host_by_year:
        changetoYear = hostYear['year'].year
        countByYearName.append({
            'year':changetoYear
        })
        countByYearCount.append({
            'count':hostYear['count']
        })


    #Get Top Company In Networks and them to the list
    same_company_count = Network.objects.values('compony_info').annotate(count=Count('compony_info_id')).filter(count__gt=1).order_by('-count')[:5][::1]
    sum_com = 0
    for same_company in same_company_count:
        comp_id = same_company['compony_info']
        count_company = same_company['count']
        sum_com += count_company
        get_in_company = Campany.objects.filter(id=comp_id).all()
        same_company['percentage'] = round(count_company / sum_com * 100)
        for singlecom in get_in_company:

            topCompanyList.append({
                'company': singlecom.owner,
                'count': count_company,
                'percentage': same_company['percentage'],
                

            })
    



    # Geting Ports State By Filtering "Open","Closed" & "Filtered"

    openPorts = Port.objects.filter(state="open").count()
    closePorts = Port.objects.filter(state="closed").count()
    filterPorts = Port.objects.filter(state="filtered").count()
    
    openstate = getOpenPorts(totalPorts,openPorts)
    closestate = getClosedPort(totalPorts,closePorts)
    filterstate = getfilterPorts(totalPorts,filterPorts)


    # Get Last Top 5 Activity Scan Cases
    top_date_scan = Host.objects.annotate(day=TruncDay('host_date')).values('day').annotate(count=Count('id')).order_by('-count')[:5]
    for group in top_date_scan:
        date_scan = group['day'].strftime('%Y-%m-%d')
        get_scan_date = ScanCase.objects.filter(scan_date=date_scan).all()
        for scan in get_scan_date:
            top5scanCases.append({
                'id':scan.id,
                'scan':scan.name,
                'scan_date':date_scan,
                'count':group['count']
            })
    print(top5scanCases)
        
    user_logs = UserLog.objects.all().order_by('-created_at')[:5][::1]


    # Get top 10 hight Ports and add them to List
    
    each_port_value = Port.objects.values('port').annotate(count=Count('port')).order_by('-count')[:10][::1]
  
    for each in each_port_value:
         each['percentage'] = round(each['count'] / totalPorts * 100, 2)

         eachPort.append({
              'ports':each['port'],
              'count':each['count'],
              'percentage':each['percentage'],
         })
    

    # Get Top Hight Host in Networks
    same_network = Host.objects.values('network_id').annotate(count=Count('network_id')).filter(count__gt=1).order_by('-count')[:5][::1]
    
    for single_network_id in same_network:
        host_id = single_network_id['network_id']
        count_host = single_network_id['count']
        get_each_host_id = Host.objects.filter(id=host_id).all()
        for each_host in get_each_host_id:
            # print(each_host)
            network = each_host.network.network 
            company = each_host.network.compony_info.owner
            topNetworkList.append({
                'network': network,
                'company': company,
                'count': count_host,

            })

    # print("------>>>> ",topNetworkList)
    

    
    # Get The Highest Ports in Host and Adding them to the list

    same_host = Port.objects.values('host_id').annotate(count=Count('host_id')).filter(count__gt=1).order_by('-count')[:5][::1]
    sum_host = 0
    for single_host_id in same_host:
        port_id = single_host_id['host_id']
        count_port = single_host_id['count']
        sum_host+=count_port
        single_host_id['percentage'] = round(count_port / sum_host * 100)
        get_each_port_id = Port.objects.filter(id=port_id).all()
        for each_port in get_each_port_id:
            host = each_port.host.hostname
            network = each_port.host.network.network
            company = each_port.host.network.compony_info.owner
            topHost.append({
                'host': host,
                'network': network,
                'company': company,
                'count': count_port,
                'percentage': single_host_id['percentage'],


            })
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
        'top_scan':top5scanCases,
        'user_logs':user_logs,
        'chartDataByMonth':monthList,
        'chartCountByMonth':countListMonth,
        'chartDataByYear':countByYearName,
        'chartCountByYear':countByYearCount,
        'topCompany':topCompanyList,
        'topHost':topHost
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
