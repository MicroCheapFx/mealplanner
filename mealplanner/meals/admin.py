from django.contrib import admin

from . import models

# Register your models here.


#class MealAdmin(admin.ModelAdmin):
#    list_display = ('',)
#
#admin.site.register(Meal, MealAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Scale)
admin.site.register(models.IngredientCategory)
admin.site.register(models.Ingredient)
admin.site.register(models.MealCategory)
admin.site.register(models.Meal)
