from django.db import models
from django_resized import ResizedImageField
from django_cleanup import cleanup
import os
from ckeditor.fields import RichTextField
import random
# Create your models here.

def upload_image_path(instance, filename):
    extention = filename.split(".")[1]
    filename = f"{instance.name}-{instance.book_code}.{extention}"
    return os.path.join('books/', filename)
def author_image_path(instance, filename):
    extention = filename.split(".")[-1]
    filename = f"{instance.name}-{random.randint(100000, 999999)}.{extention}"
    return os.path.join('Author/', filename)


class Category(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name if self.name else "No Name"
class Author(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    image = ResizedImageField(size=[500,300], quality=80,upload_to=author_image_path, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.name if self.name else "No Name"

@cleanup.select
class Book(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    book_code = models.CharField(max_length=250, null=True, blank=True)
    price = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    discount_price = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    image = ResizedImageField(size=[500,300], quality=80,upload_to=upload_image_path, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    short_details = RichTextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name if self.name else "No Name"
    
    @property
    def in_stock(self):
        return self.stock > 0
    
