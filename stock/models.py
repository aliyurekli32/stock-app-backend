from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#? Table-1 Category
class Category(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.name}"

#? Table-2 Brand
class Brand(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.name}"
    
#? Table-3 Firm
class Firm(models.Model):
    name = models.CharField(max_length=15)
    phone_number = models.PhoneNumberField(blank=True)
    address = models.CharField(max_length=100)