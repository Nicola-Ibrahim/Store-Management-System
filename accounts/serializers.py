
from rest_framework import serializers
from . import models


class CustomersSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = models.Customer
        fields = '__all__'

    

class StaffSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = models.Staff
        fields = "__all__"


