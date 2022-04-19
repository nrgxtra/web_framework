from django.shortcuts import render, redirect

from GamesPlay.game.forms import GameForm, GameDeletionForm
from GamesPlay.game.models import Game


def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        form = GameForm(request.POST)
        context = {
            'form': form,
        }
        return render(request, 'create-game.html', context)
    form = GameForm()
    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context)


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }
    return render(request, 'details-game.html', context)


def game_edit(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        form = GameForm(request.POST, instance=game)
        context = {
            'form': form,
            'game': game,
        }
        return render(request, 'edit-game.html', context)
    form = GameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')
    form = GameDeletionForm(instance=game)
    context = {
        'game': game,
        'form': form,
    }
    return render(request, 'delete-game.html', context)
