from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets,
    }
    return render(request, 'templates/pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    is_liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()

    # can_edit = pet.user == request.user
    # can_delete = pet.user == request.user
    is_owner = pet.user == request.user

    context = {
        'pet': pet,
        'is_owner': is_owner,
        'is_liked': is_liked_by_user,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk
            }
        ),
        'comments': pet.comment_set.all(),

    }
    return render(request, 'templates/pets/pet_detail.html', context)


@login_required
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    is_already_liked_by_user = pet.like_set.filter(user_id=request.user.id).first()
    if is_already_liked_by_user:
        is_already_liked_by_user.delete()
    else:
        like = Like(
            pet=pet,
            user=request.user,
        )
        like.save()
    return redirect('pet details', pet.id)


@login_required
def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('list pets')
        context = {
            'form': form,
        }
        return render(request, 'templates/pets/pet_create.html', context)
    else:
        context = {
            'form': PetForm()
        }
        return render(request, 'templates/pets/pet_create.html', context)


@login_required
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = EditPetForm(instance=pet)
        context = {
            'form': form,
            'pet': pet
        }
        return render(request, 'templates/pets/pet_edit.html', context)


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }
        return render(request, 'templates/pets/pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


# def comment_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             comment=form.cleaned_data['comment'],
#             pet=pet,
#         )
#         comment.save()
#     return redirect('pet details', pet.id)
@login_required
def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
    return redirect('pet details', pk)
