from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    writer = models.OneToOneField('auth.User', related_name='recipes', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} by {self.writer}"

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    def __str__(self):
        return f"{self.name}"

class Step(models.Model):
    recpie = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)
    step_text = models.TextField(blank=False)