from django.db import models


class Category(models.Model):
    title = models.CharField(blank=False, unique=True)
    imageURL = models.URLField(blank=False)
