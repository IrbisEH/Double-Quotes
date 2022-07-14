from django.forms import ModelForm

from .models import Author, QuoteSource, Quote


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'description', 'link', 'group']


class QuoteSourceForm(ModelForm):
    class Meta:
        model = QuoteSource
        fields = ['title', 'description', 'link', 'author']


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'source', 'year', 'author']
