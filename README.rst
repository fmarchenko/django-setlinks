=====
SetLinks
=====



Quick start
-----------

1. Add "setlinks" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'setlinks',
    )

2. Include the setlinks URLconf in your project urls.py like this::

    url(r'^setlinks/', include('setlinks.urls')),

3. Run `python manage.py migrate` to create the setlinks models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a setlinks (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/setlinks/ to participate in the setlinks.