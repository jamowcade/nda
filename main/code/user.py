import traceback
from user_agents import parse
from django.shortcuts import render, redirect
from main.models import Campany, UserLog,ErrorLog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
# Create your views here.


def login_user(request):

    try:
        device_info = hanldeLog(request)
        if request.user.is_authenticated:

            # messages.info(request, 'alredy login')
            return redirect('/')
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                msg = f"{request.user.first_name} {request.user.last_name} Logged System"
                # print(f'{request.user} - {device_info} - {msg}')
                UserLog(user=request.user,device=device_info,message=msg).save()
                return redirect('/')
            else:
                messages.info( request, 'User or Password are Incorrect.')
                msg = f"{request.POST['email']} Failed Logged System"
                UserLog(user=request.POST['email'],device=device_info,message=msg).save()
                return render(request,'accounts/login2.html/')
            
        return render(request, 'accounts/login2.html')
    
    except Exception as e:
        device_info = hanldeLog(request)
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

@login_required(login_url='login')
def logout_user(request):
    try: 
        device_info = hanldeLog(request)
        msg = f"{request.user.first_name} {request.user.last_name} Logged Out System"
        # print(f'{request.user} - {device_info} - {msg}')
        UserLog(user=request.user,device=device_info,message=msg).save()
        logout(request)
        return redirect('login')
    
    except Exception as e:
        device_info = hanldeLog(request)
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
    


@login_required(login_url='login')
@permission_required('main.add_user',raise_exception=False,login_url='login')
def users(request):
    device_info = hanldeLog(request)
    try: 
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = "123"
            status = False
            role = request.POST['role']
            if role == "superuser":
                try:
                    User.objects.create_superuser(
                    first_name=first_name, last_name=last_name,
                    username=username, password=password,
                    email=email, is_active=status
                )
                    msg = f"You Has Been Successfully Created {first_name} {last_name}'s Account as {role}"
                    UserLog(user=request.user,device=device_info,message=msg).save()
                except Exception as e:
                    info = traceback.format_exc()   
                    ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

                # User.objects.create_superuser(username=username, password=password, email=username)
            else:
                try:
                    group = Group.objects.get(name=role)
                    user = User.objects.create_user(first_name=first_name, last_name=last_name,
                    username=username, password=password,
                    email=email, is_active=status)
                    user.groups.add(group)
                    msg = f"You Has Been Successfully Created {first_name} {last_name}'s Account as {role}"
                    UserLog(user=request.user,device=device_info,message=msg).save()
                    return redirect('users')
                except Exception as e:
                    info = traceback.format_exc()   
                    ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
        users = User.objects.all()
        roles = Group.objects.all()
        context = {
            "users":users,
            "roles":roles
        }
        msg = f"You Visted List Of User Accounts"
        UserLog(user=request.user,device=device_info,message=msg).save()

        return render(request,'accounts/staffs.html', context)
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)


@login_required(login_url='login')
@permission_required('auth.view_permission', raise_exception=False,login_url='login')
def permissions(request):

    device_info = hanldeLog(request)
    try: 

        content_types = ContentType.objects.all()
        context = {
            "content_types":content_types
        }
        msg = f"You Visted List Of User Permissions"
        UserLog(user=request.user,device=device_info,message=msg).save()
        return render (request, "pages/user_permissions.html", context)
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)


@login_required(login_url='login')
@csrf_exempt
@permission_required('auth.view_user', raise_exception=False, login_url='login')
def get_user_info(request):
    device_info = hanldeLog(request)
    try: 
        search_value = request.POST.get('search_value')
        users = User.objects.filter(username__icontains=search_value)# Only retrieve the first matching user
        user_list = []
        for user in users:
            user_list.append({
                'name': user.username,
                'email': user.email,
                'user_id':user.id
            })

        return JsonResponse(user_list, safe=False)
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)


@login_required(login_url='login')
@permission_required('auth.change_user', raise_exception=False, login_url='login')
def get_permissions_user(request):
    try:
        device_info = hanldeLog(request)
        content_type_id = request.GET.get('content_type_id')
        content_type = ContentType.objects.get(id=content_type_id)
        permissions = Permission.objects.filter(content_type=content_type)
        # permissions_list = [{'id': p.id, 'name': p.name} for p in permissions ]
        # return JsonResponse(permissions_list, safe=False)
        context = {
            "permissions":permissions
        }
        msg = f"You Displayed User Permissions Table"
        UserLog(user=request.user,device=device_info,message=msg).save()
        return render(request, 'pages/user_permissions_table.html', context)
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)    


@login_required(login_url='login')
@permission_required('auth.add_user', raise_exception=False,login_url='login')
# get user permissions according to selected user and content type.
def get_user_permissions(request):
    device_info = hanldeLog(request)
    try:
        user_id = request.GET.get('user_id')
        print(user_id)
        content_type_id =  request.GET.get('content_type_id')
        user = User.objects.get(username=user_id)
        content_type = ContentType.objects.get(id=content_type_id)
        user_permissions = user.user_permissions.all()
        permissions_list = [p.id for p in user_permissions ]
        print(permissions_list)
        return JsonResponse({'permissions': permissions_list})
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)


# assigns permission to user
@permission_required('auth.add_user', raise_exception=False, login_url='login')
def assign_permissions_to_user(request):
    device_info = hanldeLog(request)
    try:
        if request.method == 'POST':
            permission_id = request.POST.get('permission_id')
            user_id = request.POST.get('user_id')
            is_checked = request.POST.get('is_checked')

            user = User.objects.get(username=user_id)
            permission = Permission.objects.get(id=permission_id)
            if is_checked == "true":
                user.user_permissions.add(permission)
                
            else:
                user.user_permissions.remove(permission)
            UserLog.objects.create(
                user=request.user,
                device=device_info,
                message=f"{request.user}  give permission {permission.name}  to user {user.username}",
            )
            return JsonResponse({'status': 'success'})
        
        else:
            return JsonResponse({'status': 'error'})
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
    


@login_required(login_url='login')
@permission_required('auth.view_user', raise_exception=False,login_url='login')
def myprofile(request):
    device_info = hanldeLog(request)
    try:
        msg = f"You Visited Account Profile "
        UserLog.objects.create(
                user=request.user,
                device=device_info,
                message=msg,
            )
        return render (request, "accounts/myprofile.html")
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)




@login_required(login_url='login')
@permission_required('auth.change_user', raise_exception=False,login_url='login')
def changepassword(request):

    device_info = hanldeLog(request)
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            password = request.POST.get('password')
            userupdatePassword = User.objects.get(id=id)
            userupdatePassword.set_password(password)
            userupdatePassword.save()            
            if userupdatePassword:
                info = f"{userupdatePassword.first_name} {userupdatePassword.last_name}'s Successfully Changed Password"
                response = {
                    'success': True,
                    'message': info
                }
                msg = f"You Has Been Successfully Changed {userupdatePassword.first_name} {userupdatePassword.last_name}'s Password"
                UserLog(user=request.user,device=device_info,message=msg).save()
                return JsonResponse(response)
            else:
                messages.error(request,f"{userupdatePassword.username}'s Not Changed Password")
                msg = f"User Has Not Successfully Changed {userupdatePassword.first_name} {userupdatePassword.last_name}'s Password"
                UserLog(user=request.user,device=device_info,message=msg).save()
                return redirect(myprofile)
        else:

            return redirect(myprofile)
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
        



@login_required(login_url='user_login')
@permission_required('auth.change_user', raise_exception=False,login_url='login')
def activeAccount(request):

    device_info = hanldeLog(request)
    try:
   
        if request.method == 'POST':
            id = request.POST.get('id')
            password = request.POST.get('password')
            status = True
            user = User.objects.get(id=id)
            user.is_active = status
            user.set_password(password)
            user.save()
            if user:
                info = f'{user.first_name} {user.last_name} has been Successfuly Activated'
                msg = f"You has been Successfuly Activated {user.first_name} {user.last_name} to the system"

                UserLog.objects.create(
                user=request.user,
                device=device_info,
                message=msg,
            )

                return JsonResponse({'success': True, 'message': info})
            else:
                msg = f"User has Not Successfuly Activated {user.first_name} {user.last_name} to the system"
                ErrorLog.objects.create(user=request.user,device=device_info, message=msg)
                return JsonResponse({'success': False, 'message': msg})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
        


@login_required(login_url='user_login')
@permission_required('auth.change_user', raise_exception=False,login_url='login')
def disableAccount(request):

    device_info = hanldeLog(request)
    try:
   
        if request.method == 'POST':
            id = request.POST.get('id')
            status = False

            user = User.objects.get(id=id)
            user.is_active = status
            user.save()
            if user:
                # print(first_name,last_name,email,user_name)
                info = f'{user.first_name} {user.last_name} has been Successfuly Disabled'
                msg = f"You has been Successfuly Disabled {user.first_name} {user.last_name} to the system"
                UserLog.objects.create(
                user=request.user,
                device=device_info,
                message=msg,
            )
                
                return JsonResponse({'success': True, 'message': info})
            else:
                msg = f"You has Not Successfuly Disabled {user.first_name} {user.last_name} to the system"
                info = traceback.format_exc()   
                ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)
                return JsonResponse({'success': False, 'message': 'Not Successfully Disabled'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

@login_required(login_url='login')
@permission_required('auth.change_user', raise_exception=False,login_url='login')
def updateAccount(request):
    device_info = hanldeLog(request)
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            userUpdate = User.objects.get(id=id)

            userUpdate.first_name = first_name
            userUpdate.last_name = last_name
            userUpdate.email = email

            userUpdate.save()

            success = True
            if userUpdate:
                info = f'{userUpdate.first_name} {userUpdate.last_name} has been Successfuly Updated'
                msg = f"You has been Successfuly Updated {userUpdate.first_name} {userUpdate.last_name} to the system"
                UserLog.objects.create(
                user=request.user,
                device=device_info,
                message=msg,
            )

                return JsonResponse({'success': True, 'message': info})
            else:
                msg = f"You has Not Successfuly Updated {userUpdate.first_name} {userUpdate.last_name} to the system"
                ErrorLog.objects.create(user=request.user,device=device_info, message=msg)
                return JsonResponse({'success': False, 'message':'Not Successfully Activted'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
    except Exception as e:
        info = traceback.format_exc()   
        ErrorLog.objects.create(user=request.user,device=device_info, message=str(e),info=info)

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
 