from django.contrib import admin

from . models import (Customer, Product, Card, OrderPlaced)

# Register your models here.
@admin.register(Customer)
class CustomerModalAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'division','district','thana', 'villorroad', 'zipCode']