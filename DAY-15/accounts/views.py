from django.shortcuts import render,redirect


from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout

from.models import UserProfile

from .forms import UserUpdateForm,ProfileUpdateForm

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
				login(request,user)
				messages.success(request,'password successully updated..!')
				return redirect('/')
			else:
				messages.error(request,"password doesn't match ")
				return render(request,'accounts/changepassword.html')
		else:
			return render(request,'accounts/changepassword.html')


def profile(request):
	user=User.objects.get(id=request.user.id)
	pro=UserProfile.objects.get(user=user)
	context={'user':user,'pro':pro}
	return render(request,'accounts/profile.html',context)

def updateprofile(request):
	user=User.objects.get(id=request.user.id)
	pro=UserProfile.objects.get(user=user)
	if request.method=="POST":
		uform=UserUpdateForm(request.POST,instance=request.user)
		pform=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
		if uform.is_valid() and pform.is_valid():
			uform.save()
			pform.save()
			messages.success(request,'profile successully Updated..!')
			return redirect('profile')
		else:
			messages.error(request,'not updated..!')
			return render(request,'accounts/updateprofile.html')
	else:
		uform=UserUpdateForm(instance=user)
		pform=ProfileUpdateForm(instance=pro)
		context={'user':user, 'pro':pro, 'uform':uform,'pform':pform}
		return render(request,'accounts/updateprofile.html',context)



def signout(request):
	logout(request)
	return redirect('/')