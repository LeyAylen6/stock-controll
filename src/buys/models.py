from django.db import models
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class Provider(models.Model):
    """Class that represents the products provider."""
    name = models.TextField(max_length=30, blank=False)
    lastname = models.TextField(max_length=30, blank=False)
    dni = models.IntegerField(validators=[MinValueValidator(0)], blank=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F'{self.name.upper()} {self.lastname.upper()}'
    

class Product(models.Model):
    """Class that represents the products in the stock."""
    name = models.TextField(blank=False, max_length=50)
    price = models.FloatField(validators=[MinValueValidator(0)], blank=False)
    actual_stock = models.IntegerField(blank=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return F'{self.name.upper()} - {self.created_at}'

    
    

        