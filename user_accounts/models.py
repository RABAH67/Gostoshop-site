from django.db import models
from product.models import Product

# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quentity = models.IntegerField(default=1)

    def total_panie(self):
        return self.product.price * self.quentity
    
    def __str__(self):
        return self.product.title
    
    
    
class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    products = models.ManyToManyField(Product,blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2,default=0.00)
    active = models.BooleanField(default=True)



    @property

    
    def __str__(self):
        return f"Cart id {self.id}"
    