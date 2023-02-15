from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import *
from carts.models import *
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.

def store(request,cat_slug=None):
    categories = None
    products = None
    

    if cat_slug != None:
        categories = get_object_or_404(Category,slug=cat_slug)
        products = Product.objects.filter(category=categories,is_available=True).order_by('id')
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True).order_by('id') 
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    products_count = products.count()
    
    context = {'products':paged_products,'products_count':products_count}
    return render(request,'store/store.html',context)


def product_details(request,cat_slug,prod_slug):
    try:
        single_product = Product.objects.get(category__slug=cat_slug,slug=prod_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()

    except Exception as e:
        raise e

    context = {'single_product':single_product,'in_cart':in_cart}
    return render(request,'store/product_details.html',context)


def search(request):
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword ) | Q(name__icontains=keyword))
    
    products_count = products.count()

    context = {'products':products,'keyword':keyword,'products_count':products_count}
    return render(request,'store/store.html',context)