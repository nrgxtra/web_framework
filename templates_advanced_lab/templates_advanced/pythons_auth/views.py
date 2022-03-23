from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from templates_advanced.pythons_auth.forms import UserLoginForm, SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign_up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign_in.html', context)


def sign_out(request):
    logout(request)
    return redirect('index')
