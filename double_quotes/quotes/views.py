from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, get_list_or_404

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


def AuthorDetailView(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    # author_quotes =
    template = 'author_detail.html'
    context = {
        'author': author
    }
    return render(request, template, context)
