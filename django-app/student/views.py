from django.shortcuts import render
from django.http import HttpResponse
from admin_route.views import saved_tutorials  # Import the saved_tutorials list from admin_route/views.py

def home(request):
    return render(request, 'homePage.html')

def chat(request):
    return render(request, 'chatPage.html')

def game(request):
    return render(request, 'gamePage.html')

def task(request):
    return render(request, 'taskPage.html')

def settings(request):
    return render(request, 'settingsPage.html')

def tutorial(request):
    return render(request, 'tutorialPage.html', {'saved_tutorials': saved_tutorials})
