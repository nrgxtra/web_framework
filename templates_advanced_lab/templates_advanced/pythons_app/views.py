from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .core.mixins import GroupRequiredMixin
from .forms import PythonCreateForm
from .models import Python


# def index(req):
#     pythons = Python.objects.all()
#     return render(req, 'index.html', {'pythons': pythons})


class IndexView(ListView):
    model = Python
    template_name = 'index.html'
    context_object_name = 'pythons'


# @login_required
# def create(req):
#     if req.method == 'GET':
#         form = PythonCreateForm()
#         return render(req, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(req.POST, req.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         return render(req, 'create.html', {'form': form})


class PythonCreateView(GroupRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Python
    fields = '__all__'
    success_url = reverse_lazy('index')



