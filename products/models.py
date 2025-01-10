from django.db import models

# Model representing a product in the database
class Product(models.Model):
    name = models.CharField(max_length=255)  # Name of the product, maximum length of 255 characters
    description = models.TextField()  # Description of the product, allows for longer text
    imagepath = models.CharField(max_length=255)  # Path or URL to the product's image, maximum length of 255 characters
    price_unit = models.CharField(max_length=10)  # The unit for the price (e.g., USD, EUR), maximum length of 10 characters
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product, with precision of up to 10 digits and 2 decimal places
    manufacturer = models.CharField(max_length=255)  # Manufacturer of the product, maximum length of 255 characters

    def __str__(self):
        return self.name  # Return the name of the product when the object is represented as a string
