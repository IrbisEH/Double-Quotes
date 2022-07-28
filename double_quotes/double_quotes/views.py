from django.shortcuts import render
from quotes.models import Author


def home_page_view(request):
    authors = Author.objects.all()[:6]
    template = 'home.html'
    context = {
        'authors': authors
    }
    return render(request, template, context)
