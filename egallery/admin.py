from django.contrib import admin

# Register your models here.
from egallery.models import *

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['title','is_public','description','created']
    prepopulated_fields = {"slug": ("title",)}


class PictureAdmin(admin.ModelAdmin): 
    list_display = ['title','image_img','description','created','gallery']
    list_filter = ('gallery',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Picture,PictureAdmin)

