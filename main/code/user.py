from django.shortcuts import render, redirect
from main.models import Campany, UserLog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
# Create your views here.



def login_user(request):
    if request.user.is_authenticated:

        # messages.info(request, 'alredy login')
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
             # log the user action
            # userLoggers.objects.create(user=request.user, action='created item')
            # logger.info('User %s login the system', request.user.username)
            return redirect('/')
        else:
            messages.info( request, 'User or Password are Incorrect.')
            return render(request,'accounts/login2.html/')
        
    return render(request, 'accounts/login2.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):

    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forget.html')

@permission_required('main.add_user', login_url='/login/', raise_exception=False)
def users(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = "123"
        role = request.POST['role']
        if role == "superuser":
            User.objects.create_superuser(username=username, password=password, email=username)
        else:
            group = Group.objects.get(name=role)
            user = User.objects.create_user(username=username, password=password, email=username)
            user.groups.add(group)
            return redirect('users')
    users = User.objects.all()
    roles = Group.objects.all()
    context = {
        "users":users,
        "roles":roles
    }
    return render(request,'accounts/staffs.html', context)

@login_required(login_url='login')
@permission_required('main.add_user', login_url='/login/', raise_exception=False)
def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        if role == "superuser":
            User.objects.create_superuser(username=username, password=password)
            UserLog.objects.create(
            user=request.user,
            message=f"{request.user} created new Superuser {user.username} user",
             )
        else:
            group = Group.objects.get(name=role)
            user = User.objects.create_user(username=username, password=password)
            user.groups.add(group)
            UserLog.objects.create(
            user=request.user,
            message=f"{request.user} created new {group.name} email {user.username} user",
             )
            return redirect('users')
        
@login_required(login_url='login')
def permissions(request):

    content_types = ContentType.objects.all()
    context = {
        "content_types":content_types
    }
    return render (request, "pages/user_permissions.html", context)
@login_required(login_url='login')
@csrf_exempt
def get_user_info(request):
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
@login_required(login_url='login')
def get_permissions_user(request):
    content_type_id = request.GET.get('content_type_id')
    content_type = ContentType.objects.get(id=content_type_id)
    permissions = Permission.objects.filter(content_type=content_type)
    # permissions_list = [{'id': p.id, 'name': p.name} for p in permissions ]
    # return JsonResponse(permissions_list, safe=False)
    context = {
        "permissions":permissions
    }
    return render(request, 'pages/user_permissions_table.html', context)
@login_required(login_url='login')
# get user permissions according to selected user and content type.
def get_user_permissions(request):
    user_id = request.GET.get('user_id')
    print(user_id)
    content_type_id =  request.GET.get('content_type_id')
    user = User.objects.get(username=user_id)
    content_type = ContentType.objects.get(id=content_type_id)
    user_permissions = user.user_permissions.all()
    permissions_list = [p.id for p in user_permissions ]
    print(permissions_list)
    return JsonResponse({'permissions': permissions_list})

@login_required(login_url='login')

# assigns permission to user
def assign_permissions_to_user(request):
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
            message=f"{request.user}  give permission {permission.name}  to user {user.username}",
        )
        return JsonResponse({'status': 'success'})
    
    else:
        return JsonResponse({'status': 'error'})
    


@login_required(login_url='login')
def myprofile(request):
    
    return render (request, "accounts/myprofile.html")




@login_required(login_url='login')
def changepassword(request):
    
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
            msg = f"User Has Been Successfully Changed {userupdatePassword.first_name} {userupdatePassword.last_name}'s Password"
            UserLog(user=request.user,message=msg).save()
            return JsonResponse(response)
        else:
            messages.error(request,f"{userupdatePassword.username}'s Not Changed Password")
            msg = f"User Has Not Successfully Changed {userupdatePassword.first_name} {userupdatePassword.last_name}'s Password"
            UserLog(user=request.user,message=msg).save()
            return redirect(myprofile)
    else:

        return redirect(myprofile)
