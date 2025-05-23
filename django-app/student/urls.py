from django.urls import path
from . import views
from admin_route.views import saved_tutorials

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('game/', views.game, name='game'),
    path('task/', views.task, name='task'),
    path('settings/', views.settings, name='settings'),
    path('tutorials', views.tutorial, name='tutorial')
]
