from django.shortcuts import render, redirect

from ex5.core.mics import get_profile, get_albums, get_albums_count
from ex5.profile_app.forms import ProfileForm


def show_home(request):
    profile = get_profile()
    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            form = ProfileForm(request.POST)
            errors = form.errors
            context = {
                'form': form,
                'errors': errors,
            }
            return render(request, 'home-no-profile.html', context)
        form = ProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)
    albums = get_albums()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def profile_details(request):
    if request.method == 'GET':
        profile = get_profile()
        albums_count = get_albums_count()
        context = {
            'profile': profile,
            'albums_count': albums_count,
        }
        return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    albums = get_albums()
    if request.method == 'POST':
        albums.delete()
        profile.delete()
        return redirect('home')
    return render(request, 'profile-delete.html')

