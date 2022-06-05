from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
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

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe')
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/')
    tags = models.ManyToManyField(Tag)
    cooking_time = models.PositiveIntegerField(validators=[validate_nums])


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(
            1, message='Ингредиенты должны быть больше нуля'
        )]
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ingredient', 'recipe'],
                name='unique_ingredient_recipe'
            )
        ]