from django.db import models
from django_resized import ResizedImageField
# Create your models here.
# class all_books(models.Model):
class books(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True),
    price = models.DecimalField( max_digits=10, decimal_places=2, default=0),
    discount_price = models.DecimalField( max_digits=10, decimal_places=2, default=0),
    image = ResizedImageField(size=[500,300], quality=80, null=True, blank=True),
    
    
    