from ex2.notes.models import Note
from ex2.user_profile.models import Profile


def get_profile():
    return Profile.objects.first()


def get_notes():
    return Note.objects.all()
