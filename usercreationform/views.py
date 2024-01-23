from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home_view(request):
    return render(request,'home.html')

def signup_view(request):
    if request.method == 'POST':

        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        upass = request.POST.get('password')

        my_user = User.objects.create_user(uname,uemail,upass)
        my_user.save()
        messages.success(request,"User Created Successfully")
        return redirect('/')
    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request,"invalid Credential!")

    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


