# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def herokuapp_robots_view(request):
    """
    Add restrictive robots.txt to prevent sites under *.herokuapp.com from being indexed.
    """

    response_text = ""
    http_host = request.get_host()

    if http_host and 'herokuapp' in http_host:
        response_text = "User-agent: *\nDisallow: /"

    return HttpResponse(response_text, content_type="text/plain")
