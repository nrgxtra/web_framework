from django.shortcuts import render, redirect

from ex3.book_app.forms import BookForm, BookEditForm
from ex3.book_app.models import Book
from ex3.core.misc import get_profile
from ex3.profile_app.forms import ProfileForm


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    books = Book.objects.all()

    context = {
        'books': books,
        'profile': profile,
    }
    return render(request, 'home-with-profile.html', context)


def book_add(request):
    profile = get_profile()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = BookForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-book.html', context)


def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = BookEditForm(instance=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'book-details.html', context)


def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')
