from rest_framework import generics
from sales.models import Order, OrderItem
from sales.serializers import OrderSerializer, OrderItemSerializer


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

class OrderItemsListView(
    generics.ListAPIView
    ):
    """View is responsible for handling order-items insertion"""
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
