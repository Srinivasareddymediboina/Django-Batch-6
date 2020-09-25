from django.urls import path
from student import views


urlpatterns = [
	path('register/',views.register,name='register'),
	path('show/',views.show,name='student_data'),
	path('edit/<int:num>', views.update, name='student_update'),
	path('delete/<int:num>', views.delete, name='student_delete'),
	path('',views.home, name='home'),
]