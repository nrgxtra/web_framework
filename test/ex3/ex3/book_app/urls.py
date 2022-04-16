from django.urls import path

from ex3.book_app.views import show_home, book_add, book_edit, book_details, book_delete

urlpatterns = (
    path('', show_home, name='home'),
    path('add/', book_add, name='add book'),
    path('edit/<int:pk>', book_edit, name='edit book'),
    path('details/<int:pk>', book_details, name='details book'),
    path('delete/<int:pk>', book_delete, name='delete book'),
)
