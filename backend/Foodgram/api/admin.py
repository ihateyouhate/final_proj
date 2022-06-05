from django.contrib import admin

from .models import Tag, Ingredient, IngredientAmount


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)


class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'amount', 'recipe')

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)