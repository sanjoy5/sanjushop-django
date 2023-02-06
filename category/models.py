from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length="255",blank=True)
    image = models.ImageField(upload_to='category_images/',blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
