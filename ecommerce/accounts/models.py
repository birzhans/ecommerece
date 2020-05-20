from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.conf import settings
import stripe


class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	stripe_id = models.CharField(max_length=100)

	def __str__(self):
		return str(self.stripe_id)

