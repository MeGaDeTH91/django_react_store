from django.contrib import admin


# Register your models here.
from main_app.models.category import Category
from main_app.models.customer import Customer
from main_app.models.order import Order
from main_app.models.product import Product
from main_app.models.review import Review

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Review)
