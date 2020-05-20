from .views import *
from django.urls import path

urlpatterns = [
    path('cart', view, name='view'),
    path('cart/<str:slug>/', add_to_cart, name='add_to_cart'),
    path('cart/<int:id>', remove_from_cart, name='remove_from_cart'),
]

