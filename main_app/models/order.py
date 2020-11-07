from django.db import models

from main_app.models.customer import Customer
from main_app.models.product import Product


class Order(models.Model):
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
