from django.shortcuts import render
from .models import Products


def home (request):
      
   data = {
      'title': 'Головна сторінка',
      'products': Products.objects.all()
   }  
   return render(request, 'main/main.html', data)


def contacts (request):
      
   data = {
      'title': 'Контакти',
   }  
   return render(request, 'main/contacts.html', data)
