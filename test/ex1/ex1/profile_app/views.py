from django.shortcuts import render, redirect

from ex1.common.misc import get_profile, get_budget_left
from ex1.expense_app.models import Expense
from ex1.profile_app.forms import ProfileEditForm


def profile_details(request):
    user = get_profile()
    budget_left = get_budget_left()
    context = {
        'profile': user,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ProfileEditForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    if request.method == 'POST':
        profile.delete()
        expenses.delete()
        return redirect('home')
    return render(request, 'profile-delete.html')
