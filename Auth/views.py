from django.shortcuts import render, redirect
# from e_commerce import Auth
from Auth.models import *
from .models import *
from django.contrib import messages
from django.contrib.auth import  authenticate, login as auth_login, logout
# Create your views here.

def register(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password =request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, "Wrong password & confirm password")
            return redirect('register')
        
        if user.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        username = email.split('@')[0]
        admin_user = user.objects.create_user(username=username, email=email, phone_number=phone, password=password, name=name)
        
        messages.success(request, "Register successful")
        admin_user.save()
        return redirect('login')
    return render(request, 'html/dashboard/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # email = email.lower()
        password = request.POST.get("password")
        user_obj = user.objects.filter(email=email)
        if user_obj.exists():
            username = user_obj.first().username
            user_instance = authenticate(username=username, password=password)
            # print(user)
            if user_instance is not None:
                auth_login(request, user_instance)
                return redirect('dashboard:CustomAdmin')
            else:
                messages.error(request, "Invalid credentials")
        else:
             messages.error(request, "Invalid credentials")
        return redirect('login')
        
    return render(request, 'html/dashboard/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    # user_obj = user.objects.get(all)
    return render(request, 'html/dashboard/profile.html')