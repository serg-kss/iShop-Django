from django.shortcuts import render
from .models import Products
from cart.forms import CartAddProductForm
from django.views.generic import ListView, DetailView


class MainPage(ListView):
   model = Products
   template_name = 'main/main.html'
   context_object_name = 'products'
   
   def get_context_data(self, **kwargs):
      ctx = super(MainPage, self).get_context_data(**kwargs)
      ctx['title'] = 'Головна сторінка'      
      return ctx
   
class ProductPage(DetailView):
   model = Products
   template_name = 'main/product.html'
   context_object_name = 'product'
   
   def get_context_data(self, **kwargs):
      cart_product_form = CartAddProductForm()
      ctx = super(ProductPage, self).get_context_data(**kwargs)
      ctx['title'] = ''
      ctx['cart_product_form'] = cart_product_form     
      return ctx


def contacts (request):
        
   data = {
      'title': 'Контакти',
   }  
   return render(request, 'main/contacts.html', data)
