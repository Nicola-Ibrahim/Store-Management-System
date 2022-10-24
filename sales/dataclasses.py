import dataclasses
from .models import Order, OrderItem
from production.models import Product
from rest_framework import exceptions

@dataclasses.dataclass
class SoldItemDetail:
    item: Product
    consume_quantity: float
    discount: float 

@dataclasses.dataclass
class OrderService:

    order: Order

    def link(self, sold_items: list[SoldItemDetail]):
        """Link items instance to the specific order"""


        def _decrement_quantity(item, quan:int):
            """Decrease the base quantity of the item"""
            new_quantity = item.base_quantity - quan
            if(new_quantity < 0):
                raise exceptions.ValidationError(f"You exceed the number of available for the {item}:{item.base_quantity}")
            item.base_quantity = new_quantity
            item.save()


        for sold_item in sold_items:
            # Create instance in the OrderItem table
            OrderItem.objects.create(
                    order=self.order, 
                    item=sold_item.item,
                    consume_quantity=sold_item.consume_quantity,
                    discount=sold_item.discount
                )

            # Subtract the base number of quantity from the item

            _decrement_quantity(sold_item.item, sold_item.consume_quantity)


    def increment_quantity(self):
        # Get all related items with the order

        order_items = OrderItem.objects.filter(order=self.order)

        # Iterate on each Product to increase the quantity
        for order_item in order_items:
            # item = Product.objects.get(id=order_item.item)
            order_item.item.base_quantity += order_item.consume_quantity
            order_item.item.save()



