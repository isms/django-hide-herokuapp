# -*- coding: utf-8 -*-
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

from hide_herokuapp.views import herokuapp_robots_view


urlpatterns = patterns('',
    url(r'^$', herokuapp_robots_view),
)
