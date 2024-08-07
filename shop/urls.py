from django.urls import path

from shop import views
app_name = 'shop'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>/', views.HomeView.as_view(), name='category_filter'),
    path('<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]