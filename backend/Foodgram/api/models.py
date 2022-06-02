from django.contrib.auth import get_user_model
from django.db import models

from .validators import validate_nums

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=7, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    measurement_unit = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe')
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/')
    tags = models.ManyToManyField(Tags)
    cooking_time = models.PositiveIntegerField(validators=[validate_nums])