from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm

def index(request):
    return render(request, 'index.html')

def employee(request):
    return render(request, 'employee.html')

def calender(request):
    return render(request, 'calender.html')

def schedule(request):
    return render(request, 'schedule.html')

def learning(request):
    return render(request, 'learning.html')

def raport(request):
    return render(request, 'raport.html')

def exam(request):
    return render(request, 'exam.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')
    else:
        form = LoginForm

    return render(request, 'registration/home.html')

def register(request):
    return render(request, 'registration/register.html')