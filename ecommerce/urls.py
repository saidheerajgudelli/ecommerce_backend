"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views.
"""

# ecommerce/urls.py
from django.contrib import admin  # Admin module for Django
from django.urls import path, include  # Path and include for routing
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # View for obtaining JWT token
    TokenRefreshView,     # View for refreshing JWT token
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('api/products/', include('products.urls')),  # Routes to product URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
]
