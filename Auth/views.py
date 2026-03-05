from django.shortcuts import render, redirect
# from e_commerce import Auth
from Auth.models import *
from .models import *
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method =="POST":
        username = request.POST.get('name')
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
        admin_user = user.objects.create_user(username=username, email=email, phone_number=phone, password=password)
        admin_user.save()
        return redirect('register')
    return render(request, 'html/dashboard/register.html')

def login(request):
    return render(request, 'html/dashboard/login.html')

