from django import template
from product.models import Product,Catigory

register = template.Library()

@register.inclusion_tag('catigory_tags/cat1.html')
def cat1():

    c = Catigory.objects.last()

    catigory1 = Product.objects.filter(catigory=c)[:4]
    context = {
        'catigory1':catigory1
    }
    
    return context

        

@register.inclusion_tag('catigory_tags/bestOfre.html')
def Bestofre():

    
    ofre = Product.objects.all()[:4]
    context = {
        'ofre':ofre,
    }
    
    return context


