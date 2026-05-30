from django.contrib import admin

from . models import (Customer, Product, Card, OrderPlaced)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'division','district','thana', 'villorroad', 'zipCode']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price','description','brand', 'category', 'product_image']



@admin.register(Card)
class CardModelAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'product', 'quantity']



@admin.register(OrderPlaced)
class OrderPacedModelAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'Customer', 'product','quantity','quantity', 'status']