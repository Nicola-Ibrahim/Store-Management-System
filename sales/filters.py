import django_filters.rest_framework as filters
from .models import Order


class OrderFilter(filters.FilterSet):

    # min_price = filters.NumberFilter(field_name="total_price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="total_price", lookup_expr='lte') 

    class Meta:
        model = Order
        fields = {
            'id': ['exact'], 
            'status': ['icontains', 'exact'],
            'order_date': ['exact', 'year__gt']

            }