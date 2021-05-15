import datetime
from dateutil.parser import parse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import clientdetails
from .forms import clientsform

from django.db.models.functions import TruncMonth, TruncDay, Extract, TruncYear

# Create your views here.
from django.urls import reverse


def addclients(request):
    # now = datetime.datetime.today()
    clients = clientdetails.objects.all()
    print("Clients added successfully ")
    # form = clientsform()
    # if request.method == 'POST':
    #     form = clientsform(request.post)
    #
    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'clients/view_clients.html')
    #     else:
    #         messages.info(request, 'SomeThing Is Wrong')
    #         return render(request, 'clients/index.html')
    # context = {'form': form}
    # return render(request, 'clients/index.html', context)
    if request.method == 'POST':

        name = request.POST["Name"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        moblieno = request.POST["moblieno"]
        address = request.POST["address"]
        diseases = request.POST["diseases"]
        # packagep = request.POST["packagep"]
        packages = request.POST["packages"]
        packagee = request.POST["packagee"]
        feesp = request.POST["feesp"]
        tranningtype = request.POST["tranningtype"]
        dob = request.POST["dob"]

        def age():
            bday = parse(dob)
            now = datetime.datetime.today()
            return (now.year - bday.year) - int((now.month, now.day) < (bday.month, bday.day))

        def packagep():
            start = parse(packages)
            end = parse(packagee)
            package = int((end - start).days/30)
            return package

        if clientdetails is not None:
            if clientdetails.objects.filter(name=name).exists():
                print("User Already Taken")
                messages.info(request, "Client Already Taken")
                return render(request, 'clients/index.html')
            else:
                form = clientdetails(name=name, age=age(), gender=gender, email=email, mobileno=moblieno,
                                     address=address, diseases=diseases, packagep=packagep(), packages=packages,
                                     packagee=packagee, feesp=feesp, tranningtype=tranningtype, dob=dob)
                form.save()
                return render(request, "clients/index.html")
        else:
            print("Something Is Wrong")
            messages.info(request, "Client Already Taken")
            return render(request, "clients/index.html")

    else:
        return render(request, "clients/index.html")


def edit(request, id):
    clients = clientdetails.objects.all()
    for client in clients:
        return render(request, 'clients/edit.html', {
            'clients': client
    })

#
# def update(request, id):
#     clients = clientdetails.objects.get(id=id)


# def age(request):
#     clients = clientdetails.objects.all()
#     clientdetails.objects.annotate(year=TruncYear('dob'))
#     now = datetime.datetime.today()
#
#     for client in clients:
#         cdob = client.dob
#         age = now - client.dob
#         # form = clientdetails(age=age)
#         # form.save()
#         return render(request, 'clients/view_clients.html', {
#             'ages': age,
#             'client': cdob
#         })


def view_clients(request):
    view_client = clientdetails.objects.all()
    return render(request, "clients/view_clients.html", {
        "viewclients": view_client
    })


def dob(request):

    details = []

    now = datetime.datetime.today()
    month = clientdetails.objects.annotate(month=TruncMonth('dob'), day=TruncDay('dob')).all()
    clients = clientdetails.objects.all()
    for client in clients:
        if client.dob.month == now.month and client.dob.day == now.day:
            details.append({
                'name': client.name,
                'dob': client.dob
            })

            # clbd.append(client.name)
    return render(request, 'clients/dob.html', {
        'dobs': details,
        'now': now,
        'month': month,
        'client': clients
    })


    # now = datetime.datetime.today()
    # now1 = {'month':now.month, 'day':now.day}
    # # view_client = clientdetails.objects.all()
    # # dob = clientdetails.objects.values('dob')
    # clientdetails.objects.annotate(month=TruncMonth('dob'), day=TruncDay('dob')).all()
    # monthday = clientdetails.objects.values(month=Extract('dob', 'month'), day=Extract('dob', 'day'))
    #
    # return render(request, "clients/dob.html", {
    #     'dobs': now1,
    #     'monthday': monthday,
    #     # "viewclients": view_client
    # })

def renewald(request):
    renewaldetail = []
    # clientdetails.objects.annotate(date=TruncMonth('dob')).all()
    now = datetime.date.today()+datetime.timedelta(days=10)
    clients = clientdetails.objects.all()

    for client in clients:
        package = client.packagee
        if client.packagee == now:
            renewaldetail.append({
                'name': client.name,
                'mobile': client.mobileno,
                'packagee': client.packagee,
            })
    return render(request, 'clients/renewal.html', {
        'renewals': renewaldetail,
    })


