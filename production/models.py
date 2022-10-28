from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from rest_framework import exceptions


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})
    
class Brand(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Brand_detail", kwargs={"pk": self.pk})



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    base_quantity = models.IntegerField()
    category = models.ForeignKey("Category", related_name='product_categories', on_delete=models.SET_NULL, null=True, blank=True)
    brands = models.ForeignKey("Brand", related_name='product_brands', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("production:product-detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    def is_available(self, consume_quantity:int):
        diff = self.base_quantity - consume_quantity

        # Abort process if the available quantity bellow 0 value
        if(diff < 0):
            raise exceptions.ValidationError(f"You exceed the number of available for the {self.name}:{self.base_quantity} / should be {diff} or les")
    


