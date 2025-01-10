from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse

# List and create products
class ProductList(APIView):
    authentication_classes = [JWTAuthentication]  # Requires authentication using JWT
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get(self, request):  # Fetch all products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):  # Create a new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, and delete a product by ID
class ProductDetail(APIView):
    authentication_classes = [JWTAuthentication]  # Requires authentication using JWT
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get(self, request, pk):  # Fetch a single product by its primary key (ID)
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):  # Update an existing product by ID
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # Delete a product by ID
        try:
            product = Product.objects.get(pk=pk)
            product.delete()  # Deleting the product from the database
            return Response(status=status.HTTP_204_NO_CONTENT)  # Successful deletion response
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
