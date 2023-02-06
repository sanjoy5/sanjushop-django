from django.db import models
from category.models import *
from django.utils.safestring import mark_safe
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products_images',blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

    def image_tag(self):
        if self.image.url:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

  