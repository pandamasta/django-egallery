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
    picture = ThumbnailerImageField(upload_to='egallery', blank=True)
    description = models.TextField(_('description'),blank=True)

    created = models.DateTimeField(_('Created'), auto_now_add=True, null=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True, null=True)
    view_count = models.PositiveIntegerField(_('view count'), default=0, editable=False)
    gallery = models.ForeignKey(Category)
    #saved_file.connect(generate_aliases_global)

    def image_img(self):
        if self.picture:
            return u'<img src="%s" />' % self.picture['avatar'].url
        else:
            return '(No pic)'

    image_img.allow_tags = True

    #Seems to be a good way, but it doesn't work
    #
    #Receive the pre_delete signal and delete the file associated with the model instance.
    #from django.db.models.signals import post_delete
    #from django.dispatch.dispatcher import receiver

    #@receiver(post_delete, sender=Picture)
    #def photo_post_delete_handler(sender, **kwargs):
    #    pic = kwargs['instance']
    #    storage, path = pic.picture.storage, pic.path
    #    storage.delete(path)

    #Overriding the delete method
    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.picture.storage, self.picture.path

        # Delete the model before the file
        super(Picture, self).delete(*args, **kwargs)

        # Delete pictures after the model
        self.picture.delete_thumbnails()
        storage.delete(path) #delete original picture

    def __str__(self):              # __unicode__ on Python 2
                return self.title



