from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# local import
from apps.products.models import Product
from apps.services.models import ProductService

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    shipping_address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    service = models.ForeignKey(ProductService, on_delete=models.SET_NULL, null=True, blank=True)
    service_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order #{self.order.id}"

    @property
    def total_price(self):
        service_cost = self.service_price or 0
        return (self.price * self.quantity) + service_cost
    
class TrackOrder(models.Model):
    ORDER_STATUS_CHOICES = [
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    order_number = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userorders')
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='PENDING')
    
    # Customer Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    
    # Shipping Information
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    
    # Order Details
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    items_count = models.PositiveIntegerField()
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Shipping Details
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    shipped_at = models.DateTimeField(blank=True, null=True)
    estimated_delivery = models.DateField(blank=True, null=True)
    
    # Additional Notes
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order {self.order_number} - {self.status}"

    
