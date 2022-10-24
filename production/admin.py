from django.contrib import admin

from .models import Product, Brand, Category

# Register your models here.
admin.site.register([Product, Brand, Category])