from django.conf.urls import url
from django.views.generic import TemplateView

from models import *
from views import *


urlpatterns = [
            url(r'^$', GalleryMainList.as_view(), name='gallery-all'),
            url(r'^(?P<cat>\w+)/$', GalleryDetailedList.as_view(), name='gallery-cat'),
            ]
