from django.shortcuts import render, redirect

from GamesPlay.core.misc import get_profile, games_count, get_avg_rating, get_games
from GamesPlay.profile_app.forms import ProfileForm, ProfileDeletionForm


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        form = ProfileForm(request.POST)
        context = {
            'form': form,
        }
        return render(request, 'create-profile.html', context)
    form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    all_games = games_count()
    avg_rating = get_avg_rating()
    context = {
        'profile': profile,
        'all_games': all_games,
        'avg_rating': avg_rating,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
        form = ProfileForm(request.POST, instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'edit-profile.html', context)
    form = ProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    games = get_games()
    if request.method == 'POST':
        games.delete()
        profile.delete()
        return redirect('home')
    form = ProfileDeletionForm(instance=profile)
    context = {
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)

