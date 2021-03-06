from django.urls import reverse_lazy
from django.shortcuts import render
from django.forms import inlineformset_factory
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person
from .forms import UserCreateForm

class IndexView(TemplateView):
    template_name = "index.html"


class UserCreationView(CreateView):
	model = User
	form_class = UserCreateForm
	success_url = reverse_lazy('create-user')
