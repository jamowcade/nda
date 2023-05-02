from django.shortcuts import render, HttpResponse
from main.models import Campany

# Create your views here.

def company(request):   
    listCompany = Campany.objects.all()
    context = {'company': listCompany}
    
    return render(request,'pages/company.html',context)


def createCompany(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        case = request.POST.get('description')
        asn = request.POST.get('asn')

        new_company = Campany(title=case, owner=name, asn=asn)
        new_company.save()

        success = 'data successfully saved'
    return HttpResponse(success)

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
            messages = 'Successfully Updated company'
        else:
            messages = "Error  ..........."
            
    return HttpResponse(messages)
