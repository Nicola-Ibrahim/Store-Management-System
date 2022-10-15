
from accounts import models, services
from rest_framework import exceptions
from rest_framework import generics, views, permissions
from rest_framework.response import Response

from . import serializers
from .permissions import OnlyAdminPermissionMixin, StaffPermissionMixin


# Create your views here.
class CustomersListView(
    StaffPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomersSerializer
    

class CustomerRetrieveUpdateDestroyView(
    StaffPermissionMixin,
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


class LoginApi(views.APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = models.User.objects.filter(username=username).first()

        if(user is None):
            raise exceptions.AuthenticationFailed("Invalid credentials")

        if(not user.check_password(raw_password=password)):
            raise exceptions.AuthenticationFailed("Invalid credentials")

        token = services.create_token(user.id)
        return Response(token)