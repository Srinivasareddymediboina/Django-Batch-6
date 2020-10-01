from django.urls import path

from .views import home,addentry

urlpatterns = [
	path('',home,name="home"),
	path('addentry/',addentry,name="addentry")
	]