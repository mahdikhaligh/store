from django.db import models
from datetime import datetime


class Contact(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=datetime.now())
    is_read = models.BooleanField()

    def __str__(self):
        return self.fullname
