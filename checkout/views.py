from django.shortcuts import render, redirect
from .forms import CreateOrderForm
from main.models import Orders
from main.models import Products
from cart.cart import Cart
from .bot import bot, chat_id
from django.db.models import F


def checkout(request):
   i_bot = bot
   if request.method == "POST":
      form = CreateOrderForm(request.POST)
      if form.is_valid():
         order = Orders()
         cart = Cart(request)
         order.goods = ''
         for item in cart:
            order.goods = order.goods + item['product'].title + ' - ' + str(item['quantity']) + '; ' 
            Products.objects.filter(title=item['product'].title).update(amount=F("amount")-item['quantity'])             
         order.order_number = Orders.objects.latest('id').order_number + 1
         order.name = form.cleaned_data.get('name')
         order.surname = form.cleaned_data.get('surname')
         order.phone = form.cleaned_data.get('phone')
         order.email = form.cleaned_data.get('email')
         order.total = str(cart.get_total_price())
         order.delivery = f'{form.cleaned_data.get("delivery")}; Endpoint: {form.cleaned_data.get("delivery_info")}'
         order.save()
         i_bot.send_message(
            chat_id,
            f'Новий заказ: {order.order_number}\nПокупець: {order.name} {order.surname}\nТел: {order.phone}\nТовар: {order.goods}\nСума: {order.total}UAH\nДоставка: {order.delivery}')
         cart.clear()         
         return redirect('result')
   else:
      form = CreateOrderForm()
   return render(request, 'checkout/checkout.html', {
      'form': form,
      'title': 'Checkout'})


def result(request):
   return render(request, 'checkout/result.html', {
      'title': 'Thank You'
      })

