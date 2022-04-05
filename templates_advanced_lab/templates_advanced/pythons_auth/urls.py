from django.urls import path

from templates_advanced.pythons_auth.views import SignUpView, SignInView, SignOutView, GoodbyeView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('goodbye/', GoodbyeView.as_view(), name='goodbye'),
)
