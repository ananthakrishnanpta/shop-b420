from django.urls import path
from .views import viewCart

urlpatterns = [
    path('', viewCart, name='view_cart')
]