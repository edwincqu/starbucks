from django.contrib import admin

from .models import Question, Person

admin.site.register(Question)
admin.site.register(Person)

