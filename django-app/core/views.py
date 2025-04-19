from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from the core app!")

def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')