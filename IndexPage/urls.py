from django.urls import path
from .views import *



urlpatterns = [
    path('',home_page, name='home_page'),
    path('subscriber/', Subscriber_user, name="Subscriber_user"),
    path('shop_page/',shop_page, name="shop_page"),
    path('shop_page/single_book/<int:id>', single_book, name="single_book")
]
