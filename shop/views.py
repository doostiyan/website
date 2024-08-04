from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
#
# # from shop.models import Product
#
#
class HomeView(View):
    def get(self, request):
#         products = Product.objects.all()
        return render(request, 'shop/index.html', )

#
#
# class ProductDetailView(View):
#     def get(self, request, product_id):
#         product = get_object_or_404(Product, pk=product_id)
#         return render(request, 'shop/product.html', {'product': product})
