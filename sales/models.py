from django.db import models
from accounts.models import Customer, Staff
from production.models import Item


class Store(models.Model):
    pass

# Create your models here.
class Order(models.Model):

    class Status(models.TextChoices):
        # Order status: 1 = Pending; 2 = Processing; 3 = Rejected; 4 = Completed
        PENDING = 'PENDING', 'pending'
        PROCESSING = 'PROCESSING', 'Processing'
        REJECTED = 'REJECTED', 'Rejected'
        COMPLETED = 'COMPLETED', 'Completed'

    status = models.CharField(max_length=20, default=Status.PROCESSING, choices=Status.choices)
    order_date = models.DateTimeField(auto_now=True)
    required_date = models.DateTimeField(auto_now=True)
    shipped_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name="customer_orders", on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, related_name="staff_orders", on_delete=models.DO_NOTHING)
    # store_id = models.ForeignKey(Store)
    items = models.ManyToManyField(Item, through='OrderItem', related_name='orders')

    @property
    def total_price(self):
        # order_items = OrderItem.objects.filter(order=self.pk)
        order_items = self.items_set.all()
        print(self.items_set.all())
        total = sum([item.price * item.quantity for item in order_items])
        if not total:
            return 0
        return total

    def __str__(self) -> str:
        return f"Order-{self.id} -> by:{str(self.customer)}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    consume_quantity = models.IntegerField(default=1)
    discount = models.FloatField(default=0)

    @property
    def price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"Order-{str(self.order.id)} -> {str(self.item)}"
