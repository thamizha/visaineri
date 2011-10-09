Installation
============

Pre-requisites
--------------

* [Django](https://www.djangoproject.com/)
* [Django Pagination](http://code.google.com/p/django-pagination/)
* [Django South](http://south.aeracode.org/)
* [PyParsing](http://pyparsing.wikispaces.coms
* [Beautiful soup](http://www.crummy.com/software/BeautifulSoup/)

These can be installed like so:

    sudo easy_install django django-pagination south pyparsing beautifulsoup

Getting the code
----------------

    cd /path/to/parent/
    git clone git://github.com/justjkk/visaineri.git
    cd visaineri
    git submodules update --init

Setting up
----------

    cd /path/to/visaineri/
    cp localsettings.py.sample localsettings.py

* Edit localsettings.py with database and debug information
* `python manage.py validate` should return 0 errors
* `python manage.py syncdb --migrate`

Testing the Site
----------------

* `python manage.py runserver`
* Point your browser [here](http://localhost:8000).
* Test the site's functionality.
* Log into [admin page](http://localhost:8000/admin) and explore the admin interface.
