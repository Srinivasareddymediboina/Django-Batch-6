from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'FirstApp/home.html')


def table(request):
    return render(request, 'FirstApp/table.html')


def forms(request):
    if request.method == 'POST':
        uname = request.POST['name']
        uemail = request.POST['email']
        udob = request.POST['dob']
        ubranch = request.POST['branch']
        ugender = request.POST['gender']
        return render(request, 'FirstApp/data.html', {'uname': uname, 'uemail': uemail,
                                                      'udob': udob, 'ubranch': ubranch, 'ugender': ugender})
    return render(request, 'FirstApp/forms.html')


def names(request, names):
    return render(request, 'FirstApp/names.html', {'names': names})


def college(request):
    col = "St Ann's College Chirala"
    return render(request, 'FirstApp/college.html', {'college': col})


def numbers(request, num):
    l = []
    for i in range(1, num + 1):
        l.append(i)

    return render(request, 'FirstApp/numbers.html', {'num': l})
