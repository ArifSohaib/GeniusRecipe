from rest_framework import serializers
from recipe.models import Recipe, Ingredient, Step
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
    recipes_ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    recipes_steps = serializers.PrimaryKeyRelatedField(many=True, queryset=Step.objects.all())
    class Meta:
        model = Recipe
        fields = ('url','id','name', 'writer', 'recipes_ingredients', 'recipes_steps')
    

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('url','id', 'name',)

class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('url', 'id','step_text',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    class Meta:
        model = User 
        fields = ('url','id', 'username', 'first_name', 'last_name', 'email', 'recipes')
