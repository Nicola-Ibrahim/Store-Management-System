from django.db import models

# # Create your models here.
# class Orders(models.Model):
# # Order status: 1 = Pending; 2 = Processing; 3 = Rejected; 4 = Completed
#     ORDER_STATUS = (
#         ('Pending', 1),
#         ('Processing', 2),
#         ('Rejected', 3),
#         ('Completed', 4),
#     )

#     status = models.CharField(max_length=20, choices=ORDER_STATUS)
#     order_date = models.DateTimeField(auto_now=True)
#     required_date = models.DateTimeField(auto_now=True)
#     shipped_date = models.DateTimeField(auto_now_add=True)
#     customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
#     staff_id = models.ForeignKey(User, on_delete=models.SET_NULL)
#     store_id = models.ForeignKey(Store)
