from django.shortcuts import render, get_object_or_404, redirect
from banner.models import *
from Books.models import *
from .models import Subscriber
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import BookFilter
# from Books.models import Book
# from .models import Book
# Create your views here.

def shop_page_filter(request):

    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    
    context = {
        'filter': book_filter
    }
    return render(request, 'html/shop/v1.html', context)

# def shop_page_category_filter(request):
#     Category_Filter = CategoryFilter(request.GET, queryset=Category.objects.all())
#     context = {
#         'filter': Category_Filter,
#         'categorys': Category_Filter.qs,
#     }
#     return render(request, 'html/shop/v1.html', context)

def home_page(request):
    context ={}
    
    banners = Banner.objects.all()
    context['banners'] = banners
    
    on_offers = on_offer.objects.all()
    context['on_offers'] = on_offers
    
    sale_offers = sale_offer.objects.all()
    context['sale_offers'] = sale_offers
    
    book = Book.objects.all()
    biography_books = Book.objects.filter(category__name="Biographies")
    context['biography_books']=biography_books
    context['books'] = book
    
    author = Author.objects.all()
    context['authors']=author
    return render(request, 'html/index.html', context)

def Subscriber_user(request):
    if request.method == "POST":
        email = request.POST.get('subscriber')
        if not Subscriber.objects.filter(email=email).exists():
            Subscriber.objects.create(email=email)
            messages.success(request, "Subscribed Successfully")
        else:
            messages.warning(request, "Already Subscribed")

    return redirect('home_page')

def shop_page(request):
    context = {}

    authors = Author.objects.all()
    authors = Author.objects.filter(book__isnull=False).distinct()
    categorys = Category.objects.all()
    categorys= Category.objects.filter(book__isnull=False).distinct()
    formats = Format.objects.all()
    formats= Format.objects.filter(book__isnull=False).distinct()

    books = Book.objects.all()

    category_id = request.GET.get('category')
    if category_id:
        books = books.filter(category_id=category_id)
    
    author_id = request.GET.get('author')
    if author_id:
        books = books.filter(author_id=author_id)
    
    format_id= request.GET.get('format')
    if format_id:
        books = books.filter(format_id=format_id)


    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['authors'] = authors
    context['categorys'] = categorys
    context['formats'] = formats
    context['books'] = page_obj

    return render(request, 'html/shop/v1.html', context)

def single_book(request,id):
    context={}
    
    book = get_object_or_404(Book, id=id)
    context['books']=book
    
    related_books = Book.objects.filter(category=book.category).exclude(id=id)
    context['related_books']=related_books
    
    return render(request, "html/shop/single-product-v1.html", context)
