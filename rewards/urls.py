from . import views
try:
    from django.urls import include, path
    urlpatterns = [
	path('', views.IndexView.as_view(), name="index"),
	path('createuser/', views.UserCreationView.as_view(), name="create-user"),
    ]

except Exception as e:
    from django.conf.urls import url, include
    urlpatterns = [
	url('', views.IndexView.as_view(), name="index"),
	url('createuser/', views.UserCreationView.as_view(), name="create-user"),
    ]

    pass
#from django.urls import path




#urlpatterns = [
#	path('', views.IndexView.as_view(), name="index"),
#	path('createuser/', views.UserCreationView.as_view(), name="create-user"),
#]
