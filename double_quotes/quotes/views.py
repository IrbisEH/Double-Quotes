from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from core.common.decorators import ajax_required

from .models import Quote, Author, QuoteSource
from .forms import QuoteForm, AuthorForm, QuoteSourceForm


class QuotesListView(ListView):
    model = Quote
    template_name = 'quotes_list.html'


class AuthorsListView(ListView):
    model = Author
    template_name = 'authors_list.html'


def quote_detail(request, id):
    quote = Quote.objects.get(id=id)
    template_name = 'quote_detail.html'
    context = {
        'quote': quote
    }
    return render(request, template_name, context)


class QuoteCreateView(CreateView):
    model = Quote
    template_name = 'quote_create.html'
    success_url = reverse_lazy('quotes:quotes_list')
    fields = ['text', 'source', 'year', 'author']


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    success_url = reverse_lazy('quotes:quotes_list')
    fields = ['full_name', 'image', 'description', 'link', 'group']


class SourceCreateView(CreateView):
    model = QuoteSource
    template_name = 'source_create.html'
    success_url = reverse_lazy('quotes:quotes_list')
    fields = ['title', 'description', 'link', 'author']


def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    author_quotes = Quote.objects.all().filter(author=author)
    sum_of_likes = 0
    # всратый способ посчитать лайки, переделать запрос!!!
    for quote in author_quotes:
        sum_of_likes += quote.like_count
    template = 'author_detail.html'
    context = {
        'author': author,
        'quotes': author_quotes,
        'sum_of_likes': sum_of_likes
    }
    return render(request, template, context)


@ajax_required
@login_required
@require_POST
def add_like(request):
    if request.method == 'POST':
        result = ''
        id = int(request.POST.get('quote_id'))
        quote = get_object_or_404(Quote, id=id)
        if quote.likes.filter(id=request.user.id).exists():
            quote.likes.remove(request.user)
            quote.like_count -= 1
            result = quote.like_count
            quote.save()
        else:
            quote.likes.add(request.user)
            quote.like_count += 1
            result = quote.like_count
            quote.save()
        return JsonResponse({'result': result, })


@ajax_required
@login_required
@require_POST
def add_share(request):
    if request.method == 'POST':
        result = ''
        id = int(request.POST.get('quote_id'))
        quote = get_object_or_404(Quote, id=id)
        if quote.shares.filter(id=request.user.id).exists():
            quote.shares.remove(request.user)
            quote.share_count -= 1
            result = quote.share_count
            quote.save()
        else:
            quote.shares.add(request.user)
            quote.share_count += 1
            result = quote.share_count
            quote.save()
        return JsonResponse({'result': result, })



def create_all_view(request):
    template = 'create_all.html'

    add_quote = False
    add_author = False
    add_source_quote = False

    if request.method == 'POST':
        if 'btn_create_quote' in request.POST:
            quote_form = QuoteForm(request.POST)
            if quote_form.is_valid:
                quote_form.save()
                add_quote = True
            quote_form = QuoteForm
            author_form = AuthorForm
            quote_source_form = QuoteSourceForm
        elif 'btn_create_author' in request.POST:
            author_form = AuthorForm(request.POST)
            if author_form.is_valid:
                author_form.save()
                add_author = True
            quote_form = QuoteForm
            quote_source_form = QuoteSourceForm
        elif 'btn_create_source_quote' in request.POST:
            quote_source_form = QuoteSourceForm(request.POST)
            if quote_source_form.is_valid:
                quote_source_form.save()
                add_source_quote = True
            quote_form = QuoteForm
            author_form = AuthorForm
    else:
        quote_form = QuoteForm()
        author_form = AuthorForm()
        quote_source_form = QuoteSourceForm()

    context = {
        'quote_form': quote_form,
        'author_form': author_form,
        'quote_source_form': quote_source_form,
        'add_quote': add_quote,
        'add_author': add_author,
        'add_source_quote': add_source_quote
    }
    return render(request, template, context)

def check_img(request):
    author = Author.objects.get(id=1)
    template = 'check_img.html'
    context = {
        'author': author
    }
    return render(request, template, context)
