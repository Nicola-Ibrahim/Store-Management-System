from rest_framework import generics
from .models import Item
from . import serializers

# Create your views here.

class ItemsListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ItemRetrieveView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer


