from django.shortcuts import render, redirect
from main.models import Campany
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.



def login_user(request):
    if request.user.is_authenticated:

        # messages.info(request, 'alredy login')
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password)
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


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    
    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forget.html')

def staffs(request):
    return render(request,'accounts/staffs.html')