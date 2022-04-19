from django.shortcuts import render

from GamesPlay.core.misc import get_profile, get_games


def show_home(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


def show_dashboard(request):
    games = get_games()
    context = {
        'games': games,
    }
    return render(request, "dashboard.html", context)

