# products/urls.py

from django.urls import path  # Import path to define URL patterns
from .views import ProductList, ProductDetail  # Import views for listing and detail views of products

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),  # Route for listing products (GET request)
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),  # Route for retrieving a single product by ID (GET request)
]
