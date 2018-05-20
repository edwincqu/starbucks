from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
	name = models.CharField(max_length=200)
	state = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Person(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	birthdate  = models.DateField(blank=False, null=False)
	question = models.ForeignKey(
		Question,
		on_delete=models.CASCADE)
	answer = models.CharField(max_length=200, blank=False, null=False)
	card_number = models.IntegerField(blank=False, null=False)
	pin_code = models.IntegerField(blank=False, null=False)
	accept_terms = models.BooleanField(default=False)
	receive_news = models.BooleanField(default=False)
	state = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{first_name} {last_name}".format(
			first_name = self.user.first_name,
			last_name = self.user.last_name)
