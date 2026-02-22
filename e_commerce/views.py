from django.shortcuts import render
from banner.models import Banner


# # Create your views here.

def home_page(request):
    context ={}
    banners = Banner.objects.all()
    context['banners'] = banners
    return render(request, 'html/index.html', context)