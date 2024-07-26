from django.contrib import admin

from shop.models import Product, Order, OrderItem, Transaction, Invoice


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created')


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


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Invoice)
admin.site.register(Transaction)


