from main.models import UserLog, ErrorLog
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url='user_login')
def erorlogs(request):
    error_logs = ErrorLog.objects.all().order_by('created_at')
    context = {
        "error_logs": error_logs
    }
    return render (request, "pages/logs/erorlogs.html", context)


@login_required(login_url='user_login')
def userlogs(request):
    user_logs = UserLog.objects.all().order_by('created_at')
    context = {
        "user_logs":user_logs
    }
    return render (request, "pages/logs/userlogs.html", context)


@login_required
def my_view(request):
    if request.method == 'POST':
        # Do something that might raise an exception
        try:
            result = 1 / 0
        except Exception as e:
            # Log the error to the database
            ErrorLog.objects.create(
                user=request.user,
                message=f"An error occurred: {str(e)}",
            )

            # Return an error response
            return HttpResponse("An error occurred.")
    else:
        # Log the user activity to the database
        UserLog.objects.create(
            user=request.user,
            message="User performed an action.",
        )

    # Get the error logs and user logs from the database
    error_logs = ErrorLog.objects.filter(user=request.user).order_by('created_at')
    user_logs = UserLog.objects.filter(user=request.user).order_by('created_at')

    return render(request, 'my_template.html', {'error_logs': error_logs, 'user_logs': user_logs})