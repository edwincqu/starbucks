from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Question
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
	birthdate = forms.DateField()
	question = forms.ModelChoiceField(queryset=Question.objects.all(), to_field_name="name")
	answer = forms.CharField()
	card_number = forms.IntegerField()
	pin_code = forms.IntegerField()
	accept_terms = forms.BooleanField()
	receive_news = forms.BooleanField()


	class Meta:
		model = User
		fields = (
			"username",
			"first_name",
			"last_name",
			"email",
			"password1",
			"password2",
			"birthdate",
			"question",
			"answer",
			"card_number",
			"pin_code",
			"accept_terms",
			"receive_news")

	def save(self, commit=True):
		user = super(UserCreateForm, self).save()
		if user:
			instance = Person(
				user=user,
				birthdate = self.cleaned_data['birthdate'],
				question = self.cleaned_data['question'],
				answer = self.cleaned_data['answer'],
				card_number = self.cleaned_data['card_number'],
				pin_code = self.cleaned_data['pin_code'],
				accept_terms = self.cleaned_data['accept_terms'],
				receive_news = self.cleaned_data['receive_news'])
			instance.save()
		return user


