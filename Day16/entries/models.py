from django.db import models

# Create your models here.


class Entry(models.Model):

	text=models.TextField()
	date_text=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.date_text
