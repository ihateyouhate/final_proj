from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'color', 'slug')
        model = Tag
        read_only_fields = ('name', 'color', 'slug')