from django.shortcuts import render, reverse, redirect
from products.models import Product, Variation
from .models import Cart, CartItem
# Create your views here.

def view(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
	if the_id:
		new_total = 0

		for item in cart.cartitem_set.all():
			line_total = item.product.price * item.quantity
			new_total += line_total

		request.session['cart_items_total'] = cart.cartitem_set.count()
		cart.total = new_total
		cart.save()
		context = {'cart': cart } 

	else:
		message = "Your cart is empty"
		context = {"empty": True, 'message': message}

	template = 'carts/view.html'

	return render(request, template, context)

def add_to_cart(request, slug):

	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)

	try:
		product = Product.objects.get(slug__iexact=slug)
	except:
		pass

	product_variations = []

	if request.method == 'POST':
		quantity = request.POST['quantity']
		# if int(quantity) <= 0:
		for item in request.POST:
			key = item
			val = request.POST[key]
			try:
				variation = Variation.get(product=product, category__iexact=key, title__iexact=val)
				product_variations.append(variation)
			except:
				pass

		cart_item = CartItem.objects.create(cart=cart, product=product)

		if len(product_variations) > 0:
			cart_item.variations.clear()
			cart_item.variations.add(*product_variations)
		cart_item.quantity = int(quantity)
		cart_item.save()


		
		return redirect(reverse('view'))
	return redirect(reverse('view'))



def remove_from_cart(request, id):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		return redirect(reverse('view'))
	cart_item = CartItem.objects.get(id=id)
	cart_item.cart = None
	cart_item.save()
	return redirect(reverse('view'))








