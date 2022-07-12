from django.urls import path
from .views import *

urlpatterns = [
    path('', get_status),
    path('get-recipes/', get_recipes)
]