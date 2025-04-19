from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

def home(request):
    return redirect('login')

def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def admin_tutorial(request):
    return render(request, 'admin_tutorial.html')

def success(request):
    return render(request, 'success.html')

