from django.urls import path

from shop import views
app_name = 'shop'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('checkout/', views.HomeView.as_view(), name='checkout'),
    # path('product/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    # path('store/', views.HomeView.as_view(), name='store'),
]