from django.urls import path

from ex3.profile_app.views import show_profile, edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', show_profile, name='show profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
    path('create/', create_profile, name='create profile')
)
