from django.contrib import admin

from shop.models import Product, Category


# from shop.models import Product, Order, OrderItem, Transaction, Invoice
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'created')


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'created')
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'created')
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'created')
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'created')
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'created')


# admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
# admin.site.register(OrderItem)
# admin.site.register(Invoice)
# admin.site.register(Transaction)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
