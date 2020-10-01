from django.shortcuts import render,redirect

from .forms import EntryForm

from.models import Entry

# Create your views here.


def home(request):
	data=Entry.objects.all()
	return render(request,'entries/home.html',{'data':data})



def addentry(request):
	if request.method=="POST":
		form=EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form=EntryForm()
		return render(request,'entries/addentry.html',{'form':form})