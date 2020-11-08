from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=35)
    imageURL = models.URLField(blank=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=40)
    description = models.TextField(blank=False)
    imageURL = models.URLField(blank=False)
    price = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Customer(AbstractUser):
    phone = models.CharField(max_length=21)
    delivery_address = models.CharField(max_length=80)
    cart = models.ManyToManyField(Product)

    def __str__(self):
        return self.username


class Order(models.Model):
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_at


class Review(models.Model):
    content = models.CharField(blank=False, max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
