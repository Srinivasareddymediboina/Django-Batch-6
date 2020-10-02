from django.urls import path

from.views import home,register,signup

urlpatterns = [
	path('',home),
	path('register/',register,name="register"),
	path('signup/',signup,name="signup")
	]