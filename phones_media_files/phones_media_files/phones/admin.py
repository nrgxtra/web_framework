from django.contrib import admin

from phones_media_files.phones.models import Phone, PhoneImage


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model']


@admin.register(PhoneImage)
class ImageAdmin(admin.ModelAdmin):
    pass
