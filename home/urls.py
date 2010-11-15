# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('home.views',
    url(r'^$', 'index', name='home_page'),
    url(r'^verse/$', 'verse_index', name='verse_index'),
    url(r'^verse/(?P<id>\d+)$', 'verse_detail', name='verse_detail'),
    url(r'^verse/(?P<id>\d+)/edit$', 'verse_edit', name='verse_edit'),
    url(r'^author/$', 'author_index', name='author_index'),
    url(r'^author/(?P<id>\d+)$', 'author_detail', name='author_detail'),
    url(r'^author/(?P<id>\d+)/edit$', 'author_edit', name='author_edit'),
    url(r'^author/create$', 'author_create', name='author_create'),
    url(r'^about_us$', 'about_us', name='about_us'),
    url(r'^contact_us$', 'contact_us', name='contact_us'),
    url(r'^search$', 'search', name='search'),
)
