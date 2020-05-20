from django.db import models
from carts.models import Cart
from django.contrib.auth import get_user_model

User = get_user_model()

STATUS_CHOICES = (
	('started', 'started'),
	('abandoned', 'abandoned'),
	('finished', 'finished'),
)

class Order(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	final_total = models.IntegerField(default=0)
	order_id = models.CharField(max_length=100, unique=True)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	status = models.CharField(max_length=20, 
		choices=STATUS_CHOICES, default='started')
	time = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return self.order_id



