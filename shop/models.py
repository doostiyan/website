from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_sub = models.BooleanField(default=False)
    sub_categories = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='scategory')

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering= ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter', args=[self.slug])


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    description = RichTextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])