from django.db import models
from users.models import User

class GroupAuthor(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа авторов'
        verbose_name_plural = 'Группы авторов'


class Author(models.Model):
    full_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)

    group = models.ForeignKey(
        GroupAuthor,
        on_delete=models.CASCADE,
        related_name='authors',
    )
    image = models.ImageField(upload_to='images/authors/', blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


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

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'


class Quote(models.Model):
    text = models.TextField(unique=True)
    source = models.ForeignKey(
        QuoteSource,
        on_delete=models.CASCADE,
        related_name='source_quotes'
    )
    year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='author_quotes'
    )
    likes = models.ManyToManyField(
        User,
        related_name='like',
        default=None,
        blank=True,
    )
    like_count = models.BigIntegerField(default='0')
    shares = models.ManyToManyField(
        User,
        related_name='share',
        default=None,
        blank=True,
    )
    share_count = models.BigIntegerField(default='0')
    created = models.DateTimeField(
        auto_now_add=True
    )

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.text[:50]+'...'

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
        ordering = ('-created',)
