from django.urls import path

from accounts.views import home,register,signin,signout,changepassword,profile,updateprofile

urlpatterns = [
	path('',home,name="home"),
	path('register/',register,name="register"),
	path('signin',signin,name="signin"),
	path('changepassword',changepassword,name="changepassword"),
	path('profile',profile,name="profile"),
	path('updateprofile',updateprofile,name="updateprofile"),
	path('signout',signout,name='signout'),
	]