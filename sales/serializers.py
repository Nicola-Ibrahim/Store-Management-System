
from rest_framework import serializers

from .models import Order, OrderItem
from production.models import Item
from accounts.models import Customer, Staff
from django.db.models import Q

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
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    # M2M relation field
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'url', 'customer_name', 'staff_name', 'customer', 'staff', 'items']
        read_only_fields = ['id']
        extra_kwargs = {
            'customer': {'write_only': True},
            'staff': {'write_only': True},
        }    
    
    def get_items(self, instance):
        """Custom Related field to show order related items in specific shape"""

        # Retrieve the sold items that relate to order 
        order_items = OrderItem.objects.filter(order=instance)

        order_items_list = list()

        # Iterate through items
        for order_item in order_items:
            order_items_list.append({
                'item': order_item.item.name,
                'consume quantity': order_item.consume_quantity, 
                'discount':order_item.discount,
            })

        return order_items_list

    def to_internal_value(self, data):
        """Change the inserting data from str to num for model"""

        data['customer'] = Customer.objects.get(username=data.get('customer'))
        data['staff'] = Staff.objects.get(username=data['staff'])

        # print(data)

        for item in data.get('items'):
            if(isinstance(item['item'], str)):
               item['item'] = Item.objects.get(name=item['item'])
        


        return data
    

    def create(self, validated_data):
        items: list = validated_data.pop('items')
        instance = super().create(validated_data)

        for item in items:
            it = OrderItem.objects.create(
                order=instance, 
                item=item['item'],
                consume_quantity=item['consume_quantity'],
                discount=item['discount']
            )
        return instance


