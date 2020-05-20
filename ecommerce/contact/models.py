from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=50)
	subject = models.CharField(max_length=50, default='No subject')
	email = models.EmailField(default='some@email.com')
	message = models.TextField()

	def __str__(self):
		return self.name + ' ' + self.message
		