from django.contrib import admin

from .models import Tags, Ingredients


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'color', 'slug')


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)

admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Tags, TagsAdmin)