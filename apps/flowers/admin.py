from django.contrib import admin
from .models import Flower, Category, Color, Price, Ingredient


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'price')


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Price)
admin.site.register(Ingredient)