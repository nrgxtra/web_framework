from django.urls import path

from ex1.profile_app.views import profile_details, profile_edit, profile_delete

urlpatterns = (
    path('', profile_details, name='profile details'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
)
