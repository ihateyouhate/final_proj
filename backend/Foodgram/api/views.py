from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Ingredient, Tag, Recipe
from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer
from .pagination import CustomPagination

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (AllowAny,)


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = (AllowAny, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    pagination_class = CustomPagination
    #permission_classes = (AllowAny, )
    serializer_class = RecipeSerializer

    #def get_serializer_class(self):
        #if self.action in ('list', 'retrieve'):
            #return RecipeListSerializer
        #return RecipeSerializer
