from django.shortcuts import render
from django.contrib.auth.models import User
from recipe.models import Recipe, Ingredient, Step
from rest_framework import permissions
from rest_framework import viewsets
from recipe.serializers import RecipeSerializer, IngredientSerializer, StepSerializer, UserSerializer
from recipe.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer 

class StepSerializer(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer