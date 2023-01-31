from django.db import models

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
