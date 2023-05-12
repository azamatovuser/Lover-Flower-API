from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'ordering', 'city', 'street', 'time_ordering', 'pay')
    date_hierarchy = 'time_ordering'