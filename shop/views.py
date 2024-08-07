from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from cart.form import CartAddForm
from shop.models import Product, Category


class HomeView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop/index.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        form = CartAddForm()
        return render(request, 'shop/product.html', {'product': product, 'form': form})


