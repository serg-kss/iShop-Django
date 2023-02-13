from django.shortcuts import render
from cart.forms import CartAddProductForm
from django.views.generic import ListView, DetailView

# Create your views here.

#class AdditionalProductsPage(ListView):
#   template_name = 'products/products.html'
 #  context_object_name = 'add-products'
   
#   def get_context_data(self, **kwargs):
#      ctx = super(AdditionalProductsPage, self).get_context_data(**kwargs)
 #     ctx['title'] = 'Доп продукти'      
#      return ctx


def AdditionalProductsPage (request):
      
   data = {
      'title': 'Доп продукти',
   }  
   return render(request, 'products/products.html', data)
