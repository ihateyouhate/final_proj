from django.core.validators import MinValueValidator
from django.db import models

from users.models import User
from .validators import ingred_nums, validate_nums


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
        User, on_delete=models.CASCADE, related_name='recipes')
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    ingredients = models.ManyToManyField(
        Ingredient, through='IngredientAmount')
    tags = models.ManyToManyField(Tag)
    cooking_time = models.PositiveIntegerField(validators=[validate_nums])

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[ingred_nums])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ingredient', 'recipe'],
                name='unique_ingredient_recipe'
            )
        ]


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='fav_user')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorite')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_user_recipe'
            )
        ]


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shopping_carts')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='shopping_carts')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shop_user_recipe'
            )
        ]
