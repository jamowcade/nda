from django.shortcuts import render, HttpResponse
from main.models import Campany,UserLog, ErrorLog
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url='login')
@permission_required('main.view_campany', raise_exception=True, login_url=None)
def company(request):   
    listCompany = Campany.objects.all()
    context = {'company': listCompany}
    UserLog.objects.create(
            user=request.user,
            message=f"{request.user}  visisted company listing page",
        )
    return render(request,'pages/company.html',context)

@login_required(login_url='login')
@permission_required('main.add_campany', raise_exception=True, login_url=None)
def createCompany(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            case = request.POST.get('description')
            asn = request.POST.get('asn')

            new_company = Campany(title=case, owner=name, asn=asn)
            new_company.save()

            success = 'data successfully saved'
            UserLog.objects.create(
            user=request.user,
            message=f"{request.user}  created Company: {new_company.owner}",
        )
            return HttpResponse(success)
        except Exception as e:
            ErrorLog.objects.create(
                user=request.user,
                message=f"An error occurred: {str(e)}",
            )

@login_required(login_url='login')
@permission_required('main.change_campany', raise_exception=True, login_url=None)
def editCompany(request):
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
            message=f"User Updated Company: {company_update.owner}",
        )
            messages = 'Successfully Updated company'
        else:
            messages = "Error  ..........."
            
    return HttpResponse(messages)
