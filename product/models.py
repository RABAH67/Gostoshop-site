from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):

    sizes = (
        ('s','s'),
        ('x','x'),
        ('xs','xs'),
        ('L','L'),
    )
    
    title = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    price = models.DecimalField(max_digits=10, decimal_places=5,blank=False,null=False)
    new_price = models.DecimalField(max_digits=10, decimal_places=5,blank=True,null=True)
    catigory = models.ForeignKey('Catigory',on_delete=models.CASCADE)
    size = models.CharField(choices=sizes,max_length=50,blank=True,null=True)
    image = models.ImageField(upload_to='product',blank=True,null=True)
    date = models.DateTimeField(auto_now_add=timezone.now)
    slug = models.SlugField(blank=True,null=True)
    
    
    def save(self,*args,**kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product,self).save(*args,**kwargs)
        
    
    class Meta:
        ordering = ('-date',)
        
        
    def __str__(self):
        return self.title
        




class Catigory(models.Model):
    
    cat = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cat
    
    
    
class Comment(models.Model):
    
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=354)
    body = models.TextField()
    product = models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
    date_c = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} review {self.body} a {self.product}"
    
    class Meta:
        ordering = ("-date_c",)
    

class MainSlider(models.Model):
    
    image = models.ImageField(upload_to='SliderImages',blank=False,null=False)
    title = models.CharField(max_length=40,blank=False,null=False)
    body = models.CharField(max_length=40,blank=True,null=True)
    Promontion = models.PositiveIntegerField(blank=True,null=True)
    
    def __str__(self):
        return f"slide {self.title}  {self.Promontion}%"



