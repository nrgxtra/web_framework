from django.shortcuts import render, redirect

from ex1.common.misc import get_profile, get_budget_left
from ex1.expense_app.forms import CreateExpenseForm, EditExpenseForm, DeleteExpenseForm
from ex1.expense_app.models import Expense
from ex1.profile_app.forms import ProfileForm


def show_home(request):
    user = get_profile()
    if not user:
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
    expenses = Expense.objects.all()
    budget_left = get_budget_left()
    context = {
        'expenses': expenses,
        'profile': user,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateExpenseForm()
    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = EditExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('home')
    form = DeleteExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)
