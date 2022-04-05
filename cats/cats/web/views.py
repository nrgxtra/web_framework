from django.shortcuts import render
from django.urls import reverse_lazy

from cats.common.bootstrap_mixins import BootstrapFormViewMixin
from cats.web.models import Cat
from django.views.generic import TemplateView, ListView, CreateView


# def index(request):
#     return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'CBV',
        }


class CreateCat(BootstrapFormViewMixin, CreateView):
    model = Cat
    template_name = 'create_cat.html'
    fields = '__all__'
    success_url = reverse_lazy('show cats')


# def show_cats(request):
#     cats = Cat.objects.all()
#     context = {
#         'cats': cats,
#     }
#     return render(request, 'cats.html', context)


class ShowCatsListView(ListView):
    model = Cat
    template_name = 'cats.html'
    context_object_name = 'cats'
