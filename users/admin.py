from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass