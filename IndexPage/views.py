from django.shortcuts import render, get_object_or_404, redirect
from banner.models import *
from Books.models import *
from .models import Subscriber
from django.contrib import messages


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