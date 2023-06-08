from django.shortcuts import render, HttpResponse, redirect
import json,traceback
from user_agents import parse
from datetime import datetime
from main.models import UserLog,ErrorLog
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.decorators import login_required, permission_required

from main.models import UserLog





@login_required(login_url='login')
@permission_required('auth.add_group', raise_exception=False, login_url='login')
def groups(request):
    device_info = hanldeLog(request)
    try:
        if request.method == 'POST':
            groupname = request.POST.get('gname')
            group = Group(name=groupname)
            group.save()
            msg = f"You Successfully Created Group Called {groupname}"
            UserLog(user=request.user,device=device_info,message=msg).save()
            return redirect('groups')
        groups = Group.objects.all()
        context = {
            "groups":groups
        }
        msg = f"You Visted Group Page"
        UserLog(user=request.user,device=device_info,message=msg).save()

        return render(request,'pages/groups.html', context)
    except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

@login_required(login_url='login')
@permission_required('auth.view_group', raise_exception=False, login_url='login')
def user_groups(request):
    device_info = hanldeLog(request)
    try:
        users = User.objects.all()
        groups = Group.objects.all()  
        context = {
            "users":users,
            "groups":groups
        } 
        msg = f"You Visted Assigning Group Page"
        UserLog(user=request.user,device=device_info,message=msg).save()
        return render (request, "pages/assign_user_to_groups.html", context)
    except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

@login_required(login_url='login')
@permission_required('auth.add_group', raise_exception=False, login_url='login')
def assign_user_to_groups(request):
    device_info = hanldeLog(request)
    try:
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            group_id = request.POST.get('group_id')
            is_checked = request.POST.get('is_checked')
            
            user = User.objects.get(id=user_id)
            group = Group.objects.get(id=group_id)
            
            if is_checked == 'true':
                user.groups.add(group)
                msg=f"You addded ({user.username}) to Group ({group.name})"
                UserLog(user=request.user,device=device_info,message=msg).save()
            else:
                user.groups.remove(group)
                msg=f"You  removed ({user.username}) from Group ({group.name})"
                UserLog(user=request.user,device=device_info,message=msg).save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})
    
    except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
    
@login_required(login_url='login')
@permission_required('auth.view_permission', raise_exception=False, login_url='login')
def get_user_groups(request):
    user_id = request.GET.get('user_id')
    
    user = User.objects.get(id=user_id)
    groups = [group.id for group in user.groups.all()]

    print(groups)
    return JsonResponse({'groups': groups})

@login_required(login_url='login')
@permission_required('auth.view_permission', raise_exception=False, login_url='login')
def groupPermissions(request):
    device_info = hanldeLog(request)
    try:
        groups = Group.objects.all()
        content_types = ContentType.objects.all()
        context = {
            "content_types": content_types,
            "groups": groups
        }
        msg = f"You Visted Assigning Permission Group Page"
        UserLog(user=request.user,device=device_info,message=msg).save()
        return render (request, "accounts/assignPermissionsGroup.html", context)
    except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)


@login_required(login_url='login')
@permission_required('auth.add_group', raise_exception=False, login_url='login')
def assign_permissions_to_group(request):
    device_info = hanldeLog(request)
    try:
        if request.method == 'POST':
            permission_id = request.POST.get('permission_id')
            group_id = request.POST.get('group_id')
            is_checked = request.POST.get('is_checked')

            group = Group.objects.get(id=group_id)
            permission = Permission.objects.get(id=permission_id)
            if is_checked == "true":
                group.permissions.add(permission)
                msg=f"You assigned permission ({permission.name}) to Group ({group.name})"
                UserLog(user=request.user,device=device_info,message=msg).save()
            else:
                group.permissions.remove(permission)
                msg=f"You removed permission ({permission.name}) from Group ({group.name})"
                UserLog(user=request.user,device=device_info,message=msg).save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})
    except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

@login_required(login_url='login')
#get permissions in each content type
@permission_required('auth.view_permission', raise_exception=False, login_url='login')
def get_permissions(request):
    device_info = hanldeLog(request)
    try:
        content_type_id = request.GET.get('content_type_id')
        content_type = ContentType.objects.get(id=content_type_id)
        permissions = Permission.objects.filter(content_type=content_type)
        # permissions_list = [{'id': p.id, 'name': p.name} for p in permissions ]
        # return JsonResponse(permissions_list, safe=False)
        context = {
            "permissions":permissions
        }
        msg = f"You Visted Permission Table Page"
        UserLog(user=request.user,device=device_info,message=msg).save()
        return render(request, 'pages/permissions_table.html', context)
    except Exception as e:
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)


@login_required(login_url='login')
# get permission of each group according to selected group and content type.
@permission_required('auth.view_permission', raise_exception=False, login_url='login')
def get_group_permissions(request):
    group_id = request.GET.get('group_id')
    print(group_id)
    content_type_id =  request.GET.get('content_type_id')
    group = Group.objects.get(id=group_id)
    content_type = ContentType.objects.get(id=content_type_id)
    group_permissions = group.permissions.filter(content_type=content_type)
    permissions_list = [p.id for p in group_permissions ]
    return JsonResponse({'permissions': permissions_list})


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
 