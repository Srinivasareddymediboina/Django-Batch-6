from django.db import models

# Create your models here.
class Student_Register(models.Model):
	branches = (
		('ece','ECE'),
		('cse','CSE'),
		('it','IT'),
		('mech','MECH')
		)

	First_name = models.CharField(max_length=20)
	Last_name = models.CharField(max_length=15,blank=True,null=True)
	Roll_No = models.CharField(max_length=15)
	Branch = models.CharField(max_length=5,choices=branches)
	Email = models.EmailField(unique=True)
	Phone = models.CharField(max_length=10, help_text='Enter your 10 digit mobile number')

	def __str__(self):
		return self.Roll_No

	class Meta:
		db_table = 'Students_data'