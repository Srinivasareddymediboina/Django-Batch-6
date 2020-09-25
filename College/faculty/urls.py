from django.urls import path
from faculty import views

urlpatterns = [
	path('register/',views.register,name='fregister')
]