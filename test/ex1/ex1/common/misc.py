from ex1.expense_app.models import Expense
from ex1.profile_app.models import Profile


def get_profile():
    return Profile.objects.first()


def get_budget_left():
    user = Profile.objects.first()
    expenses = Expense.objects.all()
    result = user.budget - sum([ex.price for ex in expenses])
    return result


