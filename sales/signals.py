"""
This file script should be imported in the ready()
method in apps.py file
For ensuring to be recognizable by the server
"""


from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Order
from .dataclasses import OrderService



@receiver(pre_delete, sender=Order)
def increment_quantity(sender, instance, **kwargs):
    OrderService(order=instance).increment_quantity()
    
    
