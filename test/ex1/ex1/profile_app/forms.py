from django import forms

from ex1.profile_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileEditForm(ProfileForm):
    pass


class ProfileDeletionForm(ProfileForm):
    pass

