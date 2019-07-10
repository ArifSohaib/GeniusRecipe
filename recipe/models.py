from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    writer = models.ForeignKey('auth.User', related_name='recipes', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} by {self.writer}"
    def save(self, *args, **kwargs):
        super(Recipe, self).save(*args, **kwargs)

class Ingredient(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    recipie = models.ForeignKey(Recipe, related_name='recipes_ingredients', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"

class Step(models.Model):
    recipie = models.ForeignKey(Recipe, related_name='recipes_steps', on_delete=models.CASCADE, null=True)
    step_text = models.TextField(blank=False)
    def __str__(self):
        return f"{self.step_text}"


