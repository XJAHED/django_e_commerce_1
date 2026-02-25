from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
# from banner.models import Banner
from banner.models import Banner
# Create your views here.

def CustomAdmin(request):
    # context ={}
    return render(request, "html/dashboard/admin.html")

def custom_table(request):
    return render(request, "html/dashboard/side-menu-light-post.html")

def add_banner(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        is_active =True if request.POST.get('is_active') else False
        description = request.POST.get('description')
        image = request.FILES.get('image')
        banner = Banner(title=title, is_active=is_active, description=description, image=image)
        banner.save()
        messages.success(request, "Banner Updated Successfully")
        return redirect('dashboard:CustomAdmin')
    return render(request, "html/dashboard/add_banner.html")

    

def editdata(request, id):
    banner = get_object_or_404(Banner, id=id)
    if request.method == "POST":
        banner.title = request.POST.get('title')
        banner.description = request.POST.get('description')
        banner.is_active = True if request.POST.get('is_active') == 'on' else False

        if request.FILES.get('image'):
            banner.image = request.FILES.get('image')
        banner.save()
        messages.success(request, "Banner Updated Successfully")
        return redirect('dashboard:CustomAdmin')
    context = {
        'banner': banner
    }
    return render(request, 'html/dashboard/side-menu-light-post.html', context)

def banner_delete(request, id):
    banner = get_object_or_404(Banner, id=id)
    banner.delete()
    messages.success(request, "Banner Delete Successfully")
    return redirect('dashboard:CustomAdmin')