from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Scale(models.Model):
    name = models.CharField(max_length=63)
    shortName = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class IngredientCategory(models.Model):
    name = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=63)
    category = models.ForeignKey(IngredientCategory, blank=True, null=True)
    scale = models.ForeignKey(Scale)

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    name = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=63, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(blank=True)
    preparationTime = models.IntegerField(blank=True, default=0)
    cookingTime = models.IntegerField(blank=True, default=0)
    price = models.IntegerField(blank=True)
    category = models.ManyToManyField(MealCategory, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return self.name
