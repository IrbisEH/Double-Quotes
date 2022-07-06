from django.db import models


class GroupAuthor(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа авторов'
        verbose_name_plural = 'Группы авторов'


class Author(models.Model):
    full_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    group = models.ForeignKey(
        GroupAuthor,
        on_delete=models.CASCADE,
        related_name='authors'
    )

    def __str__(self):
        return self.full_name


class QuoteSource(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='quote_sources'
    )

    def __str__(self):
        return self.title


class Quote(models.Model):
    text = models.TextField()
    source = models.ForeignKey(
        QuoteSource,
        on_delete=models.CASCADE,
        related_name='quotes'
    )
    year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='quotes'
    )

    def __str__(self):
        return self.text[:50]+'...'
