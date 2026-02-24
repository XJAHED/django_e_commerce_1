from django.urls import path
from Dashboard.views import CustomAdmin

urlpatterns = [
    path('admin/', CustomAdmin, name="CustomAdmin")
]
