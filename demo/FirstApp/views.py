from django.shortcuts import render
from django.http import HttpResponse


def maths_table(request,val):
    # data = {}
    # for i in range(1,11):
    #     data[i] = i*val
    # return render(request,"maths_table.html",{'data':data, 'num':val})
    data_list = []
    for i in range(1,11):
        data_list.append(i*val) # [3,6,9,...30]
    return render(request,"maths_table.html",{'list':data_list,'num':val})


def login(request):
    static_name = 'admin'
    static_pswd = '12345'
    if request.method == 'POST':
        user_name = request.POST.get('name')
        pswd = request.POST.get('password')
        if (static_name == user_name) and (static_pswd == pswd):
            return HttpResponse("user logged In successfully")
        return HttpResponse('Invalid Details!!')
    return render(request,'login.html')