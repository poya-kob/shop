from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from utils import upload_image_path


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, )

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_list',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Images(models.Model):
    product = models.ForeignKey('Product', default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)


class Comment(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments',
                                related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
