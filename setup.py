#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import re
import os
import sys


name = 'django-hide-herokuapp'
package = 'hide_herokuapp'
author = 'Isaac Slavitt'
author_email = 'isaac@drivendata.org'
url = 'https://github.com/isms/django-hide-herokuapp/'
description = 'Direct search engines not to index *.herokuapp.com URLs.'
license = 'MIT License'
install_requires = ['Django', 'mock']
keywords = ['django', 'heroku', 'herokuapp']


def read_file(filename):
    """
    Read a file into a string
    """
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.

    from: https://github.com/zapier/django-drip
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a v%(version)s -m 'version v%(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name=name,
    version=get_version(package),
    packages=[package],
    include_package_data=True,
    install_requires=install_requires,
    keywords=keywords,
    license=license,
    description=description,
    long_description=read_file('README.rst'),
    url=url,
    author=author,
    author_email=author_email,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
