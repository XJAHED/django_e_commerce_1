from django.shortcuts import render
from banner.models import *
from Books.models import *

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
    context['books'] = book
    
    return render(request, 'html/index.html', context)
