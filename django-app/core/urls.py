from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    #path('admin/', views.admin, admin.site.urls),
    #place all primary directories here
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/', include('student.urls')),
]
