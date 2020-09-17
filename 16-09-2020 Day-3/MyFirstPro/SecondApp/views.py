from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	return HttpResponse("Hello This is my first django project")

def hi(request):
	name="Srinivas "
	return HttpResponse("Hi Hello "+name)

def names(request,s):
	print(type(s))
	return HttpResponse('Hello '+s)

def rollno(request,r):
	return HttpResponse('My Rollno is {}'.format(r))

def task(request,name,roll):
	return HttpResponse("<h1>My Name is {} <br> my rollno is {} </h1>".format(name,roll))

def home(request):
	return render(request,'SecondApp/home.html')