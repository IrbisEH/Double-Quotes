from django.urls import path

from . import views
from .views import (
    QuotesListView,
    QuoteCreateView,
    AuthorCreateView,
    SourceCreateView,
    create_all_view,
)


app_name = 'quotes'

urlpatterns = [
    path('list/', QuotesListView.as_view(), name='quotes_list'),
    path('quote/<int:id>/', views.quote_detail, name='quote_detail'),
    path('author/<int:id>/', views.author_detail, name='author_detail'),
    path('create/', create_all_view, name='create_all'),
    path('quote_create/', QuoteCreateView.as_view(), name='quote_create'),
    path('author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('source_create/', SourceCreateView.as_view(), name='source_create'),
]
