from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm

def index(request):
    return render(request, 'index.html')

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