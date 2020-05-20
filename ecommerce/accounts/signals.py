from django.contrib.auth.signals import user_logged_in
from django.conf import settings
from .models import UserStripe
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
import stripe

User = get_user_model()

stripe.api_key = settings.STRIPE_SECRET_KEY

def get_or_create_user_stripe(user):
	try:
		user.userstripe.stripe_id
	except UserStripe.DoesNotExist:
		customer = stripe.Customer.create(
			email = str(user.email)
			)
		new_user_stripe = UserStripe.objects.create(
			user = user,
			stripe_id = customer.id
			)
	except:
		pass

def user_created(sender, instance, created, *args, **kwargs):
	if created:
		get_or_create_user_stripe(instance)

post_save.connect(user_created, sender=User)

#if we decide to change stripe id
# def get_or_create_stripe(sender, user, *args, **kwargs):
# 	try:
# 		user.userstripe.stripe_id
# 	except UserStripe.DoesNotExist:
# 		customer = stripe.Customer.create(
# 			email = str(user.email)
# 			)
# 		new_user_stripe = UserStripe.objects.create(
# 			user = user,
# 			stripe_id = customer.id
# 			)
# 	except:
#		pass
# user_logged_in.connect(get_or_create_stripe)