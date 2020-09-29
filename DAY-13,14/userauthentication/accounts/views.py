from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout

from.models import UserProfile

from django.contrib import messages

# Create your views here.



def home(request):
	return render(request,'accounts/home.html')



def register(request):
	if request.method=="POST":
		fname=request.POST['first_name']
		lname=request.POST['last_name']
		uname=request.POST['username']
		em=request.POST['emailid']
		img=request.FILES['image']
		pwd=request.POST['password']
		user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=em,password=pwd)
		UserProfile.objects.create(user=user,image=img)
		messages.success(request,'%s is successully Registred..!'%(uname))
		return redirect('signin')
	else:
		return render(request,'accounts/register.html')


def signin(request):
	if request.method=="POST":
		uname=request.POST['username']
		pwd=request.POST['password']
		user=authenticate(username=uname,password=pwd)
		if user:
			login(request,user)
			messages.info(request,"%s logged successully"%(uname))
			return redirect('/')
		else:
			messages.warning(request,'invalid username or password')
			return render(request,'accounts/signin.html')
	else:
		return render(request,'accounts/signin.html')


def changepassword(request):
	if not request.user.is_authenticated:
		return redirect('signin')
	else:
		if request.method=="POST":
			old=request.POST['oldpwd']
			new=request.POST['newpwd']
			con=request.POST['conpwd']
			if new == con:
				user=User.objects.get(username__exact=request.user.username)
				user.set_password(new)
				user.save()
				messages.success(request,'password successully updated..!')
				return redirect('signout')
			else:
				messages.error(request,"password doesn't match ")
				return render(request,'accounts/changepassword.html')
		else:
			return render(request,'accounts/changepassword.html')



def signout(request):
	logout(request)
	return redirect('/')