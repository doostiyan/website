
from django.urls import path

from cart import views

app_name = 'cart'
urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('detail/<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('check/', views.CartView.as_view(), name='cart'),
    path('check/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('check/delete/<int:product_id>/', views.CartDeleteView.as_view(), name='cart_delete'),
    path('pay/<int:order_id>/', views.OrderPayView.as_view(), name='order_pay'),
    path('verify/', views.OrderVerifyView.as_view(), name='order_pay'),
    path('apply/<int:order_id>/', views.CouponApplyView.as_view(), name='apply_coupon')
]