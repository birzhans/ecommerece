from django.shortcuts import render, redirect, reverse
from carts.models import Cart
from .models import Order
import time
from django.contrib.auth.decorators import login_required
from .utils import id_generator
# Create your views here.

def orders(request):
	template = 'orders/user.html'
	context = {}
	return render(request, template, context)

@login_required
def checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None

	try:
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		new_order = Order(cart=cart, order_id=id_generator())
		new_order.user = request.user
		new_order.save()
	except:
		return redirect(reverse('view'))
	

	if new_order.status == 'finished':
		del request.session['cart_id']
		del request.session['cart_items_total']
		return redirect(reverse('view'))


	return redirect(reverse('view'))