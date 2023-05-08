from django.shortcuts import render ,redirect,HttpResponseRedirect ,get_object_or_404
from django.views import View
from .forms import SingUpForm
from django.contrib import messages
from .models import Cart ,CartItem
from product.models import Product
from django.urls import reverse

# Create your views here.

def cart(request):
    
    
  
    cart = Cart.objects.all()[0]
    oo = Product.objects.filter()[0:4]
    context = {
        'cart':cart,
        'oo':oo,

    }
    
    
    return render(request,'cart.html',context)


def add_to_cart(request ,slug):
    
 
    cart = Cart.objects.all()[0]
        
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    
    cartitem , created = CartItem.objects.get_or_create(product=product)
    if created:
        print('somthing')
        
    if cartitem not in cart.items.all():
        cart.items.add(cartitem)
    else:
        cart.items.remove(cartitem)
    
    new_total = 0.00
    
    for item in cart.items.all():
        line_total = float(item.product.price) * item.quentity
        new_total += line_total
        

    request.session['totla'] = cart.items.count()
    
    cart.total = new_total
    cart.save()
    request.session['nn'] = cart.total

    return HttpResponseRedirect(reverse('cart'))

        
    




class CreateUserViews(View):
    
    def get(self,request):

        form = SingUpForm()

        return render(request,'singin.html',locals())

    def post(self,request):

        form = SingUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Sing in succussFull')
        else:
            messages.warning(request,'invalid data input')



        return render(request,'singin.html',locals())