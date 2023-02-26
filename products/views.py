from django.shortcuts import render
from cart.forms import CartAddProductForm
from django.views.generic import ListView, DetailView


def AdditionalProductsPage (request):
      
   data = {
      'title': 'Доп продукти',
   }  
   return render(request, 'products/products.html', data)
