from django.db import models # To link to database

# Create your models here.
# Don't forge to add to INSTALLED_APPS in settings.py
# blank = how the field is rendered. False = required
class Product(models.Model):
    title       = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = True)
    price       = models.DecimalField(max_digits = 10000, decimal_places = 2)
    summary     = models.TextField(blank = True, null = False)
    featured    = models.BooleanField() # null=True, default=True
