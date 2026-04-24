from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

class DietaryTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    dietary_tags = models.ManyToManyField(DietaryTag, related_name='recipes', blank=True)
    instructions = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Nutritional Information
    calories = models.PositiveIntegerField(null=True, blank=True, help_text="Calories per serving")
    protein = models.PositiveIntegerField(null=True, blank=True, help_text="Protein (g) per serving")
    carbs = models.PositiveIntegerField(null=True, blank=True, help_text="Carbs (g) per serving")
    fat = models.PositiveIntegerField(null=True, blank=True, help_text="Fat (g) per serving")

    
    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if not ratings:
            return 0
        return sum(r.score for r in ratings) / len(ratings)

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    
    class Meta:
        unique_together = ('recipe', 'user')

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

