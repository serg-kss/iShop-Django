from django.shortcuts import render, redirect
from .forms import CreateOrderForm
from main.models import Orders
from cart.cart import Cart


def checkout(request):
   
   if request.method == "POST":
      form = CreateOrderForm(request.POST)
      if form.is_valid():
         order = Orders()
         cart = Cart(request)
         order.order_number = Orders.objects.latest('id').order_number + 1
         order.name = form.cleaned_data.get('name')
         order.surname = form.cleaned_data.get('surname')
         order.phone = form.cleaned_data.get('phone')
         order.email = form.cleaned_data.get('email')
         order.total = str(cart.get_total_price())
         order.save()         
         return redirect('home-page')
   else:
      form = CreateOrderForm()
   return render(request, 'checkout/checkout.html', {
      'form': form,
      'title': 'Checkout'})

# Create your views here.
