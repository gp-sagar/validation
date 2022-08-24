from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout, name='logout'),
    path('addDevice/', views.addDevice, name='addDevice'),
    path('deviceData/', views.deviceData, name='deviceData'),
]