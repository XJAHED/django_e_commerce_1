from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from banner.models import *
from Books.models import *
# Create your views here.
@login_required
def CustomAdmin(request):
    # context ={}
    return render(request, "html/dashboard/admin.html")

@login_required
def custom_table(request):
    return render(request, "html/dashboard/side-menu-light-post.html")

@login_required
def banner_section(request):
    context ={}
    banners = Banner.objects.all()
    on_offers = on_offer.objects.first()
    sale_offers = sale_offer.objects.first()
    context['banners'] = banners
    context['on_offers'] = on_offers
    context['sale_offers'] = sale_offers
    return render(request, 'html/dashboard/admin.html', context)

@login_required
def add_banner(request):
    if request.method == "POST":
        title = request.POST.get('title')
        is_active =True if request.POST.get('is_active') else False
        description = request.POST.get('description')
        image = request.FILES.get('image')
        banner = Banner(title=title, is_active=is_active, description=description, image=image)
        banner.save()
        messages.success(request, "Banner Add Successfully")
        return redirect('dashboard:banner_section')
    return render(request, "html/dashboard/add_banner.html")

@login_required
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
        return redirect('dashboard:banner_section')
    context = {
        'banner': banner
    }
    return render(request, 'html/dashboard/side-menu-light-post.html', context)

@login_required
def banner_delete(request, id):
    banner = get_object_or_404(Banner, id=id)
    banner.delete()
    messages.success(request, "Banner Delete Successfully")
    return redirect('dashboard:banner_section')

@login_required
def on_sale_banner(request):
    return render(request, 'html/dashboard/on_sale.html')

@login_required
def on_sale_banner(request, id):
    on_sale = get_object_or_404(sale_offer, id=id)
    if request.method == "POST":
        on_sale.title = request.POST.get('title')
        on_sale.discount = request.POST.get('discount')
        on_sale.save()
        messages.success(request, "Updated Successfully")
        return redirect('dashboard:banner_section')

    context={}
    context['on_offer'] = on_sale
    return render(request, 'html/dashboard/on_sale.html', context)

@login_required
def edit_offer_banner(request, id):
    edit_offer = get_object_or_404(on_offer, id=id)
    if request.method == "POST":
        edit_offer.title = request.POST.get('title')
        edit_offer.discount = request.POST.get('discount')
        edit_offer.save()
        messages.success(request, "Updated Successfully")
        return redirect('dashboard:banner_section')
    context={}
    context['edit_offer'] = edit_offer
    return render(request, 'html/dashboard/edit_offer.html', context)

def all_books(request):
    context = {}
    book = Book.objects.all()
    context['books'] = book
    return render(request, 'html/dashboard/Books.html', context)

def add_book(request):
    return render(request, 'html/dashboard/add_book.html')




def book_category_page(request):
    context ={}
    category = Category.objects.all()
    context['categorys'] = category
    return render(request, "html/dashboard/books_category.html", context)

def product_by_category(request,id):
    context ={}
    category = get_object_or_404(Category,id=id)
    book = Book.objects.filter(category=category)
    context['categorys'] = category
    context['books'] = book
    return render(request, "html/dashboard/product_by_category.html", context)

def product_by_author(request,id):
    context ={}
    author = get_object_or_404(Author,id=id)
    book = Book.objects.filter(author=author, stock__gt=0)
    context['books'] = book
    context['author'] = author
    return render(request, "html/dashboard/product_by_category.html", context)



def edit_category(request, id):
    edit_category = get_object_or_404(Category,id=id)
    if request.method == "POST":
        edit_category.name = request.POST.get('name')
        edit_category.save()
        messages.success(request,"Updated Successfully")
        return redirect('dashboard:book_category_page')
    context={}
    context['edit_category'] = edit_category
    return render(request, 'html/dashboard/edit_category.html', context)

def book_category_delete(request, id):
     delete_category = get_object_or_404(Category,id=id)
     delete_category.delete()
     messages.success(request, "Banner Delete Successfully")
     return redirect('dashboard:book_category_page')

def add_book_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category = Category(name=name)
        category.save()
        messages.success(request, "Category Add Successfully")
        return redirect('dashboard:book_category_page')
    return render(request, "html/dashboard/add_book_category.html")

def author(request):
    context ={}
    author = Author.objects.all()
    context["authors"] = author
    return render(request, 'html/dashboard/author.html', context)