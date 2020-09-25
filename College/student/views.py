from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *


def register(request):
	if request.method=='POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		roll = request.POST.get('roll')
		branch = request.POST.get('branch')
		email = request.POST.get('mail')
		mobile = request.POST.get('phone')

		obj = Student_Register(First_name = fname,
			Last_name=lname,Roll_No=roll,Branch=branch,Email=email,Phone=mobile)
		obj.save()
		return redirect('data')
	return render(request,'student/register.html')

def show(request):
	data = Student_Register.objects.all()
	return render(request,'student/data.html',{'data':data})


def update(request,num):
	obj = Student_Register.objects.get(id=num)
	if request.method == 'POST':
		obj.First_name = request.POST.get('fname')
		obj.Last_name = request.POST.get('lname')
		obj.Roll_No = request.POST.get('roll')
		obj.Branch = request.POST.get('branch')
		obj.Email = request.POST.get('mail')
		obj.Phone = request.POST.get('phone')
		obj.save()
		return redirect('student_data')
	return render(request,'student/update_student.html',{'data':obj})


def delete(request,num):
	obj = Student_Register.objects.get(id=num)
	obj.delete()
	return redirect('student_data')


def home(request):
	return render(request,'student/abut.html')