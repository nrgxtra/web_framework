from django.urls import path

from ex4.recipe.views import show_home, create_recipe, edit_recipe, delete_recipe, recipe_details

urlpatterns = (
    path('', show_home, name='home'),
    path('create/', create_recipe, name='create'),
    path('edit/<int:pk>', edit_recipe, name='edit'),
    path('delete/<int:pk>', delete_recipe, name='delete'),
    path('details/<int:pk>', recipe_details, name='details'),
)
