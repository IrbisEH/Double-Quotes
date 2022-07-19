from django import template

from quotes.models import Quote, Author, QuoteSource


register = template.Library()


@register.simple_tag
def total_quotes():
    total = Quote.objects.count()
    return total


@register.simple_tag
def total_authors():
    total = Author.objects.count()
    return total


@register.simple_tag
def total_quote_sources():
    total = QuoteSource.objects.count()
    return total



