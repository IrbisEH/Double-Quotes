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

    def handle(self, *args, **options):

        scripts_dict = {
            'groupauthor_models': add_groupauthor_models,
            'author_models': add_author_models,
            'quotesource_models': add_quotesource_models,
            'quote_models': add_quote_models,
        }

        for name_csv in scripts_dict.keys():
            path = os.path.join(BASE_DIR, f'static/data/{name_csv}.csv')
            script_obj = scripts_dict[name_csv]
            script_obj(path)
