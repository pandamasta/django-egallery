=====
django-egallery
=====

        [ !! APP NOT FINISH TO BE USED AS EXPECTED !! ]
     [ !! README WILL BE UPDATED WHEN ALL WILL BE READY !! ]


django-egallery is a simple Django app to conduct Web-based pictures Gallery. 

The app use 3rd app:
    - django easy-thumbnails (powerfull thumbnails system) https://github.com/SmileyChris/easy-thumbnails
    - fancybox (zooming functionality for image)  https://github.com/fancyapps/fancyBox
    - rowGrid.js (lightweight jQuery plugin) https://github.com/brunjo/rowGrid.js


Quick start
-----------

1. Install required apps throught pip

   pip install easy-thumbnails
   pip install egallery (will be upload to pip)

2. Add "egallery" + easy_thumbnails to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'egallery',
          'easy_thumbnails', 
      )

3. Include the polls URLconf in your project urls.py like this::

      url(r'^gallery/', include('gallery.urls')),

4. Add profiles thumbnails in settings.py

    THUMBNAIL_ALIASES = {
        '': {
            'avatar': {'size': (50, 50), 'crop': True},
            'index': {'size': (50, 200), 'crop' : 'scale'},
            'large': {'size': (50, 400), 'crop' : 'scale'},
        },
    }

5. Don't forget to declare STATIC_URL and STATICFILES_DIRS in your settings.py

    eg:
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [(os.path.join(BASE_DIR, "static"))]


6. Run `python manage.py syncdb` to create the gallery models.

7. Start the development server and visit http://127.0.0.1:8000/admin/
   to add categories and pictures.

8. Visit http://127.0.0.1:8000/gallery/ to see the gallery.

Errors:
-------

InvalidImageFormatError at /admin/egallery/picture/
The source file does not appear to be an image

If you get InvalidImageFormatError after you trying to upload an image, it means that
pillow (installed with easy_thumbnails) doesn't have the jpeg support 

1) Uninstall Pillow
    pip uninstall Pillow    
2)
Install these following packages

    eg: Debian
    sudo apt-get install python-dev build-essential 
    sudo apt-get install libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev

3) Reinstall Pillow

    pip install Pillow

4) Check that you get JPEG support a the end of the compilation of Pillow

    PIL SETUP SUMMARY
    ----------------------
    .. 
    --- JPEG support available
    ..


