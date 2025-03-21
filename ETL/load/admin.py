from django.contrib import admin
from .models import Customer, Product, Order



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'name', 'email', 'location')
    search_fields = ('name', 'email', 'location')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'category', 'price')
    search_fields = ('name', 'category')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'product', 'order_date', 'quantity', 'total_amount')
    search_fields = ('customer__name', 'product__name', 'order_date')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)