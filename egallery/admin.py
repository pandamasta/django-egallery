from django.contrib import admin

# Register your models here.
from egallery.models import *

# Funtion to delete selected picture and its related thumb
def delete_model(modeladmin, request, queryset):
    for obj in queryset:
        storage, path = obj.picture.storage, obj.picture.path
        obj.picture.delete_thumbnails()
        storage.delete(path) #delete original picture
        obj.delete()
delete_model.short_description = "Delete selected picture and its thumbs"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','is_public','description','created']
    prepopulated_fields = {"slug": ("title",)}

class PictureAdmin(admin.ModelAdmin):
    list_display = ['title','image_img','description','created','gallery']
    list_filter = ('gallery',)
    prepopulated_fields = {"slug": ("title",)}
    actions = [delete_model]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Picture,PictureAdmin)

