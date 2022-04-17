from ex4.recipe.models import Recipe


def get_all_recipes():
    return Recipe.objects.all()

