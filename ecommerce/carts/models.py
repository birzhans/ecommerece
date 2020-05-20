from django.db import models
from products.models import Product, Variation
# Create your models here.

class CartItem(models.Model):
	variations = models.ManyToManyField(Variation, blank=True)
	cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	line_total = models.IntegerField(default=0)

	def __str__(self):
		return str(self.id)

class Cart(models.Model):
	total = models.IntegerField(default=0)

	def __str__(self):
		return str(self.id)





