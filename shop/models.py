from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('shop:product', kwargs=[self.id])


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_count = models.PositiveIntegerField(default=0)
    product_cost = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.product.name


class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    invoice_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_date


class Transaction(models.Model):
    STATUS_CHOICE = [
        ('pending', 'Pending'),
        ('failed', 'Failed'),
        ('completed', 'Completed'),
    ]
    invoice = models.ForeignKey(Invoice, models.SET_NULL, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=50)