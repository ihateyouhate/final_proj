from django.urls import include, path
from rest_framework import routers

from .views import (TagViewSet)

router = routers.DefaultRouter()
#router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('tags', TagViewSet, basename='tags')


urlpatterns = [
    path('', include(router.urls)),
]