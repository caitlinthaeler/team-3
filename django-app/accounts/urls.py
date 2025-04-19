from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.select_login_role, name='select_login_role'),
    path('student/', include('student.urls')),
    path('teacher/', include('student.urls')),
    
]