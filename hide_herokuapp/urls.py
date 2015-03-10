# -*- coding: utf-8 -*-
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('hide_herokuapp.views',
    url(r'^$', herokuapp_robots_view),
)
