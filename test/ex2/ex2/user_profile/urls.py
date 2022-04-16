from django.urls import path

from ex2.user_profile.views import show_home, show_profile, delete_profile

urlpatterns = (
    path('', show_home, name='home'),
    path('profile/', show_profile, name='profile'),
    path('delete_profile', delete_profile, name='delete profile'),
)
