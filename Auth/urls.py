from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('duplicate_email/',duplicate_email, name="duplicate_email"),
    path('logout/',user_logout,name="user_logout"),
    path('profile/', profile, name="profile"),
]
