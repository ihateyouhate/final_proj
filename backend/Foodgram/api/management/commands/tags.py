from csv import reader

from django.core.management.base import BaseCommand
from api.models import Tag


class Command(BaseCommand):
    help = 'Upload csv tags to django-models'

    def handle(self, *args, **kwargs):
        with open('data/tags.csv', 'r', encoding='utf-8') as tag:
            for row in reader(tag):
                if len(row) == 3:
                    Tag.objects.get_or_create(
                        name=row[0], color=row[1], slug=row[2])
