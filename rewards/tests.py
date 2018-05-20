from django.test import TestCase
from .models import Person, Question
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date, parse_datetime
from datetime import datetime

class PersonTestCase(TestCase):

	def setUp(self):
		user =  User.objects.create(
			password='sha1$6efc0$f93efe9fd7542f25a7be94871ea45aa95de57161',
			is_superuser=False,
			username='testclient',
			first_name='Test',
			last_name='Client',
			email='testclient@example.com',
			is_staff=False,
			is_active=True)
		if user:
			pass
			
			# Person.objects.create(
			# 	user = user,
			# 	birthdate  = parse_date("12-12-2018"),
			# 	question = Question.objects.get(pk='3'),
			# 	answer = "test",
			# 	card_number = int("461712846"),
			# 	pin_code = int("890"),
			# 	accept_terms = True,
			# 	receive_news = True)

	# def test_str(self):
	# 	user = User.objects.get(username="edwincq")
	# 	self.assertEqual(user.__str__(), 'edwincq')
