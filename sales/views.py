from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

# Create your views here.
class OrdersListCreateView(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


