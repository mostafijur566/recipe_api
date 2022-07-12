from rest_framework import serializers
from .models import *


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecommendedSerializer(serializers.ModelSerializer):
    recipe = RecipesSerializer()

    class Meta:
        model = RecommendedRecipe
        fields = '__all__'
