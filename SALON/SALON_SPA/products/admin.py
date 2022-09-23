from re import A
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ['name', 'category', 'price']

admin.site.register(Service)
admin.site.register(Categories)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['']
    autocomplete_fields = ['customer']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    autocomplete_fields = ['order', 'product']
    list_display = ['product', 'quantity', 'price', 'total']

    @admin.display(ordering='price')
    def total(self, orderItem):
       return orderItem.quantity * orderItem.price
