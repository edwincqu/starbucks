from django.urls import path
from . import views


urlpatterns = [
	path('createuser/', views.UserCreationView.as_view(), name="create-user"),
]
