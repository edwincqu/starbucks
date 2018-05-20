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


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'form-control'})
		self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'required': True})
		self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'required': True})
		self.fields['email'].widget.attrs.update({'class': 'form-control', 'required': True})
		self.fields['password1'].widget.attrs.update({'class': 'form-control'})
		self.fields['password2'].widget.attrs.update({'class': 'form-control'})
		self.fields['birthdate'].widget.attrs.update({'class': 'form-control', 'required': True})
		self.fields['question'].widget.attrs.update({'class': 'custom-select custom-select-sm', 'required': True})
		self.fields['answer'].widget.attrs.update({'class': 'form-control', 'required': True})
		self.fields['card_number'].widget.attrs.update({'class': 'form-control', 'required': True})
		self.fields['pin_code'].widget.attrs.update({'class': 'form-control', 'required': True})
		self.fields['accept_terms'].widget.attrs.update({'class': 'form-check-input', 'required': True})
		self.fields['receive_news'].widget.attrs.update({'class': 'form-check-input', 'required': True})


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


