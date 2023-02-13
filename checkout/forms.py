from django import forms
from main.models import Orders
from .choices import *


class CreateOrderForm(forms.Form):
   name = forms.CharField(
      label='Put Name', 
      required=True,
      widget=forms.TextInput(
         attrs={
            'class': 'peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0'
         }))
   surname = forms.CharField(
      label='Put Surname',
      required=True,
      widget=forms.TextInput(
         attrs={
            'class': 'peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0'
         }
      ))
   email = forms.EmailField(
      label='Put email',
      required=False,
      widget=forms.EmailInput(
         attrs={
            'class': 'peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0'
         }
      ))
   phone = forms.CharField(
      label='Put Phone',
      required=True,
      widget=forms.TextInput(
         attrs={
            'class': 'peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0'
         }
      ))
   delivery = forms.ChoiceField(
      label='Chose a Delivery',
      required=True,
      choices=options_list_checkout
   )
   
   class Meta:
      model = Orders
      