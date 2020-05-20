from django.shortcuts import render
from .models import Product, Image
# Create your views here.

def home(request):
	template = 'products/home.html'
	context = {'products': Product.objects.all()}
	return render(request, template, context)


def all(request):
	query = request.GET.get('query')
	if query:
		products = Product.objects.filter(title__icontains=query)
		context = {'products': products, 'query': query}
	else:
		context = {'products': Product.objects.all()}
	template = 'products/all.html'
	return render(request, template, context)


def single(request, slug):
	product = Product.objects.get(slug__iexact=slug)
	template = 'products/single.html'
	images = Image.objects.filter(product=product)
	context = {'product': product, 'images': images}
	return render(request, template, context)



