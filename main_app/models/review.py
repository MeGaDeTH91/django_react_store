from django.db import models

from main_app.models.customer import Customer
from main_app.models.product import Product


class Review(models.Model):
    content = models.CharField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
