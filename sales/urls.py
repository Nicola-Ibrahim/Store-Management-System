from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(
    [
        path("orders/", views.OrdersListCreateView.as_view(), name='orders-list'),
        path("orders/<int:pk>/", views.OrderRetrieveView.as_view(), name='order-detail'),
    ]
)    
    
