from django.db import models
from utils import upload_image_path, get_file_name


class Slider(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return self.title
