from django.urls import path, include
from . import views
from django.contrib import admin
from django.shortcuts import redirect


urlpatterns = [
    # Redirect the root URL to login
    path('', lambda request: redirect('login/')),  # Default redirect to login
    #path('admin/', views.admin, admin.site.urls),
    #place all primary directories here
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/', include('student.urls')),
    path('login/', include('accounts.urls')),
]
