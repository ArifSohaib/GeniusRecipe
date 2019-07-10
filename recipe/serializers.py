from rest_framework import serializers
from recipe.models import Recipe, Ingredient, Step
from django.contrib.auth.models import User

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    steps = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    class Meta:
        model = Recipe
        fields = ('id','name', 'writer', 'ingridents', 'steps')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')

class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('id','step_text')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'recipes')
