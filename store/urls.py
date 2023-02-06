from django.urls import path
from .views import *


urlpatterns = [
    path('',store,name='store'),
    path('<slug:cat_slug>/',store,name='products_by_category'),
    path('<slug:cat_slug>/<slug:prod_slug>/',product_details,name='product_details'),
]
