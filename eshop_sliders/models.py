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

    return f"sliders/{final_name}"


class Slider(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
