from django import forms

from ex3.book_app.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookEditForm(BookForm):
    pass


class BookDeleteForm(BookForm):
    pass
