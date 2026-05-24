from django.db import models
from decimal import Decimal

# Create your models here. #it can be big 

class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_desc = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories' 
        
    
    def __str__(self):
        return self.cat_name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True)
    image = models.ImageField(upload_to='product/',blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=Decimal('0.00'))
    stock = models.PositiveIntegerField(default=0)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)#it is saving the current timestamp we cannot change it and it will save the timestamp when we create the product   
    updated_at = models.DateTimeField(auto_now=True)#it is saving the current timestamp whenever we update the product
    
    
    def __str__(self):
        return self.name
