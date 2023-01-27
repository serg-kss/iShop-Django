from django.contrib import admin
from .models import Products, Orders, Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','address', 'tel')

    
@admin.register(Products)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'amount', 'supplier')
    
    
@admin.register(Orders)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('order_number','date', 'total')
    list_filter = ('order_number', 'date', 'phone')


admin.site.site_title = 'Админ панель iShop'
admin.site.site_header = 'Админ панель iShop'