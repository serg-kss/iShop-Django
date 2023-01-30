from django.shortcuts import render
from .models import Products
from cart.forms import CartAddProductForm


def home (request):
   cart_product_form = CartAddProductForm()   
   data = {
      'title': 'Головна сторінка',
      'products': Products.objects.all(),
      'cart_product_form': cart_product_form
   }  
   return render(request, 'main/main.html', data)


def contacts (request):
      
   data = {
      'title': 'Контакти',
   }  
   return render(request, 'main/contacts.html', data)
