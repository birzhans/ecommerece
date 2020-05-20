from .views import all, single
from django.urls import path

urlpatterns = [
    path('', all, name='all'), 
    path('<str:slug>', single, name='single'),  
]