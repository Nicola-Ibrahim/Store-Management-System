
from accounts import models, services
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

from rest_framework import exceptions
from rest_framework import generics, permissions, views, authentication
from rest_framework.response import Response

from . import serializers, authenticatons


# Create your views here.
class CustomersListView(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomersSerializer
    authentication_classes = [authenticatons.CustomAuth]
    permission_classes = [permissions.IsAuthenticated]

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomersSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



class StaffListView(generics.ListCreateAPIView):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



class StaffRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



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
        response = Response()
        response.set_cookie(key='jwt', value=token,  httponly=True)
        return response