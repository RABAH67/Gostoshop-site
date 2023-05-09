from django.shortcuts import render,get_object_or_404 ,redirect
from .models import Product ,MainSlider
from user_accounts.models import Cart
from .forms import NewCommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def index(request):
    
    product = Product.objects.filter()[:15]
    
    cart = Cart.objects.all()
    
    slide = MainSlider.objects.all()

    context = {
        'products':product,
        'slide':slide,
        'cart':cart,
    }
    

    
    return render(request,'index.html',context)



def single_product(request,slug):
    single_product = get_object_or_404(Product,slug=slug)
    related_product = Product.objects.filter(catigory=single_product.catigory).exclude(slug=slug)[:10]
    comments = single_product.product.filter()
    recent_views_product = None
    if 'recent_views' in request.session:
    
        if slug in request.session['recent_views']:
            request.session['recent_views'].remove(slug)
            
            
        prod = Product.objects.filter(slug__in=request.session['recent_views'])
        recent_views_product = sorted(prod,
                        key=lambda x:request.session['recent_views'].index(x.slug)
                                    )
        request.session['recent_views'].insert(0 ,slug)
        if len(request.session['recent_views']) > 5 :
            request.session['recent_views'].pop()
    else:
        request.session['recent_views'] = [slug]
    
    request.session.modified = True
    
    new_comment = NewCommentForm()

    if request.method == "POST":
            new_comment = NewCommentForm(data=request.POST)
            if new_comment.is_valid():
                comment_form =  new_comment.save(commit=False)
                comment_form.product = single_product
                comment_form.save()
                messages.success(request,'Thanks For Your Review')
                return redirect('detail',slug)
            else:
                new_comment = NewCommentForm()

    context = {
        'single_product':single_product,
        'related_product':related_product,
        'comments':comments,
        'new_comment':new_comment,
        'recent_views_product':recent_views_product,
    }
    return render(request,'single-product.html',context)


def ShopPage(request):
    
    allproduct = Product.objects.all()
    
    Productcount = Product.objects.all().count()

    paginator = Paginator(allproduct,8)

    page_nember = request.GET.get('page')
    
    page_obj = paginator.get_page(page_nember)
    
    queiry = request.GET.get('queiry' ,'')

    pp = 0
    
    if queiry:
        page_obj = allproduct.filter(Q(title__icontains=queiry) |
                                     Q(description__icontains=queiry) 
                                    )
        messages.success(request,f'For Search "{queiry}" ')
        pp = page_obj.count()


    context = {
        'allproduct':page_obj,
        'Productcount':Productcount,
        'queiry':queiry,
        'pp':pp,
    }
    
    
    return render(request,'shop.html',context)




def handel404(request,exception):
    
    return render(request,'error_404.html',status=404)



def handel500(request):
    
    return render(request,'error_500.html',status=500)