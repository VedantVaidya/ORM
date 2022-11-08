from django.shortcuts import render,redirect
from .models import Employee

def home(request):
    return render(request,"home.html")

def insertdata(request):
    if request.method=="GET":
        return render(request,"insert.html")
    elif request.method=="POST":
        name=request.POST.get("name")
        city=request.POST.get("city")
        email=request.POST.get("email")
        password=request.POST.get("password")
        obj=Employee()
        obj.name=name
        obj.city=city
        obj.email=email
        obj.password=password
        obj.save()
        return redirect("/")

from .form import *
def insertdata2(request):
    if request.method=="POST":
        obj=EmpForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={"form":EmpForm}
        return render(request,"insert2.html",d)


def insertdata3(request):
    if request.method=="POST":
        obj=EmpForm2(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={"form":EmpForm2}
        return render(request,"insert3.html",d)


def AddEmp(request):
    if request.method=="POST":
        obj=EmpForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={"form":EmpForm}
        return render(request,"AddEmp.html",d)

def AddAccount(request):
    if request.method=="POST":
        obj=AccForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={"form":AccForm}
        return render(request,"AddAccount.html",d)
