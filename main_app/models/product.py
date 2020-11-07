from django.db import models

from main_app.models.category import Category


class Product(models.Model):
    title = models.CharField(blank=False, unique=True)
    description = models.TextField(blank=False)
    imageURL = models.URLField(blank=False)
    price = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
