from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from templates_advanced.pythons_app.models import Python
from templates_advanced.pythons_auth.forms import UserLoginForm, SignUpForm

UserModel = get_user_model()


# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('sign in')
#     else:
#         form = SignUpForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'auth/sign_up.html', context)


class SignUpView(CreateView):
    template_name = 'auth/sign_up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('sign in')


# def sign_in(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#
#     else:
#         form = UserLoginForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'auth/sign_in.html', context)
class SignInView(LoginView):
    template_name = 'auth/sign_in.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('index')


# def sign_out(request):
#     logout(request)
#     return redirect('index')


class SignOutView(LogoutView):
    next_page = 'goodbye'


class GoodbyeView(ListView):
    model = Python
    template_name = 'auth/goodbye.html'

