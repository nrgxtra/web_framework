from django.urls import path
from . import views
from .views import IndexView, PythonCreateView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('create/', PythonCreateView.as_view(), name="create"),
]
