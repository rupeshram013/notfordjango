from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Register
from .forms import RegisterForm
from django.contrib import messages

def home(request):
    context = {}
    return render(request, 'index.html', context)

def login_user(request):
    pass

def register_user(request):
    register = RegisterForm()

    if request.method == 'POST':
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')
        form = RegisterForm(request.POST)
        if form.is_valid():
            if pass1 == pass2:
                Register.objects.create(
                    username = request.POST.get('username'),
                    email = request.POST.get('email'),
                    password = pass1,
                    confirm_password = pass2,
                )
            else:
                messages.error(request, 'The Passwords doesnot match. Please try again!')
        else:
            messages.error(request, 'Error occured during registration')

    return render(request, 'register.html', {'register': register})