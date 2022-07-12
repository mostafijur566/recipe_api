from django.db import models


# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=False, blank=False)
    cook_time = models.IntegerField()
    ingredients = models.TextField()
    preparation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)