# -*- coding: utf-8 -*-
try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from hide_herokuapp.views import herokuapp_robots_view


urlpatterns = [
    url(r'^robots\.txt$', herokuapp_robots_view),
]
