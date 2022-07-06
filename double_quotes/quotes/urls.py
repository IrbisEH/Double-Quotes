from django.urls import path

from .views import QuotesListView, QuoteCreateView, AuthorCreateView, SourceCreateView


app_name = 'quotes'

urlpatterns = [
    path('list/', QuotesListView.as_view(), name='quotes_list'),
    path('quote_create/', QuoteCreateView.as_view(), name='quote_create'),
    path('author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('source_create/', SourceCreateView.as_view(), name='source_create')
]
