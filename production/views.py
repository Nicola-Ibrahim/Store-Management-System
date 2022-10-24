from rest_framework import generics
from .models import Product
from . import serializers

# Create your views here.

class ProductsListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = 'slug'


