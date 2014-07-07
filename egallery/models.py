from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.
# Inspired from https://github.com/jdriscoll/django-photologue/blob/master/photologue/models.py
from easy_thumbnails.fields import ThumbnailerImageField

class Category(models.Model):
    title = models.CharField(_('title'), max_length=50 ,unique=True)
    slug = models.SlugField(_('title slug'),unique=True, help_text=_('A "slug" is a unique URL-friendly title for an object.'))
    description = models.TextField(_('description'), blank=True)

    is_public = models.BooleanField(_('is public'), default=True, help_text=_('Public galleries will be displayed in the default views.'))
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    

    class Meta:
        ordering = ['created']
        #get_latest_by = 'date_added'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):              # __unicode__ on Python 2
                    return self.title
    
    #tags = TagField(help_text='Tag of the gallery', verbose_name=_('tags'), blank=True, null=True)

class Picture(models.Model):
    title = models.CharField(_('title'),max_length=50,unique=True)
    slug = models.SlugField(_('title slug'),unique=True,help_text=_('A "slug" is a unique URL-friendly title for an object.'))
    picture = ThumbnailerImageField(upload_to='static/gallery', blank=True) 
    description = models.TextField(_('description'),blank=True)
    price = models.IntegerField (_('price'),null=True,blank=True)

    original_size_h = models.IntegerField (_('height'),null=True,blank=True)
    original_size_w = models.IntegerField (_('width'),null=True,blank=True)
    original_size_p = models.IntegerField (_('depth'),null=True,blank=True)

    created = models.DateTimeField(_('Created'), auto_now_add=True, null=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True, null=True)
    view_count = models.PositiveIntegerField(_('view count'), default=0, editable=False)
    gallery = models.ForeignKey(Category)
    #saved_file.connect(generate_aliases_global)

    def image_img(self):
        if self.picture:
            return u'<img src="/%s" />' % self.picture['avatar'].url
        else:
            return '(No pic)'

    image_img.allow_tags = True

   
    def __str__(self):              # __unicode__ on Python 2
                return self.title



