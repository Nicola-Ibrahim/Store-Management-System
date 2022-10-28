from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
        path("orders/", views.OrdersListCreateView.as_view(), name='orders-list'),
        path("orders_items/", views.OrderItemsCreateView.as_view(), name='orders-items'),
        path("orders/<int:pk>/", views.OrderRetrieveView.as_view(), name='order-detail'),

    ]   
    
