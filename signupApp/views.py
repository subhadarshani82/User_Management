from django.shortcuts import render

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
        language=request.POST['language']
        qualification = request.POST['qualification']
        print(name,address,password,email,contact,age,dob,gender,language,qualification)
    return render(request,'create_user.html')