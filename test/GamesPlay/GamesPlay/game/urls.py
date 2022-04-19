from django.urls import path

from GamesPlay.game.views import game_create, game_edit, game_delete, game_details

urlpatterns = (
    path('create/', game_create, name='game create'),
    path('details/<int:pk>', game_details, name='game details'),
    path('edit/<int:pk>', game_edit, name='game edit'),
    path('delete/<int:pk>', game_delete, name='game delete'),
)

