
from rest_framework import serializers
from .dataclasses import OrderService, SoldItemDetail
from .models import Order, OrderItem
from production.models import Product
from accounts.models import Customer, Staff



class OrderItemSerializer(serializers.ModelSerializer):

    # Add extra read_only field
    order_id = serializers.ReadOnlyField(source='order.id')
    item_name = serializers.ReadOnlyField(source='item.name')


    class Meta:
        model = OrderItem
        fields = ['order_id', 'item_name', 'consume_quantity', 'discount']


class OrderSerializer(serializers.ModelSerializer):

    # Add extra read_only field
    customer_name = serializers.ReadOnlyField(source='customer.username')
    staff_name = serializers.ReadOnlyField(source='staff.username')

    # M2M relation field
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'url', 'customer_name', 'staff_name', 'customer', 'staff', 'items', 'total_price']
        read_only_fields = ['id']

        extra_kwargs = {
            'customer': {'write_only': True},
            'staff': {'write_only': True},
        }    
    
    def get_items(self, instance):
        """Custom Method-field to display related items in a specific shape"""

        # Retrieve the sold items that relate to order 
        order_items = OrderItem.objects.filter(order=instance)

        order_items_list = list()

        # Iterate through items
        for order_item in order_items:
            order_items_list.append({
                'item': order_item.item.name,
                'consume quantity': order_item.consume_quantity, 
                'discount': order_item.discount,
                'price' : order_item.price
            })

        return order_items_list

    def to_internal_value(self, data):
        """Change the inserting data from str to num for model"""

        data['customer'] = Customer.objects.get(username=data.get('customer'))
        data['staff'] = Staff.objects.get(username=data['staff'])

        # print(data)

        for item in data.get('items'):
            if(isinstance(item['item'], str)):
                item['item'] = Product.objects.get(name=item['item'])
        
        return data
    

    def create(self, validated_data):
        items: list = validated_data.pop('items')
        items = [SoldItemDetail(**item) for item in items]

        # Create order instance
        instance = super().create(validated_data)

        # Link order with inserted items
        OrderService(order=instance).link(sold_items=items)


        return instance

