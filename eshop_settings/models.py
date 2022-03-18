import os
import random
from django.db import models


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)

    return name, ext


def upload_image_path(instance, filepath):
    new_name = random.randint(100000, 999999)
    name, ext = get_filename_ext(filepath)
    final_name = f"{new_name}-{instance.title}{ext}"

    return f"website/{final_name}"


class FooterSetting(models.Model):
    title = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    phone_number = models.IntegerField()
    mobile_number = models.IntegerField()
    email = models.EmailField()
    image_web_site = models.ImageField(upload_to=upload_image_path,null=True, blank=True)
    copy_right = models.CharField(max_length=200, default='copy right text')
    about = models.TextField(default='about text')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
