from django.shortcuts import render, redirect
from django.http import HttpResponse

def select_login_role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Hardcoded credentials
        teacher_username = 'teacher'
        teacher_password = '1'

        student_username = 'student'
        student_password = '1'

        if role == 'teacher' and username == teacher_username and password == teacher_password:
            return redirect('teacher_dashboard')
        elif role == 'student' and username == student_username and password == student_password:
            return redirect('student_dashboard')
        else:
            return HttpResponse("Invalid credentials or role.")

    return render(request, 'select_login_role.html')
