from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


# Create your views here.

@api_view(['GET'])
def get_status(request):
    return Response(
        {
            "status": 200,
            "message": "yes! django is working"
        }
    )


@api_view(['GET'])
def get_recipes(request):
    recipe = Recipe.objects.all()
    serializer = RecipesSerializer(recipe, many=True)

    return Response(
        {
            "total_recipe": recipe.count(),
            "recipes": serializer.data
        }
    )


@api_view(['GET'])
def get_recommended_recipe(request):
    recommended = RecommendedRecipe.objects.all()
    serializer = RecommendedSerializer(recommended, many=True)

    return Response({
        "total_recipe": recommended.count(),
        "recommended": serializer.data
    })
