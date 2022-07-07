from django.contrib import admin

from .models import (
    Author,
    GroupAuthor,
    QuoteSource,
    Quote
)


@admin.register(GroupAuthor)
class GroupAuthor(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    # search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'group')
    # search_fields = ('full_name',)
    ordering = ('full_name',)


@admin.register(QuoteSource)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)
    # search_fields = ('title', 'author')
    ordering = ('title',)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'source', 'year', 'author',)
    list_filter = ('source', 'year', 'author',)
    # search_fields
    # date_hierarchy = 'year' сначала исправить модель на DateTimeField
    ordering = ('text', 'author',)
