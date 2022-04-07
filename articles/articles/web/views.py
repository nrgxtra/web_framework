from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as view
from django.views.generic.detail import SingleObjectMixin

from articles.web.models import Article, Source


class ArticleCreateView(view.CreateView):
    model = Article
    template_name = 'web/create-article.html'
    success_url = reverse_lazy('index')
    fields = '__all__'


class SourceCreateView(view.CreateView):
    model = Source
    template_name = 'web/create-source.html'
    # success_url = reverse_lazy('index')
    fields = '__all__'

    def get_success_url(self):
        return reverse('details source', kwargs={
            'pk': self.object.id,
        })


class ArticlesListView(view.ListView):
    model = Article
    template_name = 'web/list-articles.html'
    context_object_name = 'articles'


class SourceDetailView(SingleObjectMixin, view.ListView):
    model = Source
    object = None
    template_name = 'web/details-source.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Source.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = self.object
        return context

    def get_queryset(self):
        return self.object.article_set.all()


class SourcesListView(view.ListView):
    model = Source
    template_name = 'web/list-sources.html'
    context_object_name = 'sources'
