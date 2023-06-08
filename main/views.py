import traceback,datetime
from user_agents import parse
from django.shortcuts import render
from django.db.models.functions import ExtractMonth,TruncMonth,TruncYear,TruncDay
from main.models import Campany,Network,Host,Port,ScanCase,UserLog,UserLoggers,ErrorLog
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from collections import defaultdict
# Create your views here.
@login_required(login_url='login')
def index(request):
    device_info = hanldeLog(request)
    try:
        current_year = datetime.datetime.now().year
        get_year = request.GET.get('get_year', current_year)

        monthList = []
        countListMonth = []
        countByYearName = []
        countByYearCount = []

        # Count Each Table Of Database
        totalCompany = Campany.objects.count()
        totalNetwork = Network.objects.count()
        totalHost = Host.objects.count()
        totalPorts = Port.objects.count()
        user_logs = UserLog.objects.all().order_by('-created_at')[:5][::1]

        # Geting Total Hosts For Each Month
        host_by_month = Host.objects.filter(host_date__year=get_year).annotate(month=TruncMonth('host_date')).values('month').annotate(count=Count('id'))
        for dateHost in host_by_month:
            changeNameMonth = dateHost['month'].strftime('%B'),
        
            month = changeNameMonth[0]
            
            monthList.append({
                'month':month
            })
            countListMonth.append({
                'count':dateHost['count']
            })
            # return monthList,countListMonth


        # Getiing Host added Each Year    
        # report_hosts_each_year = get_host_year(countByYearName,countByYearCount)
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
        top5CompanyInNetworks = get_top_5_company_networks()

        # Get The Highest Ports in Host and Adding them to the list
        top5NetworkPorts = get_top_5_network_ports()

        # Geting Ports State By Filtering "Open","Closed" & "Filtered"

        openPorts = Port.objects.filter(state="open").count()
        closePorts = Port.objects.filter(state="closed").count()
        filterPorts = Port.objects.filter(state="filtered").count()
  
        
        openstate = getOpenPorts(totalPorts,openPorts)
        closestate = getClosedPort(totalPorts,closePorts)
        filterstate = getfilterPorts(totalPorts,filterPorts)


        # Get Last Top 5 Activity Scan Cases
        top5scanCases = get_top_5_scan_cases()

        
        # Get top 10 hight Ports and add them to List
        get_hight_ports = get_top_10_ports()
        
    
        
        
        try:
            context = {
                'get_year': get_year,
                'company':totalCompany,
                'network':totalNetwork,
                'host':totalHost,
                'ports':totalPorts,
                'each_port_value': get_hight_ports,
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
                'topCompany':top5CompanyInNetworks,
                'topHost':top5NetworkPorts
                }
        except Exception as e:
            print(e)
        msg = f"You Visted List Of Dashboards"
        UserLog(user=request.user,device=device_info,message=msg).save()    
        return render(request, 'index.html',context)
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
      


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

# Get Total Hosts For Each Year 
def get_host_year(countByYearName,countByYearCount):
    host_by_year  = Host.objects.annotate(year=TruncYear('host_date')).values('year').annotate(count=Count('id'))
    for hostYear in host_by_year:
        changetoYear = hostYear['year'].year
        countByYearName.append({
            'year':changetoYear
        })
        countByYearCount.append({
            'count':hostYear['count']
        })
        return countByYearName,countByYearCount
    
# Get Top 5 Company Networks
def get_top_5_company_networks():
    topCompanyList = []
    lastList = []
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
    # for data in topCompanyList:
    #     data['percentage'] = round(count_company / sum_com * 100, 2)

    #     lastList.append({
    #         'company': data['company'], 
    #         'count': data['count'],
    #         'percentage': data['percentage'],
    #     })
    return topCompanyList

# Get Top 5 Network Ports
def get_top_5_network_ports():
    topHost = []
  
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

    return topHost

# Get Top 5 Scan Cases
def get_top_5_scan_cases():
    top5scanCases = []
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
    return top5scanCases

# Get Top 5 Scan Cases
def get_top_10_ports():
   eachPort = []
   topHighestPorts = []
   sum_total = 0
   each_port_value = Port.objects.values('port').annotate(count=Count('port')).order_by('-count')[:10][::1]
   for each in each_port_value:
         count = each['count']
         sum_total += count
         eachPort.append({
              'ports':each['port'],
              'count':each['count']
         })
   for each_port in eachPort:
        each_port['percentage'] = round(each_port['count'] / sum_total * 100, 2)
        topHighestPorts.append({
            'ports':each_port['ports'],
            'count':each_port['count'],
            'percentage':each_port['percentage'],
        })

   return topHighestPorts

def hanldeLog(request):
    user_agent_string = request.META.get('HTTP_USER_AGENT')
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = parse(user_agent_string)
    try:
        device_info = f"{ip_address} / {user_agent}"
        return device_info
    except Exception as e:
        device_info = f"{ip_address} / {user_agent}"
        info = traceback.format_exc()        
        ErrorLog.objects.create(user="AnonymousUser",device=device_info, message=str(e), info=info)
 

#delete_group
@csrf_exempt
def delete_group(request):
    
    group_id = request.POST.get('group_id')

    group = Group(id=group_id)
    print(group.id)
    group.delete()
    
    groups = Group.objects.all()
    context = {
        "groups":groups,
        "message":"Delete group Successfully"
    }

    return render(request,'pages/groups.html', context)



