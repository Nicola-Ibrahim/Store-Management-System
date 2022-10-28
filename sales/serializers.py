
from rest_framework import serializers
from .models import Order, OrderItem
from production.models import Product
from accounts.models import Customer, Staff
from accounts.serializers import CustomersSerializer, StaffSerializer



class OrdersInlineSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    total_price = serializers.IntegerField()




class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    # Add extra read_only field
    url = serializers.HyperlinkedIdentityField(
        view_name='order-detail',
        lookup_field='pk',
        read_only=True
    )

    purchased_by = CustomersSerializer(source='customer', read_only=True)
    processed_by = StaffSerializer(source='staff', read_only=True)

    related_orders = OrdersInlineSerializer(source='customer.customer_orders.all', many=True, read_only=True)

    # M2M relation field
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 
            'url', 
            'purchased_by', 
            'processed_by',
            'related_orders', 
            'customer', 
            'staff', 
            'items', 
            'total_price'
            
        ]
        read_only_fields = ['id']

        extra_kwargs = {
            'customer': {'write_only': True},
            'staff': {'write_only': True},
        }    
    
    def get_items(self, obj):
        """Custom Method-field to display related items in a specific shape"""

        # Retrieve the sold items that relate to order 
        qs = OrderItem.objects.filter(order=obj)
        return OrderItemSerializer(qs, many=True, context=self.context).data

    def to_internal_value(self, data):
        """Change the inserting data from str to num for model"""

        data['customer'] = Customer.objects.get(username=data.get('customer'))
        data['staff'] = Staff.objects.get(username=data['staff'])

        # print(data)

        for item in data.get('items'):
            if(isinstance(item['item'], str)):
                item['item'] = Product.objects.get(name=item['item']).id
        
        return data


    def create(self, validated_data):
        order_items: list = validated_data.pop('items')


        # Check available items
        for order_item in order_items:
            item = Product.objects.get(id=order_item['item'])
            item.is_available(order_item['consume_quantity'])

        # Create order instance
        instance = super().create(validated_data)

        for item in order_items:
            item['order'] = instance.id
        
        # Link order with inserted items
        ser = OrderItemSerializer(data=order_items, many=True)
        ser.is_valid(raise_exception=True)
        ser.save()


        return instance

    

