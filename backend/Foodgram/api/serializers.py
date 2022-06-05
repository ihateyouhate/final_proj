from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from .models import Tag, Ingredient, IngredientAmount, Recipe

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'color', 'slug')
        model = Tag
        read_only_fields = ('name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'measurement_unit')
        model = Ingredient


class IngredientAmountSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit')

    class Meta:
        fields = ('id', 'ingredient', 'amount', 'recipe')
        model = IngredientAmount


class AddIngredientSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    amount = serializers.IntegerField()

    class Meta:
        model = IngredientAmount
        fields = ('id', 'amount')


class RecipeSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    ingredients = AddIngredientSerializer(many=True)
    tags =  serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True)
    #author

    class Meta:
        fields = (
            'id', 'author', 'name', 'text', 'image', 'ingredients',
            'tags', 'cooking_time')
        read_only_fields = ('author',)
        model = Recipe