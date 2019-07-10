from rest_framework import serializers
from recipe.models import Recipe, Ingredient, Step

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
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