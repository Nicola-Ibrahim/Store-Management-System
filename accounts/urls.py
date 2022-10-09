from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('customer/create/', views.CustomerSignupView.as_view(), name='create_customer'),
    path('staff/create/', views.StaffSignupView.as_view(), name='create_customer')
]
