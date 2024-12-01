from django.shortcuts import render
from . models import *
# Create your views here.
def userCreate(request):
    if request.method =='POST':
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        password=request.POST['password']
        contact=request.POST['contact']
        age=request.POST['age']
        dob=request.POST['dob']
        gender = request.POST['gender']
        language=request.POST.getlist('language')
        lang=','.join(language)
        qualification = request.POST['qualification']
        print(name,address,password,email,contact,age,dob,gender,lang,qualification)
        data=Signup(name=name,address=address,password=password,email=email,contact=contact,age=age,dob=dob,gender=gender,language=lang,qualification=qualification)
        data.save()
    return render(request,'create_user.html')


def userView(request):
    data=Signup.objects.all()
    return render(request,'view_user.html',{'data':data})