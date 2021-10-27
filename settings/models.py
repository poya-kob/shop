import os

from django.db import models


from utils import upload_image_path


class SiteSetting(models.Model):
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    about_us = models.TextField(null=True, blank=True)
    copy_right = models.CharField(max_length=200, null=True, blank=True)
    logo_image = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return self.title
