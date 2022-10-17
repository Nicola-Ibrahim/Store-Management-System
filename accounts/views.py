
from . import models
from rest_framework import generics

from . import serializers
from .permissions import OnlyAdminPermissionMixin, OnlyStaffPermissionMixin, IsPresidentTestMixin, IsStaffTestMixin


# Create your views here.
class CustomersListView(
    OnlyStaffPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomersSerializer
    

class CustomerRetrieveUpdateDestroyView(
    OnlyStaffPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView
    ):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomersSerializer


class StaffListView(
    OnlyAdminPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer



class StaffRetrieveUpdateDestroyView(
    OnlyAdminPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView
    ):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer


