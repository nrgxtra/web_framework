from django import forms

from phones_media_files.phones.models import Phone, PhoneImage


class CreatePhone(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"


class AddImage(forms.ModelForm):
    class Meta:
        model = PhoneImage
        fields = ('image', 'is_selected', 'phone')
