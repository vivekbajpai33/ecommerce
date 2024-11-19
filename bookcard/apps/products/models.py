from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from djmoney.models.fields import MoneyField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    regular_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    sale_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)
    offer_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)
    amazon_link = models.URLField(max_length=500, validators=[URLValidator()])
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        return self.stock > 0
    
    @property
    def has_offer(self):
        return self.offer_price is not None

class ProductOffer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='offers')
    discount_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.discount_percentage}% off"
    



