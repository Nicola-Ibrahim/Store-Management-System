from .models import Product
from sales.serializers import OrderSerializer
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    # Reverse M2M relation
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'url', 'name', 'orders']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

        

