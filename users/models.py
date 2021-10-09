from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Multi-Address'

    def __str__(self):
        return f"{self.address}"
