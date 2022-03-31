from django.urls import path

from petstagram.accounts.views import login_user, register, logout_user, profile_details

urlpatterns = (
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profiles/', profile_details, name='profile details'),
)
