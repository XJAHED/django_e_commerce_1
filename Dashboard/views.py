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
    context={}
    authors = Author.objects.all()
    categorys = Category.objects.all()
    all_formats = Format.objects.all()
    context['formats'] = all_formats
    context['categorys'] = categorys
    context['authors'] = authors
    if request.method =="POST":
        name = request.POST.get('name')
        short_details= request.POST.get('short_details')
        description= request.POST.get('description')
        author_id= request.POST.get('author')
        author_instance = Author.objects.get(id=author_id)
        
        category_id= request.POST.get('category')
        category_instance = Category.objects.get(id=category_id)
        
        date= request.POST.get('date')
        book_code= request.POST.get('book_code')
        price= request.POST.get('price')
        discount_price= request.POST.get('discount_price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        
        format_id = request.POST.get('format')
        format_instance = Format.objects.get(id=format_id)
        page = request.POST.get('page')
        language = request.POST.get('language')

        book = Book(name=name, short_details=short_details, description=description, author=author_instance, category=category_instance, publication_data=date, book_code = book_code, price=price, discount_price=discount_price,stock=stock, image=image, format=format_instance, page=page, language=language)
        book.save()
        messages.success(request, "Add Successfully")
        return redirect('dashboard:all_books')
    return render(request, 'html/dashboard/add_book.html', context)



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
def author_edit(request, id):
    edit = get_object_or_404(Author, id=id)
    if request.method == "POST":
        edit.name = request.POST.get('name')
        edit.description = request.POST.get('description')
        if request.FILES.get('image'):
            edit.image = request.FILES.get('image')
        edit.save()
        messages.success(request, "Update Successfully")
        return redirect('dashboard:author')
    context={}
    context['author'] = edit
    return render(request, 'html/dashboard/author_edit.html', context)
def author_delete(request,id):
    delete = get_object_or_404(Author, id=id)
    delete.delete()
    messages.success(request, "Banner Delete Successfully")
    return redirect('dashboard:author')
def author_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        author = Author(name=name, description=description, image=image)
        author.save()
        messages.success(request, "Add Successfully")
        return redirect('dashboard:author')
    return render(request, "html/dashboard/author_add.html")