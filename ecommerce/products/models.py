from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100, null=False, blank=False, unique=True)
	description = models.TextField(default='No description')
	price = models.IntegerField()
	slug = models.SlugField(unique=True)
	time = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('single', kwargs={'slug': self.slug})

class Image(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/images/')

	def __str__(self):
		return self.product.title

class VariationManager(models.Manager):
	def licenses(self):
		return self.all().filter(category='license')

	def packages(self):
		return super(VariationManager, self).filter(active=True).filter(category='package')


VAR_CATEGORIES = (
		('license', 'license'),
		('package', 'package')
	)



class Variation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	category = models.CharField(max_length=100, choices=VAR_CATEGORIES, default='license')
	title = models.CharField(max_length=100)
	price = models.IntegerField(null=True, blank=True)
	active = models.BooleanField(default=True) 
	image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.CASCADE)
	objects = VariationManager()
	def __str__(self):
		return self.product.title + " " + self.title