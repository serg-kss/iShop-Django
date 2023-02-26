from django.urls import path
from . import views


urlpatterns = [
    path('/checkout-form', views.checkout, name='checkout-form'),
    path('/result', views.result, name='result'),
]