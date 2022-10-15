from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('customers/', views.CustomersListView.as_view(), name='customers-list'),
    path('staff/', views.StaffListView.as_view(), name='staff-list'),
    # path('login/', views.LoginApi.as_view(), name='login')
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
