from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from cart.cart import Cart
from cart.form import CartAddForm, CouponApplyForm
from cart.models import Order, OrderItem
from shop.models import Product


# Create your views here.

class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('cart:cart')


class CartDeleteView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart')


class OrderCreateView(LoginRequiredMixin,View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        return redirect('cart:order_create', order.id)


class OrderDetailView(LoginRequiredMixin, View):
    form_class = CouponApplyForm()

    def get(self, request, order_id):
        cart = Cart(request)
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'cart/order.html', {'order': order, 'form': self.form_class})