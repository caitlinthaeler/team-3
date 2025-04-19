from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from django.contrib.auth.models import Group
from django.urls import reverse

def select_login_role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if role == 'teacher' and user.groups.filter(name='Teacher').exists():
                return redirect('teacher_dashboard')
            elif role == 'student' and user.groups.filter(name='Student').exists():
                return redirect('student_dashboard')
            else:
                return HttpResponse("You don't have permission for this role.")
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'select_login_role.html')
