import csv

from quotes.models import (
    GroupAuthor,
    Author,
    QuoteSource,
    Quote
)


def add_groupauthor_models(path):
    print('add_groupauthor_models script in progress')
    with open(path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            group = GroupAuthor.objects.create(
                id=row[0],
                title=row[1],
                slug=row[2],
            )
            print(f'{group.title} add to DB')
        print('add_groupauthor_models script done')


def add_author_models(path):
    print('add_author_models script in progress')
    with open(path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            group = GroupAuthor.objects.get(id=row[4])
            author = Author.objects.create(
                id=row[0],
                full_name=row[1],
                description=row[2],
                link=row[3],
                group=group
            )
            print(f'{author.full_name} add to DB')
        print('add_author_models script done')


def add_quotesource_models(path):
    print('add_quotesource_models script in progress')
    with open(path, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            author = Author.objects.get(id=row[4])
            quotesource = QuoteSource.objects.create(
                id=row[0],
                title=row[1],
                description=row[2],
                link=row[3],
                author=author,
            )
            print(f'{quotesource.title} add to DB')
        print('add_quote_models script done')


def add_quote_models(path):
    print('add_quote_models script in progres')
    with open(path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            author = Author.objects.get(id=row[5])
            source = QuoteSource.objects.get(id=row[2])
            quote = Quote.objects.create(
                id=row[0],
                text=row[1],
                source=source,
                year=row[4],
                author=author
            )
            print(f'{quote.id} add to DB')
        print('add_quote_models script done')