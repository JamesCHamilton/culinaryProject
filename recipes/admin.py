from django.contrib import admin
from .models import Country, Ingredient, Recipe, DietaryTag

@admin.register(DietaryTag)
class DietaryTagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Country)

class CountryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'author', 'created_at')
    list_filter = ('country', 'author', 'dietary_tags')
    search_fields = ('title', 'ingredients__name', 'dietary_tags__name')
    filter_horizontal = ('ingredients', 'dietary_tags')
