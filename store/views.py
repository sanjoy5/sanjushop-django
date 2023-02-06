from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import *

# Create your views here.

def store(request,cat_slug=None):
    categories = None
    products = None

    if cat_slug != None:
        categories = get_object_or_404(Category,slug=cat_slug)
        products = Product.objects.filter(category=categories,is_available=True)
    else:
        products = Product.objects.filter(is_available=True)  
    
    context = {'products':products}
    return render(request,'store/store.html',context)


def product_details(request,cat_slug,prod_slug):
    try:
        single_product = Product.objects.get(category__slug=cat_slug,slug=prod_slug)
    except Exception as e:
        raise e

    context = {'single_product':single_product}
    return render(request,'store/product_details.html',context)