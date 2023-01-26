from django.contrib import admin
from .models import Products, Orders, Supplier

admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Supplier)

# Register your models here.
