from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    base_quantity = models.IntegerField()

    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Items")

    def __str__(self):
        return self.name


