from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout, name='logout'),
    path('addDevice/', views.addDevice, name='addDevice'),
    path('deviceData/<int:id>', views.deviceData, name='deviceData'),
]