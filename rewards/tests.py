from django.test import TestCase
from .models import Person
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from datetime import datetime

class PersonTestCase(TestCase):

	def setUp(self):
		user =  User.objects.create(
			password='sha1$6efc0$f93efe9fd7542f25a7be94871ea45aa95de57161',
			last_login=datetime.datetime(2006, 12, 17, 7, 3, 31),
			is_superuser=False,
			username='testclient',
			first_name='Test',
			last_name='Client',
			email='testclient@example.com',
			is_staff=False,
			is_active=True,
			date_joined=datetime.datetime(2006, 12, 17, 7, 3, 31))
		if user:
			Person.objects.create(
				user = user,
				birthdate  = parse_date("12-12-2018"),
				question = Question.objects.get(id='8'),
				answer = "test",
				card_number = int("461712846"),
				pin_code = int("890"),
				accept_terms = True,
				receive_news = True)

	def test_str(self):
		person = Person.objects.get(user__username="edwincq")
		self.assertEqual(person.__str__(), 'Edwin Calsin Quinto')
