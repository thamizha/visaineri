# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),

    (r'^account/', include('registration.backends.simple.urls')),
    
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'', include('home.urls')),
)
