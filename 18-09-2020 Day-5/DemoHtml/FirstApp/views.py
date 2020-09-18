from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'FirstApp/home.html')

def table(request):
	return render(request,'FirstApp/table.html')

def forms(request):
	return render(request,'FirstApp/forms.html')