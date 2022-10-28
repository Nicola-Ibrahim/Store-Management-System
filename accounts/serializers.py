
from rest_framework import serializers
from . import models


class CustomersSerializer(serializers.ModelSerializer):

    # related_orders = s/erializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Customer
        fields = [
            'username',
            'pk'
        ]
        extra_kwargs = {
            'password':'write_only'
        }

    # def get_realated_orders(self, obj):

    

class StaffSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = models.Staff
        fields = [
            'username',
            'pk'
        ]
        extra_kwargs = {
            'password':'write_only'
        }




