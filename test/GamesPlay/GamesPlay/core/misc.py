from GamesPlay.game.models import Game
from GamesPlay.profile_app.models import Profile


def get_profile():
    return Profile.objects.first()


def get_games():
    return Game.objects.all()


def games_count():
    games = get_games()
    return games.count()


def get_avg_rating():
    games = get_games()
    total_rating = sum(g.rating for g in games)
    avg_rating = total_rating / games.count()
    return avg_rating
