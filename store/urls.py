from django.urls import path
from .views import *


urlpatterns = [
    path('',store,name='store'),
    path('category/<slug:cat_slug>/',store,name='products_by_category'),
    path('category/<slug:cat_slug>/<slug:prod_slug>/',product_details,name='product_details'),
    path('search/',search,name='search'),
]
