from django import forms

from GamesPlay.profile_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeletionForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
