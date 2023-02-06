from django.shortcuts import render
from store.models import Product
# Create your views here.

def homePage(request):
    products = Product.objects.filter(is_available=True)
    context = {'products':products}
    return render(request,'home/home.html',context)