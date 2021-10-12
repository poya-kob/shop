from django.contrib import admin

from .models import Comment, Category, Product, ProductGallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created_at', 'updated_at']
    list_filter = ['is_active', 'in_stock', 'created_at', 'updated_at']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
    '''
    use the prepopulated_fields attribute to specify fields where
    the value is automatically set using the value of other fields.
    '''
    search_fields = ('name',)
    date_hierarchy = 'updated_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('created', 'updated')
    list_display = ('user', 'product', 'created')
    search_fields = ('name', 'content')


# @admin.register(models.ProductGallery)
# class ProductGalleryAdmin(admin.ModelAdmin):
#     pass
admin.site.register(ProductGallery)
