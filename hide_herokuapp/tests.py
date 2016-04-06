# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.test import TestCase

from mock import Mock

from hide_herokuapp.middleware import HideHerokuappFromRobotsMiddleware
from hide_herokuapp.views import herokuapp_robots_view


class TestHideHerokuappFromRobotsMiddleware(TestCase):
    def setUp(self):
        self.middleware = HideHerokuappFromRobotsMiddleware()

    def test_process_non_herokuapp_response(self):
        request = Mock(path='/')
        request.get_host = lambda: 'drivendata.org'
        response = HttpResponse()
        response = self.middleware.process_response(request, response)

        self.assertIsInstance(response, HttpResponse)
        self.assertNotIn('X-Robots-Tag', response)

    def test_process_herokuapp_response(self):
        request = Mock(path='/')
        request.get_host = lambda: 'phoney-baloney-1337.herokuapp.org'
        response = HttpResponse()
        response = self.middleware.process_response(request, response)

        self.assertIsInstance(response, HttpResponse)
        self.assertIn('X-Robots-Tag', response)
        self.assertEqual(response['X-Robots-Tag'], 'noindex, nofollow')


class TestHideHerokuappFromRobotsView(TestCase):
    def test_process_non_herokuapp_response(self):
        request = Mock(path='/')
        request.get_host = lambda: 'drivendata.org'
        response = herokuapp_robots_view(request)

        self.assertNotIn('Disallow', response.content)

    def test_process_herokuapp_response(self):
        request = Mock(path='/')
        request.get_host = lambda: 'phoney-baloney-1337.herokuapp.org'
        response = herokuapp_robots_view(request)

        self.assertIn('Disallow', response.content)

    def test_robots_url_configured(self):
        robots_url = '/robots.txt'
        response = self.client.get(robots_url)

        self.assertEqual(response.status_code, 200)
