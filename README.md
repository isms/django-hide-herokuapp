django-hide-herokuapp
=====================

Django app for Heroku users designed to hide your `*.herokuapp.com`
from search engine results.

Use case
--------

You want to develop a website called `artisanalraisinbeer.com` using
Django deployed on Heroku. You write a little bit of Django code and
create a new Heroku app called `artisanalraisinbeer` to deploy to.

While developing, you can visit your site by going to this URL:

    http://artisanalraisinbeer.herokuapp.com

Eventually, you finish the first version of your website, buy the
domain name `artisanalraisinbeer.com`, and set everything up
so that you can view the site just by going to the following URL:

    http://www.artisanalraisinbeer.com

You can still visit `http://artisanalraisinbeer.herokuapp.com`, which
is fine&mdash;but there's one problem: you want your main site to show
up in search results, *not* your `.herokuapp.com` site.

How it works
------------

This app goes about this two ways: [robots.txt](http://www.robotstxt.org/robotstxt.html)
and the [X-Robots-Tag](https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag).
Why both? _To be double-plus sure..._ :eyes:

If `herokuapp` seems to be in the [originating host](https://docs.djangoproject.com/en/1.7/ref/request-response/#django.http.HttpRequest.get_host)
of the user request, then we do two things:

  * Put the following in `robots.txt`:

    ```
    User-agent: *
    Disallow: /
    ```
  * Set `X-Robots-Tag` in our response header to `noindex, nofollow`.

For search engines that respect these settings, they should start to ignore these sites
in future crawls.

Quick start
-----------

1. Add `'hide_herokuapp'` to your INSTALLED_APPS setting.

2. Add the `HideHerokuappFromRobotsMiddleware` middleware to your `MIDDLEWARE_CLASSES`
   like this:
   ```
   MIDDLEWARE_CLASSES = (
       ...
       'hide_herokuapp.middleware.HideHerokuappFromRobotsMiddleware',
   )
   ```

3. Include the `hide_herokuapp` URLconf in your project `urls.py` like this:
   ```
   urlpatterns = patterns('',
       ...
       url(r'^robots\.txt$', include('hide_herokuapp.urls')),
       ...
   )
   ```