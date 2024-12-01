from django.shortcuts import render,redirect
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

def deleteUser(request,id):
    data=Signup.objects.get(id=id)
    data.delete()
    return redirect('userView')
def UpdateUser(request,id):
    data=Signup.objects.get(id=id)
    if request.method =='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact=request.POST.get('contact')
        age=request.POST.get('age')
        dob=request.POST.get('dob')
        gender = request.POST.get('gender')
        language=request.POST.getlist('language')
        lang=','.join(language)
        qualification = request.POST.get('qualification')
        data.name=name
        data.address=address
        data.email=email
        data.password=password
        data.contact=contact
        data.age=age
        data.dob=dob
        data.gender=gender
        data.language=lang
        data.qualification=qualification
        data.save()
        
    return render(request,'updateUser.html',{'data':data})
    