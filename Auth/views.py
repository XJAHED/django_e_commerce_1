from django.shortcuts import render, redirect, get_object_or_404
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

def profile(request, id):
    user_obj = get_object_or_404(user, id=id)
    if request.method =="POST":
        user_obj.name= request.POST.get('name')
        user_obj.phone_number= request.POST.get('phone_number')
        user_obj.save()
        messages.success(request, "Update Successfully")
        return redirect('profile', id=request.user.id)
    return render(request, 'html/dashboard/profile.html')

def change_password(request):
    if request.method =="POST":
        current_pass = request.POST.get('password')
        new_pass = request.POST.get('new_password')
        confirm_pass = request.POST.get('confirm_password')
        
        user = request.user
        
        if not user.check_password(current_pass):
            messages.error(request, "Current password incorrect")
            return redirect('change_password')
        if new_pass != confirm_pass:
            messages.error(request,"Password not match")
            return redirect('change_password')
        
        user.set_password(new_pass)
        user.save()
        messages.success(request,"Password changed successfully")
        return redirect('login')
    return render(request, 'html/dashboard/profile.html')

def change_profile(request,id):
    profile = get_object_or_404(user, id=id)
    if request.method == "POST":
        if request.FILES.get('image'):
           profile.profile = request.FILES.get('image')
        profile.save()
        messages.success(request, "Profile Updated Successfully")
        return redirect('profile', id=request.user.id)

    return render(request, 'html/dashboard/profile.html')