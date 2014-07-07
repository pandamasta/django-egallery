=====
django-egallery
=====

django-egallery is a simple Django app to conduct Web-based Gallery. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "egallery" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'egallery',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^gallery/', include('gallery.urls')),

3. Add profiles thumbnails in settings.py

    THUMBNAIL_ALIASES = {
        '': {
            'avatar': {'size': (50, 50), 'crop': True},
            'index': {'size': (50, 200), 'crop' : 'scale'},
            'large': {'size': (50, 400), 'crop' : 'scale'},
        },
    }


4. Run `python manage.py syncdb` to create the gallery models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create and add Picture. You'll need the Admin app enabled.

6. Visit http://127.0.0.1:8000/gallery/ to see the gallery.
