from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
import os, random
# Create your models here.
def upload_image_path(instance, filename):
    extention = filename.split(".")[1]
    filename = f"{instance.title}-{random.randint(100000, 999999)}.{extention}"
    return os.path.join('Blog/', filename)



class Blog(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(auto_now=True)
    discription = RichTextField(null=True, blank=True)
    image = ResizedImageField(size=[500,300], quality=80,upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return str(self.title)