from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('/result', views.result, name='result'),
]