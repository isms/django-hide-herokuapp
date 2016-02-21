import os
from setuptools import setup


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-hide-herokuapp',
    version='0.2',
    packages=['hide_herokuapp'],
    include_package_data=True,
    keywords=['django', 'heroku', 'herokuapp'],
    license='MIT License',
    description='Direct search engines not to index *.herokuapp.com URLs.',
    long_description=read_file('README.rst'),
    url='https://github.com/isms/django-hide-herokuapp/',
    author='Isaac Slavitt',
    author_email='isaac@drivendata.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
