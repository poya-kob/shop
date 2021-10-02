from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created_at', 'updated_at']
    list_filter = ['is_active','in_stock', 'created_at', 'updated_at']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
    '''
    use the prepopulated_fields attribute to specify fields where
    the value is automatically set using the value of other fields.
    '''
    search_fields = ('name',)
    date_hierarchy = 'updated_at'


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ( 'created', 'updated')
    list_display = ('user', 'product', 'created')
    search_fields = ('name', 'content')



@admin.register(models.Images)
class ImagesAdmin(admin.ModelAdmin):
    pass