from django.urls import path
from .views import *

urlpatterns = [
    path('', get_status),
    path('api/v1/recipes/', get_recipes),
    path('api/v1/recommended/', get_recommended_recipe)
]