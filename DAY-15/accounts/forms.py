from django.forms import ModelForm

from django.contrib.auth.models import User

from.models import UserProfile


class UserUpdateForm(ModelForm):
	class Meta:
		model=User

		fields=['first_name','last_name','username','email']


class ProfileUpdateForm(ModelForm):
	class Meta:
		model=UserProfile

		fields=['image','dob','mobileno']