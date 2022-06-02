from django.contrib import admin

from .models import Tag, Ingredient


class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'color', 'slug')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)