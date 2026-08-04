from django.urls import path

from .views import *


urlpatterns = [
    path('blog/', blog, name='blog'),
    path('dashboard/blog/', dashboard_blog, name="dashboard_blog"),
    path('dashboard/blog/post/',post_blog, name="post_blog"),
    path('dashboard/blog/edit/<int:id>', edit_blog, name="edit_blog"),
    path('dashboard/blog/delete/<int:id>', delete_blog, name="delete_blog")
]
