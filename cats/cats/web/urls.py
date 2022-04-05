from django.urls import path

from cats.web.views import IndexView, ShowCatsListView, CreateCat

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('cats/', ShowCatsListView.as_view(), name='show cats'),
    path('create/', CreateCat.as_view(), name='create cat'),
)
