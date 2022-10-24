from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsListView.as_view(), name='products-list'),
    path("products/<str:slug>/", views.ProductRetrieveView.as_view(), name='product-detail'),

]
