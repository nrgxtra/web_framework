from django.urls import path

from ex5.profile_app.views import show_home, profile_details, profile_delete

urlpatterns = (
    path('', show_home, name='home'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
)
