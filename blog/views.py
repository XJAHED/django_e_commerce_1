from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
# Create your views here.

# Frontend
def blog(request):
    context = {}
    blog = Blog.objects.all()
    context['blogs'] = blog
    return render(request, 'html/blog/blog-v1.html', context)



# Dashboard
def dashboard_blog(request):
    context ={}
    blog = Blog.objects.all()
    context['blogs'] = blog
    return render(request, 'html/dashboard/Blog.html', context)

def post_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        discription = request.POST.get('discription')
        image = request.FILES.get('image')
        blog = Blog(title=title, discription=discription, image=image)
        blog.save()
        messages.success(request, "Add Successfully")
        return redirect('dashboard_blog')

    return render(request, 'html/dashboard/post_blog.html')

def edit_blog(request, id):
    edit = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        edit.title = request.POST.get('title')
        edit.discription = request.POST.get('discription')
        if request.FILES.get('image'):
            edit.image = request.FILES.get('image')
        edit.save()
        messages.success(request, "Update Successfully")
        return redirect('dashboard_blog')
    context={}
    context['blogs']=edit
    return render(request, 'html/dashboard/edit_blog.html',context)


def delete_blog(request, id):
    delete_blog = get_object_or_404(Blog, id=id)
    delete_blog.delete()
    messages.success(request, "Book delete Successfully")
    return redirect('dashboard_blog')