from django.views.generic import ListView

from .models import Quote


class QuotesListView(ListView):
    model = Quote
    template_name = 'quotes_list.html'
