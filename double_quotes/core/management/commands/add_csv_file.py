import os
from django.core.management.base import BaseCommand

from double_quotes.settings import BASE_DIR

from ._add_models_scripts import (
    add_groupauthor_models,
    add_author_models,
    add_quotesource_models,
    add_quote_models
)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name_csv', type=str, help=' Укажите название файла')

    def handle(self, *args, **options):

        name_csv = options['name_csv']
        path = os.path.join(BASE_DIR, f'static/data/{name_csv}.csv')

        scripts_dict = {
            'groupauthor_models': add_groupauthor_models,
            'author_models': add_author_models,
            'quotesource_models': add_quotesource_models,
            'quote_models': add_quote_models,
        }

        script_obj = scripts_dict[name_csv]
        script_obj(path)

