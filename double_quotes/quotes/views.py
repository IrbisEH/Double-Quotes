from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

from .models import Quote, Author, QuoteSource


class QuotesListView(ListView):
    model = Quote
    template_name = 'quotes_list.html'


class QuoteCreateView(CreateView):
    model = Quote
    template_name = 'quote_create.html'
    success_url = reverse_lazy('quotes:quotes_list')
    fields = ['text', 'source', 'year', 'author']


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    success_url = reverse_lazy('qoutes:quotes_list')
    fields = ['full_name', 'description', 'link', 'group']


class SourceCreateView(CreateView):
    model = QuoteSource
    template_name = 'source_create.html'
    success_url = reverse_lazy('quotes:quotes_list')
    fields = ['title', 'description', 'link', 'author']
