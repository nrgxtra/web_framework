from django.urls import path

from ex2.notes.views import add_note, edit_note, details_note, delete_note

urlpatterns = (
    path('add/', add_note, name='note create'),
    path('edit/<int:pk>', edit_note, name='note edit'),
    path('details/<int:pk>', details_note, name='note details'),
    path('delete/<int:pk>', delete_note, name='note delete'),
)

