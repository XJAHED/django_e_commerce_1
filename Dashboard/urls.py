from django.urls import path
from Dashboard.views import CustomAdmin, custom_table, editdata, banner_delete, add_banner, banner_section, on_sale_banner, edit_offer_banner

app_name = "dashboard"

urlpatterns = [
    path('', CustomAdmin, name="CustomAdmin"),
    path('table/', custom_table, name="custom_table"),
    path('banner_section/',banner_section, name='banner_section'),
    path('banner_section/add_banner/', add_banner, name="add_banner"),
    path('banner_section/editdata/<int:id>/', editdata, name='editdata'),
    path('banner_delete/<int:id>/', banner_delete, name='banner_delete'),
    path('banner_section/on_sale/<int:id>/', on_sale_banner, name="on_sale_banner"),
    path('banner_section/edit_offer/<int:id>/', edit_offer_banner, name="edit_offer_banner")
    
]
