
import imp
from .models import Item
from sales.serializers import OrderSerializer
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):

    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'orders']

