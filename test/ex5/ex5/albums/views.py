from django.shortcuts import render, redirect

from ex5.albums.forms import AlbumForm, AlbumDeletionForm
from ex5.albums.models import Album


def album_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        form = AlbumForm(request.POST)
        context = {
            'form': form,
        }
        return render(request, 'add-album.html', context)
    form = AlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
        form = AlbumForm(request.POST, instance=album)
        context = {
            'form': form,
            'album': album,
        }
        return render(request, 'edit-album.html', context)
    form = AlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('home')
    form = AlbumDeletionForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'delete-album.html', context)

