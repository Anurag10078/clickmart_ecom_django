from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from decimal import Decimal

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #only 1 user can have only 1 cart 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email
    
    @property
    def subtotal(self): # cart.subtotal
        subtotal = Decimal("0.00")
        for item in self.items.all():
            subtotal += item.product.price * item.quantity
        return subtotal
    
    @property
    def tax_amount(self):
        tax = Decimal("0.00")
        for item in self.items.all():
            tax += (item.product.price * item.quantity * Decimal(item.product.tax_percentage / Decimal("100.00")))
        return tax
    
    @property
    def grand_total(self):
        grand_total = self.subtotal + self.tax_amount
        return grand_total
    


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items") #delete cascade ka matlab agar usa relation wala primary delete hota hai tho ya bhi delete ho jayage
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}" #applex2 like this we want to show 