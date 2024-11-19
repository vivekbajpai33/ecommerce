from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator, URLValidator

# local import 
from apps.products.models import Product

# Create your models here.


class ProductService(models.Model):
    SERVICE_TYPES = [
        ('WARRANTY', 'Warranty Service'),
        ('INSTALLATION', 'Installation Service'),
        ('SUPPORT', 'Technical Support'),
        ('MAINTENANCE', 'Maintenance'),
        ('INSURANCE', 'Product Insurance')
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    duration_days = models.PositiveIntegerField()
    terms_conditions = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['product', 'service_type']

    def __str__(self):
        return f"{self.product.name} - {self.name}"






