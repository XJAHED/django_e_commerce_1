from django.urls import path
from Dashboard.views import CustomAdmin, custom_table, editdata, banner_delete, add_banner

app_name = "dashboard"

urlpatterns = [
    path('', CustomAdmin, name="CustomAdmin"),
    path('table/', custom_table, name="custom_table"),
    path('add_banner/', add_banner, name="add_banner"),
    path('editdata/<int:id>/', editdata, name='editdata'),
    # path('editdata/<int:id>/', edit_banner, name='edit_banner')
    path('banner_delete/<int:id>/', banner_delete, name='banner_delete'),

]
