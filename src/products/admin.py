from django.contrib import admin

# import Product class from models.py
from .models import Product

# Register your models here.
# So we can view models in admin view
admin.site.register(Product)