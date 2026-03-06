from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
import os
import random
from django_cleanup import cleanup
# Create your models here.

def admin_profile(instance, filename):
    extention = filename.split(".")[-1]
    filename = f"{instance.name}-{random.randint(100000, 999999)}.{extention}"
    return os.path.join('User/', filename)
@cleanup.select
class user(AbstractUser):
    first_name = None
    last_name = None
    
    class RoleData(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CUSTOMER = 'customer', 'Customer'
    
    profile = ResizedImageField(size=[300,200],quality=80,upload_to=admin_profile, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank= True, null = True)
    role = models.CharField(max_length=10,choices=RoleData.choices, default='customer')
