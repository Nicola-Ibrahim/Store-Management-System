from rest_framework import generics
from sales.models import Order
from sales.serializers import OrderSerializer


# Create your views here.
class OrdersListCreateView(
    generics.ListCreateAPIView
    ):
    """View is responsible for handling order insertion"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

