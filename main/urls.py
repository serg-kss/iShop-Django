from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='home-page'),
    path('product/<int:pk>', views.ProductPage.as_view(), name='product-page'),
    path('contacts', views.contacts, name='contacts-page'),
]