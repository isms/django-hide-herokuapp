# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class HideHerokuappFromRobotsMiddleware(object):
    def process_response(self, request, response):
        """
        Add the header to prevent sites under *.herokuapp.com from being indexed.
        """
        http_host = request.get_host()

        if http_host and 'herokuapp' in http_host:
            response['X-Robots-Tag'] = 'noindex, nofollow'

        return response
