from django.contrib import admin

from .models import (
        Author,
        GroupAuthor,
        QuoteSource,
        Quote
)

admin.site.register(Author)
admin.site.register(GroupAuthor)
admin.site.register(QuoteSource)
admin.site.register(Quote)