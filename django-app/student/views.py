from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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
    return render(request, 'tutorialPage.html')