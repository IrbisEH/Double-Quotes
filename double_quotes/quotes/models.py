from django.db import models


class GroupAuthor(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа авторов'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    group = models.ForeignKey(
        GroupAuthor,
        on_delete=models.CASCADE,
        related_name='authors'
    )

    def __str__(self):
        return self.last_name


class QuoteSource(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    link = models.URLField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='quote_sources'
    )


class Quote(models.Model):
    text = models.TextField()
    source = models.ForeignKey(
        QuoteSource,
        on_delete=models.CASCADE,
        related_name='quotes'
    )
    date = models.DateField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='quotes'
    )

    def __str__(self):
        return self.text[:15]
