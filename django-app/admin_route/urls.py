from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.make_admin_tutorial, name='admin_tutorial'),
    path('admin_tutorial', views.make_admin_tutorial, name='admin_tutorial')
    
]