"""
This file script should be imported in the ready()
method in apps.py file
For ensuring to be recognizable by the server
"""


from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from rest_framework import exceptions
from .models import Order, OrderItem



@receiver(pre_delete, sender=Order)
def increment_quantity(sender, instance, **kwargs):
    """Increment items quantity after deleting an order"""

    # Get all related items with the order
    order_items = OrderItem.objects.filter(order=instance)

    # Iterate on each Product to increase the quantity
    for order_item in order_items:
        # item = Product.objects.get(id=order_item.item)
        order_item.item.base_quantity += order_item.consume_quantity
        order_item.item.save()

@receiver(post_save, sender=OrderItem)
def decrement_quantity(sender, instance, **kwargs):
    """Decrement items quantity after creating an order"""


    item = instance.item
    """Decrease the base quantity of the item"""
    new_quantity = item.base_quantity - instance.consume_quantity

    # Abort process if the available quantity bellow 0 value
    if(new_quantity < 0):
        raise exceptions.ValidationError(f"You exceed the number of available for the {item}:{item.base_quantity}")
        
    item.base_quantity = new_quantity
    item.save()

    
    
