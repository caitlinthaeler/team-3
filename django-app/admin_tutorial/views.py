from django.shortcuts import render, redirect
from django.http import HttpResponse

def make_admin_tutorial(request):
    return redirect('admin_tutorial')