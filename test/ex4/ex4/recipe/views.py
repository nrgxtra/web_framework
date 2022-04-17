from django.shortcuts import render, redirect

from ex4.core.all_recipes import get_all_recipes
from ex4.recipe.forms import RecipeForm, RecipeEditForm, RecipeDeleteForm
from ex4.recipe.models import Recipe


def show_home(request):
    recipes = get_all_recipes()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = RecipeForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = RecipeEditForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    form = RecipeDeleteForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ing = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ing': ing,
    }
    return render(request, 'details.html', context)
