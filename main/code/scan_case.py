from main.models import Campany, Host, Network, Port, ScanCase
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from django.utils import timezone

@login_required(login_url='login')
@permission_required('main.view_scancase', raise_exception=False, login_url='login')
def scan_case(request):

    if request.method == 'POST':
        date = request.POST.get('date')
        name = f"scan case- {date}"
        is_exist = ScanCase.objects.filter(scan_date = date)
        date_is_less = compare_date(date)
        last_entry_date = ScanCase.objects.last().scan_date
        if date_is_less:
            return JsonResponse ({'success': False,"message":f"Scan case Date cannot be less than {last_entry_date} "})

        if is_exist:
            return JsonResponse ({'success': False,"message":"Scan case already Created"})
        scan_case = ScanCase(name=name, scan_date=date, description=name)
        scan_case.save()
        return JsonResponse ({'success': True,"message":"data saved"})

        print(name, date, description)
    else:
        scan_cases = ScanCase.objects.all()
   
        context = {
        "scan_cases":scan_cases,
        
        }
  
        return render(request, 'pages/scan_case.html', context)



def compare_date(date):
    given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    last_entry_date = ScanCase.objects.last().scan_date

    return given_date < last_entry_date