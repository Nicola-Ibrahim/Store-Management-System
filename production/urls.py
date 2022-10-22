from django.urls import path
from . import views

urlpatterns = [
    path("items/", views.ItemsListView.as_view(), name='items-list'),
    path("items/<int:pk>", views.ItemRetrieveView.as_view(), name='item-detail'),

]
