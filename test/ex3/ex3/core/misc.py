from ex3.book_app.models import Book
from ex3.profile_app.models import Profile


def get_profile():
    return Profile.objects.first()


def get_books():
    return Book.objects.all()

