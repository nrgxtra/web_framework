from django.shortcuts import render, redirect

from core.misc import get_profile, get_notes
from ex2.user_profile.forms import ProfileForm


def show_home(request):
    profile = get_profile()
    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        form = ProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)

    notes = get_notes()
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def show_profile(request):
    profile = get_profile()
    notes = get_notes()
    notes_count = notes.count()
    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = get_notes()
    notes.delete()
    profile.delete()
    return redirect('home')
