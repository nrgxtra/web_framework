from django.urls import path

from GamesPlay.home_app.views import show_home, show_dashboard

urlpatterns = (
    path('', show_home, name='home'),
    path('dashboard/', show_dashboard, name='dashboard'),
)
