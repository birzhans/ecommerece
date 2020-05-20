from django.urls import path
from .views import *

urlpatterns = [
	path('checkout', checkout, name='checkout'),
	path('', orders, name='user_orders'),
]