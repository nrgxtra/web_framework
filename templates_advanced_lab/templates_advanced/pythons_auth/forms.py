from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)


class UserLoginForm(AuthenticationForm):
    user = None
    # email = forms.EmailField()
    # password = forms.CharField(
    #     max_length=30,
    #     widget=forms.PasswordInput(),
    # )

    def clean_password(self):
        super().clean()
        self.user = authenticate(
            email=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError('email and/or password incorrect')

    def save(self):
        return self.user
