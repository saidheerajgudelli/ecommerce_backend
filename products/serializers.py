from rest_framework import serializers
from .models import Product

# Serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # Define the model to be serialized
        fields = ['id', 'name', 'description', 'imagepath', 'price_unit', 'price', 'manufacturer']  # Fields to be included in the serialization
        read_only_fields = ['created', 'updated']  # Mark 'created' and 'updated' fields as read-only
    
    # Optional custom fields (required=False makes these optional during validation)
    name = serializers.CharField(required=False)  # Name of the product
    description = serializers.CharField(required=False)  # Description of the product
    imagepath = serializers.CharField(required=False)  # Image URL path for the product
    price_unit = serializers.CharField(required=False)  # Price unit (e.g., USD)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)  # Price of the product with decimal precision
    manufacturer = serializers.CharField(required=False)  # Manufacturer of the product
