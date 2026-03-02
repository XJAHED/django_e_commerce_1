from django.urls import path
from .views import *



urlpatterns = [
    path('',home_page, name='home_page'),
    path('subscriber/', Subscriber_user, name="Subscriber_user")

]
