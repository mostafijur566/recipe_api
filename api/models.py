from django.db import models


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=False, blank=False)
    cook_time = models.IntegerField()
    ingredients = models.TextField()
    preparation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[0:50]

    class Meta:
        ordering = ['-updated_at']


class RecommendedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recipe.name[0:50]

    class Meta:
        ordering = ['-updated_at']
