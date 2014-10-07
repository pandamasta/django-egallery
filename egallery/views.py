from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from egallery.models import *

class GalleryMainList(ListView):

    template_name = 'egallery/index.html'
    model = Picture

    def get_queryset(self):
        return Picture.objects.filter(gallery__is_public=True)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context

        all_active_rubrique = Category.objects.filter(is_public=True)
        context = super(GalleryMainList, self).get_context_data(**kwargs)
        context['categories'] = all_active_rubrique
        return context

class GalleryDetailedList(ListView):

    template_name = 'egallery/index.html'
    model = Picture

    def get_queryset(self):
        self.gallery_choice = get_object_or_404(Category, title=self.kwargs['cat'])
        return Picture.objects.filter(gallery__title=self.gallery_choice)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        all_active_rubrique = Category.objects.filter(is_public=True)
        context = super(GalleryDetailedList, self).get_context_data(**kwargs)
        context['categories'] = all_active_rubrique
        context['currentcategorie'] = Category.objects.get(title=self.kwargs['cat'])
        return context
