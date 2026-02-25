from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from django_cleanup import cleanup
import random
import os
# Create your models here.

def image_upload_path(instance, filename):
    extetion = filename.split(".")[1]
    filename = f"{instance.title}_{random.randint(100000, 999999)}.{extetion}"
    return os.path.join('Banner/',filename)


@cleanup.select
class Banner(models.Model):
    description = RichTextField(max_length=250)
    title = models.CharField(max_length=50, null=True, blank=True)
    image = ResizedImageField(size=[500,300], quality=75,upload_to=image_upload_path, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


