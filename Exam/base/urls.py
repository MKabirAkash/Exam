from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('createadmin/', views.createadmin,name="createadmin"),
    path('login/', views.login,name="login"),
]