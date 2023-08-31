from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('createadmin/', views.createadmin,name="createadmin"),
    path('addemployee/', views.addemployee,name="employeeadd"),
    path('addgadget/', views.addgadget,name="gadgetadd")
]