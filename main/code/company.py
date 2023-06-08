import traceback
from django.http import JsonResponse
from user_agents import parse
from django.shortcuts import render, HttpResponse
from main.models import Campany,UserLog, ErrorLog
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url='login')
@permission_required('main.view_campany', raise_exception=True, login_url=None)
def company(request):  
    device_info = hanldeLog(request) 
    try:
        listCompany = Campany.objects.all()
        context = {'company': listCompany}
        msg = f"You Visted List Of Company Page"
        UserLog(user=request.user,device=device_info,message=msg).save()
        return render(request,'pages/company.html',context)
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

@login_required(login_url='login')
@permission_required('main.add_campany', raise_exception=True, login_url=None)
def createCompany(request):
        device_info = hanldeLog(request)
        try:
            if request.method == 'POST':
                name = request.POST.get('name')
                case = request.POST.get('description')
                asn = request.POST.get('asn')
                is_exist = Campany.objects.filter(asn = asn)
                if is_exist:
                    message=f"ASN  ({asn})  Already Given to anotehr company!"
                             
                    return JsonResponse({'success': False, 'error':message})
                else:
                    new_company = Campany(title=case, owner=name, asn=asn)
                    new_company.save()
                    company = Campany.objects.filter(asn = asn)
                    if company: # check if company is created ans saved.
                        success = True
                    if success: 
                        UserLog.objects.create(
                        user=request.user,device=device_info,
                        message=f"You Successfully created Company: {new_company.owner}",
                        )
                        msg = f"Company {new_company.owner} with Asn: {asn} is created succefully"
                        return JsonResponse({'success': True, 'message':msg})
        except Exception as e:
            info = traceback.format_exc()   
            ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
          
            return JsonResponse({'success': False, 'error': f"{str(e)}"})

@login_required(login_url='login')
@permission_required('main.change_campany', raise_exception=True, login_url=None)
def editCompany(request):
    device_info = hanldeLog(request)
    try: 
        if request.method == 'POST':
            id = request.POST.get('id')
            name = request.POST.get('name')
            asn = request.POST.get('asn')
            description = request.POST.get('description')

            company_update = Campany.objects.get(id=id)
            
            company_update.owner = name
            company_update.asn = asn
            company_update.title = description

            print(company_update.owner, ":",name)
            print(company_update.asn, ":",asn)
            print(company_update.title, ":",description)

            company_update.save()

            success = True
            if success:
                UserLog.objects.create(
                user=request.user,
                device=device_info,
                message=f"You Updated Company: {company_update.owner}",
            )
                messages = 'Successfully Updated company'
                msg = f"Company {company_update.owner} with Asn: {asn} is created succefully"
                return JsonResponse({'success': True, 'message':msg})
            else:
                messages = "Error  ..........."
            
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
                
    return HttpResponse(messages)


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
 