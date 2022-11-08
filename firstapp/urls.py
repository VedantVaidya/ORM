from django.urls import path
from . import views as v

urlpatterns = [
    path("",v.home),
    path("insert",v.insertdata),
    path("insert2",v.insertdata2),
    path("insert3",v.insertdata3),
    path("AddEmp",v.AddEmp),
    path("AddAccount",v.AddAccount)
]
