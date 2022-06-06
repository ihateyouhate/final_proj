from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import Recipe
from .models import Follow, User


class ProfileCreateSerializer(UserCreateSerializer):

    class Meta:
        fields = ('email', 'username', 'first_name',
                  'last_name', 'password')
        model = User