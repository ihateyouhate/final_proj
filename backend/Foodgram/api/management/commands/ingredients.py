from csv import reader

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Upload csv ingredients to django-models'

    def handle(self, *args, **kwargs):
        with open(
            'data/ingredients.csv', 'r', encoding='UTF-8') as ingredient:
            for row in reader(ingredient):
                if len(row) == 2:
                    Ingredient.objects.get_or_create(
                        name=row[0], measurement_unit=row[1])
