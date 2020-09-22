from django.urls import path
from . import views

urlpatterns = [
    path('maths/table/<int:val>', views.maths_table, name='maths_table'),
    path('login', views.login, name='first_login'),
    ]