from ex5.albums.models import Album
from ex5.profile_app.models import Profile


def get_profile():
    return Profile.objects.first()


def get_albums():
    return Album.objects.all()


def get_albums_count():
    albums = get_albums()
    return albums.count()

