from django.urls import path
from .views import receive_location
from . import views
from .views import receive_location, home, index, login_view, logout_view

urlpatterns = [
    path('receive-location/', receive_location, name='receive_location'),
    path('locations/receive-location/', receive_location, name='receive_location'),
    path('', views.home, name='home'), 
    path('index', views.index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('registered_users/', views.registered_users, name='registered_users'),  
    path('lost_devices/', views.lost_devices, name='lost_devices'), 
    path('last_location/', views.last_location, name='last_location'),   
    path('devices_location/', views.devices_location, name='devices_location'),   

]
