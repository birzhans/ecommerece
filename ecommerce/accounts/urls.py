from django.urls import path
from .views import *


urlpatterns = [
	path('logout', logout_view, name='logout'),
	path('login', login_view, name='login'),
	path('registration', registration_view, name='registration'),
]