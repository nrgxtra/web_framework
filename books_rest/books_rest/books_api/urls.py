from django.urls import path

from books_rest.books_api.views import BookListCreate, BookGetUpdateDelete

urlpatterns = (
    path('books/', BookListCreate.as_view(), name='book list create'),
    path('books/<int:pk>',BookGetUpdateDelete.as_view(), name='update delete'),
)
