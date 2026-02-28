from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# # Create your views here.

# def home_page(request):
#     context ={}
#     banners = Banner.objects.all()
#     on_offers = on_offer.objects.all()
#     sale_offers = sale_offer.objects.all()
#     context['banners'] = banners
#     context['on_offers'] = on_offers
#     context['sale_offers'] = sale_offers
#     return render(request, 'html/index.html', context)

@login_required
def admin_page(request):
    users = User.objects.all()
    return render(request, "html/dashboard/dashboard.html", {"users": users})

