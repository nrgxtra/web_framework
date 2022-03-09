from django.urls import path

from phones_media_files.phones.views import index, add_phone

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_phone, name='add'),
    # path('image/', add_image, name='add image'),
)
