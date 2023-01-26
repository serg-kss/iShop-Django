from django.shortcuts import render


def home (request):
   number = 50
   products = [
      {
         'id':number
      }
   ]
     
   data = {
      'title': 'Головна сторінка',
      'products': products
   }  
   return render(request, 'main/main.html', data)
