from django.urls import path
from . import views


urlpatterns = [
    path('/add-products', views.AdditionalProductsPage, name='add-products-page'),
]