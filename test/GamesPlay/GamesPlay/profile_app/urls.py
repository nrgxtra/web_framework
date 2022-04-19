from django.urls import path

from GamesPlay.profile_app.views import profile_create, profile_details, profile_edit, profile_delete

urlpatterns = (
    path('create/', profile_create, name='profile create'),
    path('edit/', profile_edit, name='profile edit'),
    path('details/', profile_details, name='profile details'),
    path('delete/', profile_delete, name='profile delete'),
)
