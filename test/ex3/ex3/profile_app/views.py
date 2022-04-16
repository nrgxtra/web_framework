from django.shortcuts import render, redirect

from ex3.core.misc import get_profile, get_books
from ex3.profile_app.forms import ProfileForm, EditProfileForm, DeleteProfileForm


def create_profile(request):
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


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    books = get_books()
    if request.method == 'POST':
        books.delete()
        profile.delete()
        return redirect('home')
    form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)

