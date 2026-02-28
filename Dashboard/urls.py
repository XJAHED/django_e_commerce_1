from django.urls import path
from Dashboard.views import *

app_name = "dashboard"

urlpatterns = [
    path('', CustomAdmin, name="CustomAdmin"),
    path('table/', custom_table, name="custom_table"),
    path('banner_section/',banner_section, name='banner_section'),
    path('banner_section/add_banner/', add_banner, name="add_banner"),
    path('banner_section/editdata/<int:id>/', editdata, name='editdata'),
    path('banner_delete/<int:id>/', banner_delete, name='banner_delete'),
    path('banner_section/on_sale/<int:id>/', on_sale_banner, name="on_sale_banner"),
    path('banner_section/edit_offer/<int:id>/', edit_offer_banner, name="edit_offer_banner"),
    path('books_category/', book_category_page, name="book_category_page"),
    path('book_category/edit/<int:id>/', edit_category, name="edit_category"),
    path('book_category/edit_category_delete/<int:id>/', book_category_delete, name="category_delete"),
    path('book_category/add_category/', add_book_category, name="add_book_category"),
    path('book_category/book_filter_category/<int:id>', product_by_category, name="product_by_category"),
    path('book_category/book_filter_author/<int:id>', product_by_author, name="product_by_author"),
    path('books/', all_books, name="all_books"),
    path('books/add_book/', add_book, name="add_book"),
    path('author/', author, name="author"),
    path('author/author_edit/<int:id>', author_edit, name="author_edit"),
    path('author/author_delete/<int:id>', author_delete, name="author_delete"),
    path('author/author_add/', author_add, name="author_add"),
    
    
]
