from django.contrib import admin

from .models import Product, Brand, Category

# Register your models here.
admin.site.register([Brand, Category])

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'base_quantity')