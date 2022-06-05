from django.urls import include, path
from rest_framework import routers

from .views import (TagViewSet, IngredientViewSet)

router = routers.DefaultRouter()
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
]