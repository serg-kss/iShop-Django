from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='home-page'),
    path('<slug:slug>', views.ProductPage.as_view(), name='product_detail'),
    path('contacts', views.contacts, name='contacts-page'),
]