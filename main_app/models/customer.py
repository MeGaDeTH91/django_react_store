from django.contrib.auth.models import User
from django.db import models

from main_app.models.order import Order
from main_app.models.product import Product


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=21)
    delivery_address = models.CharField(max_length=80)
    cart = models.ManyToManyField(Product)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
