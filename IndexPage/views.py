from django.shortcuts import render, get_object_or_404, redirect
from banner.models import *
from Books.models import *
from .models import Subscriber
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
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
    context={}
    author = Author.objects.all()
    context['authors']=author
    category = Category.objects.all()
    context['categorys']=category
    format = Format.objects.all()
    context['formats']=format
    
    book = Book.objects.all()
    # context['books']=book
    
    paginator = Paginator(book, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['books']=page_obj
    
    return render(request, 'html/shop/v1.html', context)

def single_book(request,id):
    context={}
    
    book = get_object_or_404(Book, id=id)
    context['books']=book
    
    related_books = Book.objects.filter(category=book.category).exclude(id=id)
    context['related_books']=related_books
    
    return render(request, "html/shop/single-product-v1.html", context)